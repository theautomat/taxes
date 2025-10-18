# Deduplication Rules for Merged Transactions

**Script Location**: `scripts/deduplicate_transactions.py`

This document describes the deduplication rules implemented in the actual script. It should be kept in sync with the script implementation.

## Problem Statement

The merged CSV file contains duplicates because the same transaction appears in multiple source documents:

1. **Privacy.com CSV** shows the transaction on the merchant charge date
2. **Wells Fargo statement** shows the same transaction when it posts to the bank (typically 1-3 days later)

For example:
- Privacy.com: `2022-01-01, Pwp AMZN Mktp US*8820R2183, -8.50`
- Wells Fargo: `2022-01-03, Pwp Amzn Mktp U Privacycom TN: 1412233, -8.50`

These are the SAME transaction, just recorded at different times by different systems.

## Workflow Context

Deduplication happens **after** all sources have been converted to standardized CSVs and merged:

1. **Extraction Phase**: Convert all source documents (PDFs, statements) to individual CSVs
   - Include ALL transactions, even duplicates
   - Maintain complete audit trail with Source field

2. **Merge Phase**: Combine all source CSVs into one file
   - Keep source reference for each transaction
   - Sort by date

3. **Deduplication Phase**: Identify and remove duplicates (THIS DOCUMENT)
   - Apply matching rules (described below)
   - Keep the most detailed record
   - Generate review file for ambiguous matches

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

## Deduplication Algorithm (Implementation)

The script uses a **two-pass approach** to handle both simple duplicates and recurring subscriptions:

### Pass 1: Simple 1:1 Matching (lines 162-201)

For each amount that appears more than once:
1. Separate Privacy.com transactions from Wells Fargo transactions
2. For each Privacy.com transaction, find matching Wells Fargo transactions
3. If **exactly 1 match** found:
   - Perfect 1:1 match → deduplicate immediately
   - Keep Privacy.com record, remove Wells Fargo record
   - Merge category info from Wells Fargo into Privacy.com notes
4. If **multiple matches** found:
   - Save as "ambiguous" for Pass 2 (subscription matching)

### Pass 2: Subscription Matching (lines 203-255)

For each amount with ambiguous matches:
1. Group all Privacy.com and Wells Fargo transactions for that amount
2. **Check if counts are equal**:
   - If YES (e.g., 12 Privacy.com, 12 Wells Fargo):
     - Sort both lists by date
     - Match sequentially (1st to 1st, 2nd to 2nd, etc.)
     - Only match if dates are within 5-day window
     - Handles recurring subscriptions automatically
   - If NO (unequal counts):
     - Flag as truly ambiguous → requires manual review
3. Generate review file for remaining ambiguous matches

### Output Generation

1. Write deduplicated CSV (duplicates removed)
2. Write log file (detailed matching decisions)
3. Write review file (ambiguous matches needing manual review)
4. Print summary statistics

**Simplified Flow**:
```
Load merged CSV
  ↓
Group by amount
  ↓
Pass 1: Match 1:1 duplicates → Dedupe
  ↓
Pass 2: Match equal-count subscription groups → Dedupe
  ↓
Remaining ambiguous matches → Review file
  ↓
Write deduplicated CSV + logs
```

## Source Field Format and Tracking

**Why Source Field Matters**: The Source field allows you to trace any transaction back to its original document for verification. This is critical for audits and debugging.

**Format**: Use the original source document filename exactly as it appears:

Examples:
- `013122 WellsFargo.pdf` - Original PDF filename
- `Privacy.com Statement 2022-01-01 - 2022-12-31.csv` - Privacy.com export
- `Chase_1234_January2022.pdf` - Credit card statement
- `2022-01_wells-fargo_checking.csv` - Standardized extracted CSV

**After Deduplication**: The kept record maintains its original source, but adds a note about which source was deduped:
```
Source: Privacy.com Statement 2022-01-01 - 2022-12-31.csv
Notes: Privacy.com card ending 5261 | Deduped with: 2022-01_wells-fargo_checking (2022-01-03) | WF Category: Shopping
```

## Output Format

The deduplicated CSV maintains all original columns:
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

The script automatically performs and reports several verification checks:

### Automated Checks (Built into Script)

1. **Count Check** (printed in summary):
   - Original transaction count
   - Duplicates removed count
   - Final transaction count
   - Ambiguous matches count (need manual review)

2. **Amount Check** (printed in summary):
   - Original total amount
   - Removed amount (duplicates)
   - Final total amount
   - Difference should equal removed duplicates

3. **Source Breakdown** (printed in summary):
   - Privacy.com transaction count
   - Wells Fargo transaction count
   - Other sources count

4. **Detailed Logs** (`2022_deduped_TIMESTAMP.log`):
   - Every duplicate match logged with dates, amounts, descriptions
   - Pass 1 and Pass 2 statistics
   - Warning messages for date gaps or unequal counts

### Manual Verification Steps

After running the script, review:

1. **Review File** (`2022_deduped_TIMESTAMP_review.md`):
   - Contains all ambiguous matches that couldn't be auto-resolved
   - Lists each Privacy.com transaction with its possible Wells Fargo matches
   - Requires manual decision on which (if any) should be deduped

2. **Spot Check**:
   - Randomly sample 10-20 deduped transactions
   - Verify the correct record was kept (Privacy.com over Wells Fargo)
   - Check that Notes field shows the dedup trail

3. **Edge Case Check**:
   - Search for same amount, same day transactions in final CSV
   - Verify they're legitimately different (not false negatives)
   - Check log file for how they were handled

4. **Subscription Verification**:
   - Pick a known recurring charge (e.g., Netflix)
   - Verify all 12 months were properly matched
   - Check that no subscription charges remain duplicated

## Manual Review Queue

The script generates a review file (`*_review.md`) for transactions that:
- **Have ambiguous matches**: Multiple possible duplicates with no clear 1:1 match
- **Unequal count groups**: Different number of Privacy.com vs Wells Fargo transactions (can't use subscription matching)
- **Large date gaps**: Dates beyond the 5-day window during subscription matching

**Review File Format**: Lists each ambiguous Privacy.com transaction with all its possible Wells Fargo matches, showing dates and descriptions side-by-side for manual decision-making.

## Important Safety Rules

⚠️ **Do NOT auto-delete duplicates without verification** - The script logs everything but requires you to review the output

⚠️ **When in doubt, keep both** - Better to have a duplicate than miss a real transaction (can be manually removed later)

⚠️ **Always check the review file** - Ambiguous matches need human judgment

⚠️ **Verify subscription matching** - Check that recurring charges were properly paired

⚠️ **Document decisions** - If you manually resolve ambiguous matches, document in Notes field

⚠️ **Preserve audit trail** - Never delete source documents or original CSVs

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

### Special Case: Recurring Subscriptions (IMPLEMENTED)

**Problem**: Multiple identical charges (same merchant, same amount) throughout the year.

Examples:
- Netflix: $15.49 monthly x 12 months
- Google Domains: $12.00 for multiple domain renewals
- QuickNode: $99.00 monthly subscription

**Implementation Status**: ✅ ACTIVE - Handled by Pass 2 of the deduplication script

**How It Works**: Sequential date matching for equal-count groups (Pass 2 in script)

When the script finds multiple matches for the same amount:
1. Group all Privacy.com and Wells Fargo transactions for that amount
2. Check if counts are equal (e.g., 12 Privacy.com, 12 Wells Fargo)
3. If equal: Sort both by date and match sequentially (closest dates)
4. If unequal: Flag as ambiguous for manual review

**Code Implementation** (lines 203-255 in `deduplicate_transactions.py`):
```python
# Pass 2: Subscription matching for equal-count groups
for amount, ambiguous_group in ambiguous_by_amount.items():
    all_privacy = [p for p, _ in ambiguous_group]
    all_wf = list({m for _, matches in ambiguous_group for m in matches})

    # Only apply subscription matching if counts are equal
    if len(all_privacy) == len(all_wf):
        privacy_sorted = sorted(all_privacy, key=lambda t: t.date)
        wf_sorted = sorted(all_wf, key=lambda t: t.date)

        # Match sequentially (closest dates)
        for p_txn, wf_txn in zip(privacy_sorted, wf_sorted):
            if date_diff <= self.date_window_days:
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
