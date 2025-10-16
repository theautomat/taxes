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
import logging
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


def setup_logging(log_file):
    """Set up logging to file and console."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler(sys.stdout)
        ]
    )
    return logging.getLogger(__name__)


def flag_expenses(input_csv, output_csv, patterns_file, log_file):
    """
    Read transactions from input CSV and flag potential expenses.

    Args:
        input_csv: Path to input CSV with transactions
        output_csv: Path to output CSV for flagged expenses
        patterns_file: Path to expense patterns JSON
        log_file: Path to log file
    """
    logger = setup_logging(log_file)

    logger.info("=" * 80)
    logger.info("EXPENSE FLAGGING SESSION STARTED")
    logger.info("=" * 80)
    logger.info(f"Input file: {input_csv}")
    logger.info(f"Output file: {output_csv}")
    logger.info(f"Patterns file: {patterns_file}")
    logger.info(f"Log file: {log_file}")
    logger.info("")

    patterns = load_patterns(patterns_file)
    logger.info(f"Loaded {len(patterns['categories'])} expense categories from patterns file")
    logger.info("")

    flagged_transactions = []
    total_transactions = 0
    flagged_count = 0
    category_counts = {}

    # Read input CSV
    with open(input_csv, 'r') as f:
        reader = csv.DictReader(f)
        required_fields = ['Date', 'Description', 'Amount', 'Source']

        # Validate CSV has required fields
        if not all(field in reader.fieldnames for field in required_fields):
            logger.error(f"Input CSV missing required columns: {', '.join(required_fields)}")
            sys.exit(1)

        logger.info("Processing transactions...")
        logger.info("")

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

                # Log the flagged transaction
                logger.info(f"FLAGGED: {row['Date']} | ${row['Amount']:>10} | {cat_data['name']}")
                logger.info(f"         Description: {description}")
                logger.info(f"         Matched keyword: '{matched_keyword}' (confidence: {cat_data['confidence']})")
                logger.info(f"         Deductibility: {cat_data['deductibility']}")
                if 'note' in cat_data:
                    logger.info(f"         Note: {cat_data['note']}")
                logger.info("")

                # Track category counts
                category_name = cat_data['name']
                category_counts[category_name] = category_counts.get(category_name, 0) + 1

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

        logger.info("=" * 80)
        logger.info("SUMMARY")
        logger.info("=" * 80)
        logger.info(f"Total transactions processed: {total_transactions}")
        logger.info(f"Total flagged as expenses: {flagged_count} ({flagged_count/total_transactions*100:.1f}%)")
        logger.info("")
        logger.info("Breakdown by category:")
        for category, count in sorted(category_counts.items(), key=lambda x: x[1], reverse=True):
            logger.info(f"  {category}: {count}")
        logger.info("")
        logger.info(f"Results written to: {output_csv}")
        logger.info(f"Log file: {log_file}")
        logger.info("")
        logger.info("Next steps:")
        logger.info("  1. Review flagged expenses in CSV")
        logger.info("  2. Verify categories and deductibility")
        logger.info("  3. Add/remove transactions as needed")
        logger.info("  4. Update expense_patterns.json with new keywords discovered")
        logger.info("")
        logger.info("Note:")
        logger.info("  - This script is ONE of multiple ways to flag expenses")
        logger.info("  - Manual review, spreadsheet research, and other methods can also add flags")
        logger.info("  - The 'FlaggedBy' field tracks multiple sources (comma-separated)")
        logger.info("=" * 80)
    else:
        logger.info("=" * 80)
        logger.info("SUMMARY")
        logger.info("=" * 80)
        logger.info(f"Total transactions processed: {total_transactions}")
        logger.info("No potential expenses found matching patterns")
        logger.info("")
        logger.info("Consider:")
        logger.info("  - Adding more keywords to expense_patterns.json")
        logger.info("  - Checking if input CSV has expected transaction types")
        logger.info("=" * 80)


def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/flag_expenses.py <input_csv> [output_csv]")
        print("\nExample:")
        print("  python scripts/flag_expenses.py generated-files/merged/merged_2022.csv generated-files/expenses/flagged_expenses.csv")
        sys.exit(1)

    input_csv = sys.argv[1]

    # Default output path with timestamp
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    if len(sys.argv) >= 3:
        output_csv = sys.argv[2]
    else:
        output_csv = f"generated-files/expenses/flagged_expenses_{timestamp}.csv"

    # Log file path (same name as output CSV but .log extension)
    log_file = Path(output_csv).with_suffix('.log')

    # Patterns file path (relative to script)
    script_dir = Path(__file__).parent
    patterns_file = script_dir.parent / "generated-files/expenses/expense_patterns.json"

    if not Path(input_csv).exists():
        print(f"Error: Input file not found: {input_csv}")
        sys.exit(1)

    if not patterns_file.exists():
        print(f"Error: Patterns file not found: {patterns_file}")
        sys.exit(1)

    flag_expenses(input_csv, output_csv, patterns_file, log_file)


if __name__ == "__main__":
    main()
