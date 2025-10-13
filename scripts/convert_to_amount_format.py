#!/usr/bin/env python3
"""
Convert CSV files from Deposits/Withdrawals format to Amount format.

Old format: Date,Description,Deposits,Withdrawals,Balance,Type,Category,Notes
New format: Date,Description,Amount,Balance,Type,Category,Source,Notes

Conversion rules:
- If Deposits has value -> Amount = +value (positive)
- If Withdrawals has value -> Amount = -value (negative)
- Extract Source from Notes field if present, otherwise use filename
- Preserve all other fields
"""

import csv
import sys
import os
import re
from pathlib import Path


def extract_source_from_notes(notes, fallback_source):
    """Extract source from notes field if present, otherwise use fallback."""
    if not notes:
        return fallback_source, notes

    # Look for pattern: "Source: filename.ext"
    match = re.search(r'Source:\s*([^|]+)', notes)
    if match:
        source = match.group(1).strip()
        # Remove source from notes
        notes = re.sub(r'\s*\|\s*Source:[^|]+', '', notes)
        notes = re.sub(r'Source:[^|]+\s*\|\s*', '', notes)
        notes = notes.strip()
        return source, notes

    return fallback_source, notes


def convert_csv(input_file, output_file=None):
    """Convert a single CSV from Deposits/Withdrawals to Amount format."""
    if output_file is None:
        output_file = input_file

    # Derive default source from filename
    filename = Path(input_file).name

    rows = []
    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)

        # Check if already in new format
        if 'Amount' in reader.fieldnames:
            print(f"✓ {filename} already in Amount format, skipping")
            return False

        # Check if in old format
        if 'Deposits' not in reader.fieldnames or 'Withdrawals' not in reader.fieldnames:
            print(f"⚠ {filename} has unexpected format, skipping")
            return False

        for row in reader:
            deposits = row.get('Deposits', '').strip()
            withdrawals = row.get('Withdrawals', '').strip()
            notes = row.get('Notes', '').strip()

            # Calculate Amount
            if deposits:
                amount = deposits
            elif withdrawals:
                amount = f"-{withdrawals}"
            else:
                amount = ""

            # Extract source
            source, cleaned_notes = extract_source_from_notes(notes, filename)

            # Build new row
            new_row = {
                'Date': row.get('Date', ''),
                'Description': row.get('Description', ''),
                'Amount': amount,
                'Balance': row.get('Balance', ''),
                'Type': row.get('Type', ''),
                'Category': row.get('Category', ''),
                'Source': source,
                'Notes': cleaned_notes
            }
            rows.append(new_row)

    # Write converted data
    fieldnames = ['Date', 'Description', 'Amount', 'Balance', 'Type', 'Category', 'Source', 'Notes']
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"✓ Converted {filename}: {len(rows)} rows")
    return True


def main():
    """Convert all CSVs in generated-files/ directories."""
    base_dir = Path(__file__).parent.parent

    directories = [
        base_dir / 'generated-files' / 'extracted',
        base_dir / 'generated-files' / 'merged'
    ]

    total_converted = 0
    total_skipped = 0

    for directory in directories:
        if not directory.exists():
            print(f"⚠ Directory not found: {directory}")
            continue

        print(f"\n📁 Processing {directory.name}/ directory...")
        csv_files = sorted(directory.glob('*.csv'))

        for csv_file in csv_files:
            converted = convert_csv(csv_file)
            if converted:
                total_converted += 1
            else:
                total_skipped += 1

    print(f"\n✅ Conversion complete!")
    print(f"   Converted: {total_converted} files")
    print(f"   Skipped: {total_skipped} files")


if __name__ == '__main__':
    main()
