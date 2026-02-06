#!/usr/bin/env python3
"""
Extract all IKEA transactions from Wells Fargo CSV files.
Output a CSV file with IKEA transactions for office expense tracking.
"""

import csv
import os
import glob
from datetime import datetime

def find_wells_fargo_csvs(base_path):
    """Find all Wells Fargo CSV files in the extracted directory."""
    pattern = os.path.join(base_path, "personal/2022/generated-files/extracted/wells-fargo/*.csv")
    files = sorted(glob.glob(pattern))
    return files

def extract_ikea_transactions(csv_files):
    """Extract all transactions containing 'ikea' (case insensitive)."""
    ikea_transactions = []

    for csv_file in csv_files:
        print(f"Processing: {csv_file}")

        try:
            with open(csv_file, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)

                for row in reader:
                    # Check if 'ikea' appears in the description (case insensitive)
                    description = row.get('Description', '')
                    if 'ikea' in description.lower():
                        ikea_transactions.append(row)
                        print(f"  Found: {row['Date']} - {description} - {row['Amount']}")

        except Exception as e:
            print(f"  Error reading {csv_file}: {e}")
            continue

    return ikea_transactions

def write_ikea_csv(transactions, output_path):
    """Write IKEA transactions to a CSV file."""
    if not transactions:
        print("\nNo IKEA transactions found.")
        return

    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Use the same column headers as the input files
    fieldnames = ['Date', 'Description', 'Amount', 'Balance', 'Type', 'Category', 'Source', 'Notes']

    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(transactions)

    print(f"\n✓ Written {len(transactions)} IKEA transactions to: {output_path}")

def calculate_total(transactions):
    """Calculate total amount from transactions."""
    total = 0.0
    for txn in transactions:
        try:
            amount = float(txn['Amount'])
            total += amount
        except (ValueError, KeyError):
            continue
    return total

def main():
    # Base path is the project root
    base_path = "/home/kurt/Projects/taxes"

    # Find all Wells Fargo CSV files
    csv_files = find_wells_fargo_csvs(base_path)

    if not csv_files:
        print("No Wells Fargo CSV files found.")
        return

    print(f"Found {len(csv_files)} Wells Fargo CSV files\n")

    # Extract IKEA transactions
    ikea_transactions = extract_ikea_transactions(csv_files)

    # Sort by date
    ikea_transactions.sort(key=lambda x: x.get('Date', ''))

    # Calculate total
    total = calculate_total(ikea_transactions)

    # Write to output file
    output_path = os.path.join(base_path, "personal/2022/generated-files/extracted/ikea/2022_ikea_office-expenses.csv")
    write_ikea_csv(ikea_transactions, output_path)

    # Summary
    print(f"\nSummary:")
    print(f"  Total transactions: {len(ikea_transactions)}")
    print(f"  Total amount: ${total:,.2f}")
    print(f"\nNote: Negative amounts indicate expenses/debits")

if __name__ == "__main__":
    main()
