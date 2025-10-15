#!/usr/bin/env python3
"""
Merge all extracted CSV files into one master file.

This script combines all individual CSV files from generated-files/extracted/ into a single
merged CSV file, sorted by date. This creates the "monster CSV" ready for
deduplication and categorization in Airtable or other tools.

Output: generated-files/merged/2022_all-transactions_merged_YYYY-MM-DD.csv

The script only READS from generated-files/extracted/ and never modifies those files.
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
# NOTE: Only reads from extracted/ directory - archived files are never accessed
extracted_dir = os.path.join(project_root, "generated-files", "extracted")
merged_dir = os.path.join(project_root, "generated-files", "merged")
archive_dir = os.path.join(merged_dir, "archive")

# Create merged and archive directories if they don't exist
os.makedirs(merged_dir, exist_ok=True)
os.makedirs(archive_dir, exist_ok=True)

# Archive any existing merged files before creating new one
existing_merged = glob.glob(os.path.join(merged_dir, "2022_all-transactions_merged_*.csv"))
if existing_merged:
    print("=" * 60)
    print("ARCHIVING PREVIOUS MERGED FILES")
    print("=" * 60)
    for old_file in existing_merged:
        filename = os.path.basename(old_file)
        archive_path = os.path.join(archive_dir, filename)
        os.rename(old_file, archive_path)
        print(f"📦 Archived: {filename} → archive/")
    print()

# Generate timestamped output filename
today = datetime.now().strftime("%Y-%m-%d")
output_file = os.path.join(merged_dir, f"2022_all-transactions_merged_{today}.csv")

# WHITELIST: Only merge CSVs from these subdirectories
# Add or remove directories here to control what gets merged
SOURCE_FOLDERS = [
    "wells-fargo",      # Wells Fargo checking account statements
    "privacy-com",      # Privacy.com virtual card transactions
    "nft-genius",       # NFT Genius payroll/income
    # "popstand",       # Popstand income (may not need merging - already has reconciliation docs)
    # "amazon",         # Amazon purchases (uncomment when ready)
]

# Find all CSV files in whitelisted subdirectories for 2022
csv_files = []
for folder in SOURCE_FOLDERS:
    folder_path = os.path.join(extracted_dir, folder)
    if os.path.exists(folder_path):
        pattern = os.path.join(folder_path, "2022*.csv")
        found_files = [f for f in glob.glob(pattern) if "merged" not in f]
        csv_files.extend(found_files)
    else:
        print(f"⚠️  Warning: Folder not found: {folder_path}")

print(f"Merging CSV files from whitelisted folders:")
print(f"Source folders: {', '.join(SOURCE_FOLDERS)}")
print(f"\nFound {len(csv_files)} CSV files to merge:")
for f in sorted(csv_files):
    # Show folder name and filename for clarity
    rel_path = os.path.relpath(f, extracted_dir)
    print(f"  - {rel_path}")
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
            if 'Notes' in row:
                notes = row['Notes'] or ""  # Handle None values
                if filename not in notes:
                    if notes:
                        row['Notes'] = f"{notes} | Merged from: {filename}"
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
    fieldnames = ['Date', 'Description', 'Amount', 'Balance', 'Type', 'Category', 'Source', 'Notes']
    writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')

    writer.writeheader()
    writer.writerows(all_transactions)

print(f"✅ Successfully merged {len(all_transactions)} transactions")
print(f"   Output saved to: {output_file}")
print()

# Validation: Verify transaction counts
print("=" * 60)
print("VALIDATION CHECKS")
print("=" * 60)

# Count transactions per source file (excluding Balance rows)
source_counts = {}
total_expected = 0

for csv_file in csv_files:
    filename = os.path.basename(csv_file)
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        count = sum(1 for row in reader if row.get('Type') != 'Balance')
        source_counts[filename] = count
        total_expected += count

print(f"\n📊 Source File Transaction Counts (excluding Balance rows):")
for filename in sorted(source_counts.keys()):
    print(f"   {filename:45} {source_counts[filename]:4} transactions")

print(f"\n{'Total expected from source files:':48} {total_expected:4} transactions")
print(f"{'Total in merged file:':48} {len(all_transactions):4} transactions")

# Verification
if len(all_transactions) == total_expected:
    print(f"\n✅ VALIDATION PASSED: All transactions accounted for")
else:
    diff = total_expected - len(all_transactions)
    print(f"\n⚠️  VALIDATION WARNING: {abs(diff)} transaction mismatch")
    print(f"   Expected: {total_expected}, Got: {len(all_transactions)}")

# Check for date range
dates = [row['Date'] for row in all_transactions if row['Date']]
if dates:
    print(f"\n📅 Date Range: {min(dates)} to {max(dates)}")

# Check for empty required fields
empty_dates = sum(1 for row in all_transactions if not row.get('Date'))
empty_descriptions = sum(1 for row in all_transactions if not row.get('Description'))
missing_amount = sum(1 for row in all_transactions if not row.get('Amount'))

if empty_dates or empty_descriptions or missing_amount:
    print(f"\n⚠️  Data Quality Issues:")
    if empty_dates:
        print(f"   - {empty_dates} transactions with empty Date")
    if empty_descriptions:
        print(f"   - {empty_descriptions} transactions with empty Description")
    if missing_amount:
        print(f"   - {missing_amount} transactions with no Amount")
else:
    print(f"\n✅ Data Quality: All required fields populated")

print("\n" + "=" * 60)
print("Next steps:")
print("1. Import this CSV into Airtable (or similar tool)")
print("2. Use filters/grouping to identify duplicates visually")
print("3. Mark duplicates and categorize transactions")
print("4. Export clean version to generated-files/final/")
