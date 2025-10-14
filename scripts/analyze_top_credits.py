#!/usr/bin/env python3
"""
Analyze Wells Fargo CSV files to find the top N largest credits/deposits.

NOTE: Only reads from extracted/ directory by default - archived files are never accessed.
"""

import csv
import glob
import sys
from pathlib import Path
from datetime import datetime

def parse_amount(amount_str):
    """Parse amount string to float."""
    if not amount_str or amount_str.strip() == '':
        return 0.0
    # Remove any whitespace and convert to float
    return float(amount_str.strip())

def analyze_top_credits(pattern, top_n=10, year=None):
    """
    Find the top N largest credits from CSV files matching the pattern.

    Args:
        pattern: Glob pattern for CSV files
        top_n: Number of top credits to return
        year: Optional year filter (e.g., '2022')
    """
    all_credits = []

    # Find all matching CSV files
    csv_files = sorted(glob.glob(pattern))

    if not csv_files:
        print(f"No CSV files found matching pattern: {pattern}")
        return

    print(f"Analyzing {len(csv_files)} CSV files...\n")

    # Process each CSV file
    for csv_file in csv_files:
        filename = Path(csv_file).name

        try:
            with open(csv_file, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)

                for row in reader:
                    # Get amount and filter for positive values (credits)
                    amount = parse_amount(row.get('Amount', '0'))

                    if amount > 0:  # Positive = credit/deposit
                        date = row.get('Date', '')

                        # Apply year filter if specified
                        if year and not date.startswith(year):
                            continue

                        all_credits.append({
                            'date': date,
                            'amount': amount,
                            'description': row.get('Description', ''),
                            'source': row.get('Source', filename),
                            'notes': row.get('Notes', '')
                        })

        except Exception as e:
            print(f"Error processing {filename}: {e}")
            continue

    # Sort by amount (descending) and get top N
    all_credits.sort(key=lambda x: x['amount'], reverse=True)
    top_credits = all_credits[:top_n]

    # Display results
    print(f"Top {top_n} Largest Credits/Deposits:")
    print("=" * 100)
    print(f"{'Rank':<5} {'Date':<12} {'Amount':>12} {'Description':<50} {'Source':<20}")
    print("-" * 100)

    total = 0
    for i, credit in enumerate(top_credits, 1):
        print(f"{i:<5} {credit['date']:<12} ${credit['amount']:>11,.2f} {credit['description'][:50]:<50} {Path(credit['source']).name[:20]:<20}")
        total += credit['amount']

        if credit['notes']:
            print(f"      Notes: {credit['notes']}")

    print("=" * 100)
    print(f"Total of top {top_n}: ${total:,.2f}")
    print(f"\nTotal credits found: {len(all_credits)}")
    print(f"Total of all credits: ${sum(c['amount'] for c in all_credits):,.2f}")

if __name__ == "__main__":
    # Default: analyze Wells Fargo 2022 files
    pattern = "generated-files/extracted/2022-*_wells-fargo_*.csv"
    top_n = 10
    year = "2022"

    # Allow command-line overrides
    if len(sys.argv) > 1:
        pattern = sys.argv[1]
    if len(sys.argv) > 2:
        top_n = int(sys.argv[2])
    if len(sys.argv) > 3:
        year = sys.argv[3]

    analyze_top_credits(pattern, top_n, year)
