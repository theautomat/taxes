#!/usr/bin/env python3
"""
Deduplicate transactions from merged CSV file.

This script identifies and removes duplicate transactions that appear in both
Privacy.com statements and Wells Fargo bank statements. The same transaction
appears twice because Privacy.com records it on the charge date, while Wells
Fargo records it on the posting date (typically 1-3 days later).

See generated-files/merged-deduped/DEDUPLICATION_RULES.md for detailed rules.
"""

import csv
import sys
import logging
from datetime import datetime, timedelta
from pathlib import Path
from typing import List, Dict, Set, Tuple
from collections import defaultdict


class Transaction:
    """Represents a single transaction."""

    def __init__(self, row: Dict[str, str], row_number: int):
        self.row_number = row_number
        self.date_str = row['Date']
        self.date = datetime.strptime(row['Date'], '%Y-%m-%d')
        self.description = row['Description']
        self.amount = float(row['Amount']) if row['Amount'] else 0.0
        self.balance = row.get('Balance', '')
        self.type = row.get('Type', '')
        self.category = row.get('Category', '')
        self.source = row['Source']
        self.notes = row.get('Notes', '')
        self.original_row = row

    def is_privacy_com(self) -> bool:
        """Check if this transaction is from Privacy.com."""
        # Check both Source and Notes (for merged files)
        return ('Privacy.com Statement' in self.source or
                'Privacy.com Statement' in self.notes or
                'privacy-com_transactions' in self.notes)

    def is_wells_fargo_privacy(self) -> bool:
        """Check if this is a Wells Fargo transaction that came from Privacy.com."""
        # Must have Privacy.com markers in description
        has_pwp = 'Pwp' in self.description and 'Privacycom' in self.description

        # Check if from Wells Fargo (Source or Notes for merged files)
        from_wells_fargo = (
            'wells-fargo' in self.source.lower() or
            'wells-fargo' in self.notes.lower()
        )

        return has_pwp and from_wells_fargo

    def matches(self, other: 'Transaction', date_window_days: int = 5) -> bool:
        """
        Check if this transaction matches another (is a duplicate).

        Rules:
        1. Exact amount match
        2. Within date_window_days of each other
        3. One is Privacy.com, other is Wells Fargo Privacy.com transaction
        """
        # Must have exact same amount
        if abs(self.amount - other.amount) > 0.001:  # Float comparison tolerance
            return False

        # Must be within date window
        date_diff = abs((self.date - other.date).days)
        if date_diff > date_window_days:
            return False

        # One must be Privacy.com, other must be Wells Fargo
        if self.is_privacy_com() and other.is_wells_fargo_privacy():
            return True
        if self.is_wells_fargo_privacy() and other.is_privacy_com():
            return True

        return False

    def merge_info_from(self, other: 'Transaction') -> None:
        """
        Merge useful information from another transaction.
        Typically used to add Wells Fargo category to Privacy.com record.
        """
        # If Wells Fargo has a category and we don't, use it
        if other.category and not self.category:
            self.category = other.category

        # Add deduplication note
        dedup_note = f"Deduped with: {Path(other.source).stem} ({other.date_str})"
        if other.category:
            dedup_note += f" | WF Category: {other.category}"

        if self.notes:
            self.notes += f" | {dedup_note}"
        else:
            self.notes = dedup_note

    def to_dict(self) -> Dict[str, str]:
        """Convert back to dictionary for CSV output."""
        return {
            'Date': self.date_str,
            'Description': self.description,
            'Amount': str(self.amount) if self.amount != 0 else '',
            'Balance': self.balance,
            'Type': self.type,
            'Category': self.category,
            'Source': self.source,
            'Notes': self.notes
        }


class TransactionDeduplicator:
    """Main deduplication engine."""

    def __init__(self, date_window_days: int = 5, logger: logging.Logger = None):
        self.date_window_days = date_window_days
        self.transactions: List[Transaction] = []
        self.duplicates_found: Set[int] = set()  # Row numbers to remove
        self.match_count = 0
        self.ambiguous_matches: List[Tuple[Transaction, List[Transaction]]] = []
        self.duplicate_pairs: List[Tuple[Transaction, Transaction]] = []  # Track what was removed
        self.logger = logger or logging.getLogger(__name__)

    def load_transactions(self, csv_path: Path) -> None:
        """Load transactions from CSV file."""
        print(f"Loading transactions from: {csv_path}")
        self.logger.info(f"Loading transactions from: {csv_path}")

        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row_num, row in enumerate(reader, start=2):  # Start at 2 (header is row 1)
                if row['Date']:  # Skip empty rows
                    self.transactions.append(Transaction(row, row_num))

        print(f"Loaded {len(self.transactions)} transactions")
        self.logger.info(f"Loaded {len(self.transactions)} transactions")

    def find_duplicates(self) -> None:
        """Find and mark duplicate transactions."""
        print(f"\nSearching for duplicates (date window: ±{self.date_window_days} days)...")
        self.logger.info(f"\nSearching for duplicates (date window: ±{self.date_window_days} days)")
        self.logger.info("="*80)

        # Group transactions by amount for faster matching
        by_amount = defaultdict(list)
        for txn in self.transactions:
            by_amount[txn.amount].append(txn)

        # Find duplicates
        for amount, txns in by_amount.items():
            if len(txns) < 2:
                continue  # No possible duplicates

            # Check each Privacy.com transaction against Wells Fargo transactions
            privacy_txns = [t for t in txns if t.is_privacy_com()]
            wells_fargo_txns = [t for t in txns if t.is_wells_fargo_privacy()]

            for privacy_txn in privacy_txns:
                # Find matching Wells Fargo transactions
                matches = [wf for wf in wells_fargo_txns if privacy_txn.matches(wf)]

                if len(matches) == 1:
                    # Perfect match - deduplicate
                    wf_txn = matches[0]
                    date_diff = abs((privacy_txn.date - wf_txn.date).days)

                    # Log the duplicate match
                    self.logger.info(f"\n✓ DUPLICATE FOUND (#{self.match_count + 1})")
                    self.logger.info(f"  Amount: ${amount:.2f}")
                    self.logger.info(f"  Date difference: {date_diff} days")
                    self.logger.info(f"  KEPT (Privacy.com):")
                    self.logger.info(f"    Date: {privacy_txn.date_str}")
                    self.logger.info(f"    Description: {privacy_txn.description}")
                    self.logger.info(f"    Row: {privacy_txn.row_number}")
                    self.logger.info(f"  REMOVED (Wells Fargo):")
                    self.logger.info(f"    Date: {wf_txn.date_str}")
                    self.logger.info(f"    Description: {wf_txn.description}")
                    self.logger.info(f"    Row: {wf_txn.row_number}")

                    privacy_txn.merge_info_from(wf_txn)
                    self.duplicates_found.add(wf_txn.row_number)
                    self.duplicate_pairs.append((privacy_txn, wf_txn))
                    self.match_count += 1

                elif len(matches) > 1:
                    # Ambiguous - multiple possible matches
                    self.ambiguous_matches.append((privacy_txn, matches))
                    self.logger.warning(f"\n⚠️  AMBIGUOUS MATCH")
                    self.logger.warning(f"  Amount: ${amount:.2f}")
                    self.logger.warning(f"  Privacy.com ({privacy_txn.date_str}): {privacy_txn.description}")
                    for i, m in enumerate(matches, 1):
                        self.logger.warning(f"  Possible WF match {i} ({m.date_str}): {m.description}")

                    print(f"  ⚠️  Ambiguous match for {privacy_txn.date_str} ${amount:.2f}")
                    print(f"      Privacy.com: {privacy_txn.description}")
                    for m in matches:
                        print(f"      Wells Fargo: {m.description} ({m.date_str})")

        self.logger.info("\n" + "="*80)
        self.logger.info(f"DEDUPLICATION PASS COMPLETE")
        self.logger.info(f"Found {self.match_count} duplicate pairs")
        self.logger.info(f"Found {len(self.ambiguous_matches)} ambiguous matches (need review)")
        self.logger.info("="*80)

        print(f"\nFound {self.match_count} duplicate pairs")
        print(f"Found {len(self.ambiguous_matches)} ambiguous matches (need review)")

    def get_deduplicated_transactions(self) -> List[Transaction]:
        """Return list of transactions with duplicates removed."""
        return [t for t in self.transactions if t.row_number not in self.duplicates_found]

    def write_deduplicated_csv(self, output_path: Path) -> None:
        """Write deduplicated transactions to CSV file."""
        deduped = self.get_deduplicated_transactions()

        print(f"\nWriting deduplicated transactions to: {output_path}")

        with open(output_path, 'w', encoding='utf-8', newline='') as f:
            fieldnames = ['Date', 'Description', 'Amount', 'Balance', 'Type', 'Category', 'Source', 'Notes']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()

            for txn in deduped:
                writer.writerow(txn.to_dict())

        print(f"Wrote {len(deduped)} transactions (removed {len(self.duplicates_found)} duplicates)")

    def write_review_file(self, output_path: Path) -> None:
        """Write ambiguous matches to review file."""
        if not self.ambiguous_matches:
            print("\nNo ambiguous matches - no review file needed")
            return

        print(f"\nWriting ambiguous matches to: {output_path}")

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write("# Ambiguous Matches - Manual Review Required\n\n")
            f.write("These transactions had multiple possible duplicate matches.\n")
            f.write("Please review manually and update the deduplication rules if needed.\n\n")

            for i, (privacy_txn, matches) in enumerate(self.ambiguous_matches, 1):
                f.write(f"## Match Group {i}\n\n")
                f.write(f"**Privacy.com Transaction:**\n")
                f.write(f"- Date: {privacy_txn.date_str}\n")
                f.write(f"- Description: {privacy_txn.description}\n")
                f.write(f"- Amount: ${privacy_txn.amount:.2f}\n")
                f.write(f"- Source: {privacy_txn.source}\n\n")

                f.write(f"**Possible Wells Fargo Matches:**\n")
                for j, match in enumerate(matches, 1):
                    f.write(f"{j}. Date: {match.date_str} | {match.description} | ${match.amount:.2f}\n")
                f.write("\n---\n\n")

    def print_summary(self) -> None:
        """Print deduplication summary statistics."""
        deduped = self.get_deduplicated_transactions()

        original_count = len(self.transactions)
        final_count = len(deduped)
        removed_count = len(self.duplicates_found)

        # Calculate amount totals
        original_total = sum(t.amount for t in self.transactions)
        final_total = sum(t.amount for t in deduped)
        removed_total = original_total - final_total

        print("\n" + "="*60)
        print("DEDUPLICATION SUMMARY")
        print("="*60)
        print(f"Original transactions:    {original_count:>6}")
        print(f"Duplicates removed:       {removed_count:>6}")
        print(f"Final transactions:       {final_count:>6}")
        print(f"Ambiguous matches:        {len(self.ambiguous_matches):>6}")
        print()
        print(f"Original total amount:    ${original_total:>12,.2f}")
        print(f"Removed amount:           ${removed_total:>12,.2f}")
        print(f"Final total amount:       ${final_total:>12,.2f}")
        print("="*60)

        # Breakdown by source
        privacy_count = sum(1 for t in deduped if t.is_privacy_com())
        wells_fargo_count = sum(1 for t in deduped if 'wells-fargo' in t.source.lower())
        other_count = final_count - privacy_count - wells_fargo_count

        print("\nTransactions by Source:")
        print(f"  Privacy.com:            {privacy_count:>6}")
        print(f"  Wells Fargo:            {wells_fargo_count:>6}")
        print(f"  Other:                  {other_count:>6}")
        print("="*60)


def setup_logging(log_file: Path) -> logging.Logger:
    """Setup logging to file and console."""
    logger = logging.getLogger('deduplicator')
    logger.setLevel(logging.INFO)

    # Clear any existing handlers
    logger.handlers = []

    # File handler - detailed logs
    file_handler = logging.FileHandler(log_file, mode='w', encoding='utf-8')
    file_handler.setLevel(logging.INFO)
    file_formatter = logging.Formatter('%(message)s')
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)

    return logger


def main():
    """Main entry point."""
    # Setup paths
    repo_root = Path(__file__).parent.parent
    merged_dir = repo_root / 'generated-files' / 'merged'
    output_dir = repo_root / 'generated-files' / 'merged-deduped'

    # Find most recent merged file
    merged_files = sorted(merged_dir.glob('*_merged_*.csv'))
    if not merged_files:
        print("ERROR: No merged CSV files found in generated-files/merged/")
        sys.exit(1)

    input_file = merged_files[-1]

    # Generate output filenames with timestamp
    timestamp = datetime.now().strftime('%Y-%m-%d')
    output_file = output_dir / f'2022_deduped_{timestamp}.csv'
    review_file = output_dir / f'2022_deduped_{timestamp}_review.md'
    log_file = output_dir / f'2022_deduped_{timestamp}.log'

    # Create output directory
    output_dir.mkdir(parents=True, exist_ok=True)

    # Setup logging
    logger = setup_logging(log_file)

    # Log run metadata
    logger.info("="*80)
    logger.info("TRANSACTION DEDUPLICATION LOG")
    logger.info("="*80)
    logger.info(f"Run timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    logger.info(f"Input file: {input_file}")
    logger.info(f"Output file: {output_file}")
    logger.info(f"Review file: {review_file}")
    logger.info(f"Log file: {log_file}")
    logger.info("="*80)

    # Run deduplication
    print("="*60)
    print("TRANSACTION DEDUPLICATION")
    print("="*60)

    deduplicator = TransactionDeduplicator(date_window_days=5, logger=logger)
    deduplicator.load_transactions(input_file)
    deduplicator.find_duplicates()
    deduplicator.write_deduplicated_csv(output_file)
    deduplicator.write_review_file(review_file)
    deduplicator.print_summary()

    # Log summary
    logger.info("\n" + "="*80)
    logger.info("FINAL SUMMARY")
    logger.info("="*80)
    logger.info(f"Original transactions: {len(deduplicator.transactions)}")
    logger.info(f"Duplicates removed: {len(deduplicator.duplicates_found)}")
    logger.info(f"Final transactions: {len(deduplicator.get_deduplicated_transactions())}")
    logger.info(f"Ambiguous matches: {len(deduplicator.ambiguous_matches)}")
    logger.info("="*80)
    logger.info(f"\n✅ Deduplication complete!")
    logger.info(f"Log saved to: {log_file}")

    print(f"\n✅ Deduplication complete!")
    print(f"\nOutput files:")
    print(f"  - Deduplicated CSV: {output_file}")
    print(f"  - Log file: {log_file}")
    if deduplicator.ambiguous_matches:
        print(f"  - Review file: {review_file}")


if __name__ == '__main__':
    main()
