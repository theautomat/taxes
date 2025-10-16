#!/usr/bin/env python3
"""
Flag potential business expenses from merged transaction data.

Usage:
    python scripts/flag_expenses.py <input_csv> [output_csv]

Example:
    python scripts/flag_expenses.py generated-files/merged/merged_2022.csv generated-files/expenses/flagged_expenses.csv
"""

import csv
import json
import sys
from pathlib import Path
from datetime import datetime


def load_patterns(patterns_file):
    """Load expense patterns from JSON file."""
    with open(patterns_file, 'r') as f:
        return json.load(f)


def match_transaction(description, patterns):
    """
    Match a transaction description against expense patterns.

    Returns:
        tuple: (category_key, category_data, matched_keyword) or (None, None, None)
    """
    if not description:
        return None, None, None

    description_lower = description.lower()
    best_match = None
    best_confidence = None
    matched_keyword = None

    # Check each category
    for cat_key, cat_data in patterns['categories'].items():
        for keyword in cat_data['keywords']:
            if keyword.lower() in description_lower:
                # Track the best match (highest confidence)
                if best_match is None or confidence_rank(cat_data['confidence']) > confidence_rank(best_confidence):
                    best_match = (cat_key, cat_data)
                    best_confidence = cat_data['confidence']
                    matched_keyword = keyword

    if best_match:
        return best_match[0], best_match[1], matched_keyword

    return None, None, None


def confidence_rank(confidence_level):
    """Convert confidence level to numeric rank for comparison."""
    ranks = {'high': 3, 'medium': 2, 'low': 1}
    return ranks.get(confidence_level, 0)


def flag_expenses(input_csv, output_csv, patterns_file):
    """
    Read transactions from input CSV and flag potential expenses.

    Args:
        input_csv: Path to input CSV with transactions
        output_csv: Path to output CSV for flagged expenses
        patterns_file: Path to expense patterns JSON
    """
    patterns = load_patterns(patterns_file)

    flagged_transactions = []
    total_transactions = 0
    flagged_count = 0

    # Read input CSV
    with open(input_csv, 'r') as f:
        reader = csv.DictReader(f)
        required_fields = ['Date', 'Description', 'Amount', 'Source']

        # Validate CSV has required fields
        if not all(field in reader.fieldnames for field in required_fields):
            print(f"Error: Input CSV must contain columns: {', '.join(required_fields)}")
            sys.exit(1)

        for row in reader:
            total_transactions += 1
            description = row.get('Description', '')

            # Try to match against patterns
            cat_key, cat_data, matched_keyword = match_transaction(description, patterns)

            if cat_data:
                # Check if already flagged by another source
                existing_flagged_by = row.get('FlaggedBy', '')

                # Build expense row
                expense_row = {
                    'Date': row['Date'],
                    'Description': row['Description'],
                    'Amount': row['Amount'],
                    'Source': row['Source'],
                    'ExpenseCategory': cat_data['name'],
                    'Deductibility': cat_data['deductibility'],
                    'FlaggedBy': 'pattern_match' if not existing_flagged_by else f"{existing_flagged_by},pattern_match",
                    'Confidence': cat_data['confidence'],
                    'Notes': f"Matched keyword: '{matched_keyword}'"
                }

                # Add any additional notes from pattern
                if 'note' in cat_data:
                    expense_row['Notes'] += f" | {cat_data['note']}"

                # Preserve existing notes if any
                if row.get('Notes'):
                    expense_row['Notes'] = f"{row['Notes']} | {expense_row['Notes']}"

                flagged_transactions.append(expense_row)
                flagged_count += 1

    # Write flagged transactions to output CSV
    if flagged_transactions:
        output_path = Path(output_csv)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        fieldnames = ['Date', 'Description', 'Amount', 'Source', 'ExpenseCategory',
                     'Deductibility', 'FlaggedBy', 'Confidence', 'Notes']

        with open(output_csv, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(flagged_transactions)

        print(f"✓ Processed {total_transactions} transactions")
        print(f"✓ Flagged {flagged_count} potential business expenses ({flagged_count/total_transactions*100:.1f}%)")
        print(f"✓ Results written to: {output_csv}")
        print(f"\nNext steps:")
        print(f"  1. Review flagged expenses in {output_csv}")
        print(f"  2. Verify categories and deductibility")
        print(f"  3. Add/remove transactions as needed")
        print(f"  4. Update expense_patterns.json with new keywords discovered")
        print(f"\nNote:")
        print(f"  - This script is ONE of multiple ways to flag expenses")
        print(f"  - Manual review, spreadsheet research, and other methods can also add flags")
        print(f"  - The 'FlaggedBy' field tracks multiple sources (comma-separated)")
    else:
        print(f"✓ Processed {total_transactions} transactions")
        print(f"✗ No potential expenses found matching patterns")
        print(f"\nConsider:")
        print(f"  - Adding more keywords to expense_patterns.json")
        print(f"  - Checking if input CSV has expected transaction types")


def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/flag_expenses.py <input_csv> [output_csv]")
        print("\nExample:")
        print("  python scripts/flag_expenses.py generated-files/merged/merged_2022.csv generated-files/expenses/flagged_expenses.csv")
        sys.exit(1)

    input_csv = sys.argv[1]

    # Default output path with timestamp
    if len(sys.argv) >= 3:
        output_csv = sys.argv[2]
    else:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        output_csv = f"generated-files/expenses/flagged_expenses_{timestamp}.csv"

    # Patterns file path (relative to script)
    script_dir = Path(__file__).parent
    patterns_file = script_dir.parent / "generated-files/expenses/expense_patterns.json"

    if not Path(input_csv).exists():
        print(f"Error: Input file not found: {input_csv}")
        sys.exit(1)

    if not patterns_file.exists():
        print(f"Error: Patterns file not found: {patterns_file}")
        sys.exit(1)

    flag_expenses(input_csv, output_csv, patterns_file)


if __name__ == "__main__":
    main()
