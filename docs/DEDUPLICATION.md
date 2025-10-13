# Transaction Deduplication Strategy

## Overview

This document outlines the strategy for identifying and removing duplicate transactions across multiple financial data sources. Deduplication happens **after** all sources have been tabulated into their own CSVs.

## Workflow

1. **Collection Phase** (Current)
   - Convert all source documents (PDFs, statements) to individual CSVs
   - Include ALL transactions, even if duplicates exist
   - Maintain complete audit trail for each source
   - **Always include Source field** with original filename

2. **Consolidation Phase** (Later)
   - Combine all source CSVs into a master transaction list
   - Keep source reference for each transaction

3. **Deduplication Phase** (Later)
   - Identify likely duplicates using matching rules
   - Review and confirm duplicates
   - Create final deduplicated CSV

## Duplicate Detection Rules

### Primary Match: Date + Amount
**Rule:** If two transactions have the same date AND same amount, they are likely duplicates.

**Example:**
```
Source: privacy-com-january.pdf
Date: 2022-01-03, Amount: -9.03, Description: "Dnh*Godaddy"

Source: 013122 WellsFargo.pdf
Date: 2022-01-03, Amount: -9.03, Description: "Pwp Dnh*Godaddy Privacycom TN: 2863985"
```
These are the same transaction - Privacy.com virtual card charged by Wells Fargo.

### Secondary Indicators
Additional clues that help confirm duplicates:

1. **Merchant name appears in both descriptions**
   - "Godaddy" in both examples above

2. **Privacy.com indicators**
   - Wells Fargo transactions starting with "Pwp" are Privacy.com
   - Look for matching non-Privacy.com source with same merchant

3. **Date tolerance** (edge cases)
   - Some transactions may post 1 day apart
   - Consider ±1 day window for amount matches

## Known Duplicate Patterns

### Privacy.com Transactions
- Privacy.com statement shows: Merchant charge
- Wells Fargo shows: "Pwp [Merchant]" charge
- **Action:** Keep one, note which source in final CSV

### Wire Transfers
- Sending bank shows: Wire out + fee
- Receiving bank shows: Wire in
- **Action:** Both are real transactions for different accounts
- **NOT duplicates** if tracking multiple accounts

### Credit Card Payments
- Bank account shows: Payment to credit card
- Credit card shows: Payment received
- **Action:** Keep bank account side only (payment is the expense, not receipt)

## Tools for Deduplication

### Excel/Google Sheets Method
1. Import all CSVs into one sheet
2. Source column already included
3. Sort by Date, then Amount
4. Use COUNTIFS to find matching Date+Amount pairs
5. Manually review flagged duplicates

### Airtable Method
1. Import all transactions
2. Create formula field: `Date & Amount` (concatenated)
3. Use Airtable's duplicate detection
4. Group by duplicate field
5. Review and mark for deletion

### Python/Script Method (Future)
```python
# Pseudocode for deduplication
duplicates = transactions.groupby(['Date', 'Amount']).filter(lambda x: len(x) > 1)
# Review and confirm before removing
```

## Source Field Format

**Always use the original source document filename:**

Examples:
- `013122 WellsFargo.pdf` - Original PDF filename
- `privacy-com-jan-2022.csv` - Original export filename
- `Chase_1234_January2022.pdf` - Credit card statement

**Why:** If you find a funky transaction, you can trace it back to the exact source document to verify the details.

## Final Output

### Deduplicated CSV Format
```csv
Date,Description,Amount,Source,Business_Personal,Category,Deductible,Notes
2022-01-03,Dnh*Godaddy,-9.03,013122 WellsFargo.pdf,Business,Services,Yes,Domain registration
```

## Important Notes

⚠️ **Do NOT auto-delete duplicates** - Always review manually first

⚠️ **When in doubt, keep both** - Better to have a duplicate than miss a real transaction

⚠️ **Document decisions** - Note why you kept/removed transactions in the Notes field

⚠️ **Always track source** - Every transaction must reference its source document
