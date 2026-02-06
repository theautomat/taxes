#!/usr/bin/env python3
"""
Fix Wells Fargo CSV files that have the old schema.

Old schema: Date,Description,Amount,Source,Balance,Notes
New schema: Date,Description,Amount,Balance,Type,Category,Source,Notes

This script converts files in-place to match the standard schema.
Amount is negative for expenses, positive for income.
"""

import csv
import os

# Get the project root directory
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_dir)
extracted_dir = os.path.join(project_root, "personal", "2022", "generated-files", "extracted")

# Files to fix (Feb-Dec 2022)
files_to_fix = [
    "2022-02_wells-fargo_checking.csv",
    "2022-03_wells-fargo_checking.csv",
    "2022-04_wells-fargo_checking.csv",
    "2022-05_wells-fargo_checking.csv",
    "2022-06_wells-fargo_checking.csv",
    "2022-07_wells-fargo_checking.csv",
    "2022-08_wells-fargo_checking.csv",
    "2022-09_wells-fargo_checking.csv",
    "2022-10_wells-fargo_checking.csv",
    "2022-11_wells-fargo_checking.csv",
    "2022-12_wells-fargo_checking.csv",
]

print("Fixing Wells Fargo CSV schema...")
print()

for filename in files_to_fix:
    filepath = os.path.join(extracted_dir, filename)

    # Read the file
    rows = []
    with open(filepath, 'r') as f:
        reader = csv.DictReader(f)
        old_headers = reader.fieldnames

        # Check if it needs fixing
        if 'Amount' not in old_headers:
            print(f"⏭️  Skipping {filename} - already has correct schema")
            continue

        for row in reader:
            # Convert to new schema
            amount = float(row['Amount']) if row['Amount'] else 0

            # Determine transaction type
            trans_type = 'Credit' if amount >= 0 else 'Debit'

            # Extract source from old schema or use filename as fallback
            source = row.get('Source', filename)

            new_row = {
                'Date': row['Date'],
                'Description': row['Description'],
                'Amount': str(amount) if amount != 0 else '',
                'Balance': row['Balance'],
                'Type': trans_type,
                'Category': '',  # Empty for now
                'Source': source,
                'Notes': row['Notes']
            }
            rows.append(new_row)

    # Write back with new schema
    with open(filepath, 'w', newline='') as f:
        fieldnames = ['Date', 'Description', 'Amount', 'Balance', 'Type', 'Category', 'Source', 'Notes']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"✅ Fixed {filename} - converted {len(rows)} transactions")

print()
print("Schema fix complete! All Wells Fargo files now use standard schema.")
