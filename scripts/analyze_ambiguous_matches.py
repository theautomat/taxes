#!/usr/bin/env python3
"""
Analyze ambiguous matches to understand why deduplication failed.
"""

import csv
from pathlib import Path
from collections import defaultdict
from datetime import datetime

def load_merged_transactions():
    """Load the merged CSV file."""
    repo_root = Path(__file__).parent.parent
    merged_file = repo_root / 'generated-files' / 'merged' / '2022_all-transactions_merged_2025-10-13.csv'

    transactions = []
    with open(merged_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['Date']:
                transactions.append(row)

    return transactions

def is_privacy_com(txn):
    """Check if transaction is from Privacy.com."""
    return 'Privacy.com Statement' in txn['Source'] or 'privacy-com_transactions' in txn.get('Notes', '')

def is_wells_fargo_privacy(txn):
    """Check if this is a Wells Fargo Privacy.com transaction."""
    return 'Pwp' in txn['Description'] and 'Privacycom' in txn['Description'] and 'wells-fargo' in txn.get('Notes', '').lower()

def analyze_by_amount():
    """Group ambiguous transactions by amount and analyze patterns."""
    transactions = load_merged_transactions()

    # Group by amount
    by_amount = defaultdict(list)
    for txn in transactions:
        if txn['Amount']:
            amount = float(txn['Amount'])
            if amount < 0:  # Only expenses
                by_amount[amount].append(txn)

    # Find amounts with multiple Privacy.com and multiple Wells Fargo
    ambiguous_amounts = {}

    for amount, txns in by_amount.items():
        privacy_txns = [t for t in txns if is_privacy_com(t)]
        wf_txns = [t for t in txns if is_wells_fargo_privacy(t)]

        if len(privacy_txns) >= 2 and len(wf_txns) >= 2:
            ambiguous_amounts[amount] = {
                'privacy_count': len(privacy_txns),
                'wf_count': len(wf_txns),
                'privacy_txns': privacy_txns[:5],  # First 5 examples
                'wf_txns': wf_txns[:5]
            }

    return ambiguous_amounts

def main():
    print("="*80)
    print("AMBIGUOUS MATCH ANALYSIS")
    print("="*80)
    print("\nAnalyzing transactions that couldn't be automatically matched...")
    print("\n")

    ambiguous = analyze_by_amount()

    # Sort by frequency (most common amounts first)
    sorted_ambiguous = sorted(ambiguous.items(),
                             key=lambda x: max(x[1]['privacy_count'], x[1]['wf_count']),
                             reverse=True)

    print(f"Found {len(sorted_ambiguous)} amounts with ambiguous matches\n")
    print("="*80)

    for amount, data in sorted_ambiguous[:20]:  # Top 20
        print(f"\n💰 Amount: ${abs(amount):.2f}")
        print(f"   Privacy.com transactions: {data['privacy_count']}")
        print(f"   Wells Fargo transactions: {data['wf_count']}")
        print(f"   Problem: {data['privacy_count']} Privacy.com → {data['wf_count']} Wells Fargo = Can't match 1:1")

        # Show some examples
        print("\n   Example Privacy.com transactions:")
        for i, txn in enumerate(data['privacy_txns'][:3], 1):
            print(f"     {i}. {txn['Date']} - {txn['Description'][:60]}")

        print("\n   Example Wells Fargo transactions:")
        for i, txn in enumerate(data['wf_txns'][:3], 1):
            print(f"     {i}. {txn['Date']} - {txn['Description'][:60]}")

        # Analysis
        if data['privacy_count'] == data['wf_count']:
            print(f"\n   ✓ GOOD: Equal counts! These SHOULD match, but dates/timing make it ambiguous")
            print(f"     → Solution: Use closest date matching within each batch")
        else:
            diff = abs(data['privacy_count'] - data['wf_count'])
            print(f"\n   ⚠️  BAD: Unequal counts (diff: {diff})")
            if data['privacy_count'] > data['wf_count']:
                print(f"     → {diff} Privacy.com transactions haven't posted to bank yet (or outside date range)")
            else:
                print(f"     → {diff} Wells Fargo transactions don't have Privacy.com match (or already matched)")

        print("-"*80)

if __name__ == '__main__':
    main()
