# Deduplication Rules for Merged Transactions

## Problem Statement

The merged CSV file contains duplicates because the same transaction appears in multiple source documents:

1. **Privacy.com CSV** shows the transaction on the merchant charge date
2. **Wells Fargo statement** shows the same transaction when it posts to the bank (typically 1-3 days later)

For example:
- Privacy.com: `2022-01-01, Pwp AMZN Mktp US*8820R2183, -8.50`
- Wells Fargo: `2022-01-03, Pwp Amzn Mktp U Privacycom TN: 1412233, -8.50`

These are the SAME transaction, just recorded at different times by different systems.

## Deduplication Strategy

### Core Matching Rules

A transaction is considered a duplicate if it matches on:

1. **Amount Match (Required)**: Exact dollar and cents match
2. **Date Proximity (Required)**: Within 5 days of each other
3. **Source Relationship (Required)**: One source is Privacy.com, the other is Wells Fargo

### Why These Rules Work

**Amount Match**: The amount is the most reliable identifier. It's extremely unlikely that two different transactions have the exact same dollar and cents amount within a 5-day window.

**Date Proximity**: Privacy.com records the transaction date, while Wells Fargo records the posting date. Typically 1-3 days apart, but we use 5 days to be safe.

**Source Relationship**: We only dedupe between Privacy.com and Wells Fargo because:
- Privacy.com is the credit card processor
- Wells Fargo is the bank account where the card is paid from
- The relationship is: Privacy.com charge → posts to Wells Fargo

### Transaction Markers

Privacy.com transactions are easy to identify:
- Description starts with "Pwp " (Privacy.com prefix)
- Source field contains "Privacy.com Statement"

Wells Fargo Privacy.com transactions:
- Description contains "Pwp" and "Privacycom"
- Source field contains "wells-fargo"

## Deduplication Priority Rules

When duplicates are found, we keep the transaction with MORE information:

### Rule 1: Keep Privacy.com record over Wells Fargo record
**Reason**: Privacy.com has the actual merchant name and transaction details. Wells Fargo just shows "Pwp...Privacycom TN: xxxxx" which has less detail.

**Example:**
- **KEEP**: `Pwp AMAZON.COM*QM9EH6BI3, -13.12` (Privacy.com - has Amazon order ID)
- **REMOVE**: `Pwp Amazon.Com* Privacycom TN: 4454793, -13.12` (Wells Fargo - generic)

### Rule 2: Preserve the original transaction date
**Reason**: The Privacy.com date is the actual transaction date (when you made the purchase). Wells Fargo date is just the posting date (when the bank processed it).

### Rule 3: Combine useful information from both records
**Reason**: Privacy.com has merchant details, Wells Fargo sometimes has category information.

**Keep from Privacy.com record:**
- Date (actual transaction date)
- Description (detailed merchant info)
- Amount
- Source (Privacy.com statement)
- Notes (card ending number)

**Add from Wells Fargo record if present:**
- Category (Wells Fargo sometimes categorizes transactions)
- Add note that this was matched/deduped

## Edge Cases

### Edge Case 1: Multiple transactions same day, same amount
**Problem**: You might buy two identical items from the same merchant on the same day.

**Solution**: Check if the number of duplicates matches. If we find 2 Privacy.com records and 2 Wells Fargo records for the same amount on the same day, keep all 4 (2 unique transactions, properly deduped).

**Implementation**: Group by (date_window, amount) and count matches. If counts don't match, flag for manual review.

### Edge Case 2: Refunds and credits
**Problem**: A refund might post on a different day with different timing.

**Solution**: Same rules apply. A Privacy.com refund (+$) should match a Wells Fargo refund (+$) within 5 days.

### Edge Case 3: Partial refunds
**Problem**: You might get a partial refund with a different amount.

**Solution**: These won't match on amount, so they'll be kept as separate transactions. This is correct behavior - they ARE different transactions.

### Edge Case 4: Wire transfers same day, same amount
**Problem**: Two wires for the same amount on the same day (rare but possible).

**Solution**: Wire transfers don't involve Privacy.com, so they won't be deduped by these rules. They'll both be kept.

### Edge Case 5: Non-Privacy.com transactions
**Problem**: Regular Wells Fargo transactions (direct debits, wire transfers, etc.) shouldn't be touched.

**Solution**: Only dedupe if one source is Privacy.com. All other transactions are kept as-is.

## Deduplication Algorithm

```
1. Load all transactions from merged CSV
2. Sort by date
3. For each transaction:
   a. If source is Privacy.com:
      - Look for Wells Fargo transactions with:
        * Same amount
        * Date within ±5 days
        * Description contains "Pwp" and "Privacycom"
      - If match found:
        * Mark Wells Fargo record for removal
        * Optionally merge category from Wells Fargo into Privacy.com record
   b. Continue to next transaction
4. Remove all marked transactions
5. Output deduplicated CSV
```

## Output Format

The deduplicated CSV should maintain all original columns:
- Date (from Privacy.com record for deduped transactions)
- Description (from Privacy.com record)
- Amount
- Balance (if available)
- Type
- Category (merged if available from both sources)
- Source (from Privacy.com record, note the deduplication)
- Notes (combined from both records)

**Example deduped transaction:**
```csv
2022-01-01,Pwp AMZN Mktp US*8820R2183,-8.50,,Debit,Shopping,Privacy.com Statement 2022-01-01 - 2022-12-31.csv,"Privacy.com card ending 5261 | Deduped with: 2022-01_wells-fargo_checking.csv (2022-01-03) | WF Category: Shopping"
```

## Verification Strategy

After deduplication, verify the results:

1. **Count Check**:
   - Before: X transactions
   - After: Y transactions
   - Removed: X - Y duplicates
   - Expected: Privacy.com has ~650 transactions that should match Wells Fargo

2. **Amount Check**:
   - Sum all amounts before dedup
   - Sum all amounts after dedup
   - Difference should equal the sum of removed duplicates

3. **Spot Check**:
   - Manually review a sample of deduped transactions
   - Verify the correct record was kept
   - Verify no false positives (different transactions incorrectly deduped)

4. **Edge Case Check**:
   - Look for same amount, same day transactions
   - Verify they were handled correctly

## Manual Review Queue

The script should generate a review file for transactions that:
- Have ambiguous matches (multiple possible duplicates)
- Have unusual patterns (same amount, same day, but different merchants)
- Fall outside normal parameters (date gap > 5 days but otherwise matching)

## Source Priority Hierarchy (Future: 3-Way Deduplication)

### Current State (2-Way)
Privacy.com → Wells Fargo

### Future State (3-Way)
Amazon Order History → Privacy.com → Wells Fargo

### Why This Hierarchy?

**Priority 1: Amazon Order History (BEST)**
- Has actual product name and details
- Shows what was purchased (e.g., "Logitech MX Master 3 Mouse")
- Enables accurate business vs personal classification
- Contains order IDs for audit trail

**Priority 2: Privacy.com (GOOD)**
- Has merchant name and partial order info (e.g., "Pwp AMAZON.COM*QM9EH6BI3")
- Shows actual transaction date
- Better than Wells Fargo, but less detail than Amazon

**Priority 3: Wells Fargo (MINIMAL)**
- Generic description (e.g., "Pwp Amazon.Com* Privacycom TN: 4454793")
- Only shows posting date, not purchase date
- Least useful for categorization

### 3-Way Matching Algorithm (Future Implementation)

```
For each Amazon transaction:
  1. Look for Privacy.com match (same amount, within ±5 days)
     - If found: Mark Privacy.com as duplicate
  2. Look for Wells Fargo match (same amount, within ±5 days)
     - If found: Mark Wells Fargo as duplicate
  3. Keep Amazon record, note which records were matched

For remaining Privacy.com transactions (not matched to Amazon):
  1. Look for Wells Fargo match (current 2-way logic)
  2. Keep Privacy.com, remove Wells Fargo

Result: One transaction per actual purchase, with the most detailed record kept
```

### Source Detection Rules

**Amazon transactions:**
- Source field contains "amazon" (case-insensitive)
- Description has product details or order ID
- Amount matches Privacy.com/Wells Fargo charges

**Privacy.com transactions:**
- Description starts with "Pwp"
- Source contains "Privacy.com Statement"
- Has Privacy.com card number in notes

**Wells Fargo transactions:**
- Description contains "Privacycom"
- Source contains "wells-fargo"
- Is the final destination (bank posting)

### Special Case: Recurring Subscriptions (IMPORTANT)

**Problem**: Multiple identical charges (same merchant, same amount) throughout the year.

Examples:
- Netflix: $15.49 monthly x 12 months
- Google Domains: $12.00 for multiple domain renewals
- QuickNode: $99.00 monthly subscription

**Current Behavior**: Marked as "ambiguous" because algorithm can't determine which Privacy.com matches which Wells Fargo when there are multiple candidates.

**Solution**: Sequential date matching for equal-count groups
```python
# When counts match (e.g., 10 Privacy.com, 10 Wells Fargo)
# Sort both by date and match in order
privacy_sorted = sorted(privacy_txns, key=lambda t: t.date)
wf_sorted = sorted(wf_txns, key=lambda t: t.date)

for p_txn, wf_txn in zip(privacy_sorted, wf_sorted):
    if abs((p_txn.date - wf_txn.date).days) <= 5:
        match_and_dedupe(p_txn, wf_txn)
```

This handles recurring subscriptions automatically without manual review.

## Future Enhancements

1. **3-Way Deduplication**: Amazon → Privacy.com → Wells Fargo with source priority
2. **Subscription Detection**: Automatically identify and match recurring charges
3. **Machine Learning**: Train on manually reviewed duplicates to improve matching
4. **Fuzzy Description Matching**: Sometimes merchant names vary slightly
5. **Chase Account Integration**: If you add Chase statements, apply similar logic
6. **Cross-year Deduplication**: Handle transactions that span year boundaries
7. **Product-Level Detail**: Use Amazon product names for better expense categorization
