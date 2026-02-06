#!/usr/bin/env python3
"""
Merge all Popstand CSV files into one consolidated file.

This script combines individual monthly CSV files from generated-files/extracted/popstand/
into a single consolidated CSV file, sorted by date.
"""

import csv
import os
from datetime import datetime
from pathlib import Path

# Setup paths
script_dir = Path(__file__).parent
project_root = script_dir.parent
popstand_dir = project_root / "generated-files" / "extracted" / "popstand"
output_file = popstand_dir / "2022_popstand_wire-transfers.csv"

# Find all txt files (CSVs) in popstand directory
csv_files = sorted(popstand_dir.glob("*.txt"))

if not csv_files:
    print("ERROR: No CSV files found in popstand directory")
    exit(1)

print(f"Found {len(csv_files)} CSV files to merge:")
for f in csv_files:
    print(f"  - {f.name}")
print()

# Collect all transactions
all_transactions = []
issues_found = []

for csv_file in csv_files:
    print(f"Processing: {csv_file.name}")
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        row_count = 0
        for row in reader:
            # Validate required fields
            if not row.get('Date'):
                issues_found.append(f"  ⚠️  {csv_file.name}: Empty date in row {row_count + 2}")
                continue

            if not row.get('Amount'):
                issues_found.append(f"  ⚠️  {csv_file.name}: Empty amount in row {row_count + 2}")
                continue

            # Add source file tracking
            if 'Source' not in row or not row['Source']:
                row['Source'] = 'Popstand Chase Statement'

            all_transactions.append(row)
            row_count += 1

        print(f"  → {row_count} transactions")

print(f"\nTotal transactions collected: {len(all_transactions)}")

# Sort by date
all_transactions.sort(key=lambda x: x['Date'])

print(f"Sorted transactions by date")

# Write consolidated CSV
with open(output_file, 'w', newline='') as f:
    fieldnames = ['Date', 'Description', 'Amount', 'Balance', 'Type', 'Category', 'Source', 'Notes']
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(all_transactions)

print(f"\n✅ Successfully merged {len(all_transactions)} transactions")
print(f"   Output saved to: {output_file}")

# Validation checks
print("\n" + "=" * 60)
print("VALIDATION CHECKS")
print("=" * 60)

if issues_found:
    print("\n⚠️  Issues Found:")
    for issue in issues_found:
        print(issue)
else:
    print("\n✅ No data quality issues found")

# Check for potential duplicates (same date, same amount)
from collections import defaultdict
date_amount_groups = defaultdict(list)

for txn in all_transactions:
    key = (txn['Date'], txn['Amount'])
    date_amount_groups[key].append(txn)

duplicates = {k: v for k, v in date_amount_groups.items() if len(v) > 1}

if duplicates:
    print(f"\n⚠️  Potential Duplicates Found ({len(duplicates)} groups):")
    for (date, amount), txns in duplicates.items():
        print(f"\n  {date} | ${amount}")
        for i, txn in enumerate(txns, 1):
            notes = txn.get('Notes', '')
            if 'duplicate' in notes.lower():
                print(f"    {i}. [MARKED AS DUPLICATE] {notes}")
            else:
                print(f"    {i}. {notes}")
else:
    print("\n✅ No duplicate transactions found")

# Date range
dates = [txn['Date'] for txn in all_transactions]
print(f"\n📅 Date Range: {min(dates)} to {max(dates)}")

# Calculate total
total = sum(float(txn['Amount']) for txn in all_transactions)
print(f"💰 Total Amount: ${total:,.2f}")

# Monthly breakdown
monthly_totals = defaultdict(float)
monthly_counts = defaultdict(int)

for txn in all_transactions:
    month = txn['Date'][:7]  # YYYY-MM
    monthly_totals[month] += float(txn['Amount'])
    monthly_counts[month] += 1

print(f"\n📊 Monthly Breakdown:")
for month in sorted(monthly_totals.keys()):
    print(f"  {month}: ${monthly_totals[month]:>8,.2f} ({monthly_counts[month]:>2} transfers)")

print("\n" + "=" * 60)
