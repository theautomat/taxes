#!/usr/bin/env python3
"""
Convert Privacy.com transaction CSV to standardized format.

Input: source-documents/Privacy.com Transactions/Privacy.com Statement 2022-01-01 - 2022-12-31.csv
Output: generated-files/extracted/2022_privacy-com_transactions.csv

This script converts Privacy.com transactions to match our standard CSV format:
Date, Description, Amount, Balance, Type, Category, Source, Notes
"""

import csv
from datetime import datetime
import os

# Get the project root directory (parent of scripts/)
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_dir)

# Define paths
input_file = os.path.join(project_root, "source-documents/Privacy.com Transactions/Privacy.com Statement 2022-01-01 - 2022-12-31.csv")
output_file = os.path.join(project_root, "generated-files", "extracted", "2022_privacy-com_transactions.csv")

print(f"Converting Privacy.com transactions...")
print(f"Input:  {input_file}")
print(f"Output: {output_file}")
print()

transaction_count = 0
refund_count = 0

with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
    reader = csv.DictReader(infile)
    writer = csv.writer(outfile)

    # Write header matching our standard format
    writer.writerow(['Date', 'Description', 'Amount', 'Balance', 'Type', 'Category', 'Source', 'Notes'])

    for row in reader:
        transaction_count += 1

        # Parse the timestamp to get just the date
        timestamp = row['transaction-timestamp']
        date = datetime.fromisoformat(timestamp.replace('Z', '+00:00')).strftime('%Y-%m-%d')

        # Description from descriptor field - add "Pwp" prefix to match Wells Fargo format
        description = f"Pwp {row['descriptor']}"

        # Amount - check if it's a SALE (withdrawal/negative) or REFUND (deposit/positive)
        amount_value = row['amount-usd']
        trans_type = row['type']

        if trans_type == 'SALE':
            amount = f"-{amount_value}"  # Negative for expenses
            type_col = 'Debit'
        elif trans_type == 'REFUND':
            amount = amount_value  # Positive for income/refunds
            type_col = 'Credit'
            refund_count += 1
        else:
            # Unknown type, treat as sale
            amount = f"-{amount_value}"
            type_col = 'Debit'

        # Balance column empty (not provided by Privacy.com)
        balance = ''

        # Category - leave empty for now, can be categorized later
        category = ''

        # Source - the original statement filename
        source = "Privacy.com Statement 2022-01-01 - 2022-12-31.csv"

        # Notes - include card last 4
        notes = f"Privacy.com card ending {row['card-last-four']}"

        writer.writerow([date, description, amount, balance, type_col, category, source, notes])

print(f"✅ Successfully converted {transaction_count} transactions")
print(f"   - Sales (withdrawals): {transaction_count - refund_count}")
print(f"   - Refunds (deposits): {refund_count}")
print(f"   - Output saved to: {output_file}")
