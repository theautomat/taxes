#!/usr/bin/env python3
"""
Merge all extracted CSV files into one master file.

This script combines all individual CSV files from extracted-data/ into a single
merged CSV file, sorted by date. This creates the "monster CSV" ready for
deduplication and categorization in Airtable or other tools.

Output: merged-data/2022_all-transactions_merged_YYYY-MM-DD.csv

The script only READS from extracted-data/ and never modifies those files.
Each merge run creates a timestamped file so you can track different versions.
"""

import csv
import os
from datetime import datetime
import glob

# Get the project root directory (parent of scripts/)
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_dir)

# Define paths
extracted_dir = os.path.join(project_root, "extracted-data")
merged_dir = os.path.join(project_root, "merged-data")

# Create merged-data directory if it doesn't exist
os.makedirs(merged_dir, exist_ok=True)

# Generate timestamped output filename
today = datetime.now().strftime("%Y-%m-%d")
output_file = os.path.join(merged_dir, f"2022_all-transactions_merged_{today}.csv")

# Find all CSV files in extracted-data/ for 2022 (except previous merged files)
csv_pattern = os.path.join(extracted_dir, "2022*.csv")
csv_files = [f for f in glob.glob(csv_pattern) if "merged" not in f]

print(f"Merging CSV files from: {extracted_dir}")
print(f"Found {len(csv_files)} CSV files to merge:")
for f in sorted(csv_files):
    print(f"  - {os.path.basename(f)}")
print()

# Collect all transactions
all_transactions = []

for csv_file in csv_files:
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Skip balance-only rows (Beginning/Ending Balance)
            if row.get('Type') == 'Balance':
                continue

            # Add source filename to notes if not already there
            filename = os.path.basename(csv_file)
            if 'Notes' in row and filename not in row['Notes']:
                if row['Notes']:
                    row['Notes'] = f"{row['Notes']} | Merged from: {filename}"
                else:
                    row['Notes'] = f"Merged from: {filename}"

            all_transactions.append(row)

print(f"Total transactions collected: {len(all_transactions)}")

# Sort by date
all_transactions.sort(key=lambda x: x['Date'])

print(f"Sorting by date...")

# Write merged CSV
with open(output_file, 'w', newline='') as f:
    # Use the standard column order
    fieldnames = ['Date', 'Description', 'Deposits', 'Withdrawals', 'Balance', 'Type', 'Category', 'Notes']
    writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')

    writer.writeheader()
    writer.writerows(all_transactions)

print(f"✅ Successfully merged {len(all_transactions)} transactions")
print(f"   Output saved to: {output_file}")
print()
print("Next steps:")
print("1. Import this CSV into Airtable (or similar tool)")
print("2. Use filters/grouping to identify duplicates visually")
print("3. Mark duplicates and categorize transactions")
print("4. Export clean version to final-data/")
