# Wells Fargo PDF Extraction Process

This document provides a step-by-step process for extracting transaction data from Wells Fargo bank statement PDFs using AI vision capabilities.

## Overview

Wells Fargo statements are monthly PDF documents containing checking account transactions. Each PDF must be carefully extracted to CSV format, ensuring accurate representation of deposits (credits) and withdrawals (debits).

## Source Document Location

**PDF Location:** `personal/2022/source-documents/Tax - Finance Documents/2022 Tax Info/Well Fargo Statements/`

**Naming Pattern:** `MMDDYY WellsFargo.pdf` (e.g., `043022 WellsFargo.pdf` for April 30, 2022)

## Output Format

**Destination:** `personal/2022/generated-files/extracted/YYYY-MM_wells-fargo_checking.csv`

**Standard CSV Schema:**
```csv
Date,Description,Amount,Balance,Type,Category,Source,Notes
```

**Column Specifications:**
- **Date**: YYYY-MM-DD format (convert from MM/DD/YYYY if needed)
- **Description**: Exact transaction description from statement
- **Amount**:
  - **NEGATIVE** for withdrawals, debits, expenses, payments OUT
  - **POSITIVE** for deposits, credits, income, payments IN
- **Balance**: Daily ending balance (when shown on statement)
- **Type**:
  - `Credit` for deposits/income (positive amounts)
  - `Debit` for withdrawals/expenses (negative amounts)
- **Category**: Leave empty (will be filled in later stages)
- **Source**: Original PDF filename (e.g., `043022 WellsFargo.pdf`)
- **Notes**: Leave empty unless clarification needed

## Wells Fargo Statement Structure

Wells Fargo statements typically have TWO separate sections:

### 1. Deposits and Other Additions (Credits Section)
- Wire transfers IN from clients/companies
- Payroll deposits (Gusto Pay, company payroll)
- Mobile deposits (checks)
- ACH credits
- Refunds and credits
- Interest payments
- **ALL amounts in this section should be POSITIVE in the CSV**

### 2. Withdrawals and Other Subtractions (Debits Section)
- Purchases (debit card transactions)
- Wire transfers OUT to vendors/services
- Wire transfer service charges
- ATM withdrawals
- Bill payments
- Recurring payments
- Checks
- ACH debits
- Account fees
- **ALL amounts in this section should be NEGATIVE in the CSV**

## Critical Extraction Rules

### Rule 1: Section Determines Sign
**The physical location in the PDF determines the sign, NOT the transaction description.**

- If transaction appears under "Deposits and Other Additions" → **POSITIVE amount**
- If transaction appears under "Withdrawals and Other Subtractions" → **NEGATIVE amount**

### Rule 2: Common Confusion Points

**Wire Transfers:**
- Wire transfers can be incoming (deposits) OR outgoing (payments)
- **INCOMING wire** (in Deposits section): `WT Fed - Jpmorgan Chase Ban - Popstand Inc` → POSITIVE
- **OUTGOING wire** (in Withdrawals section): `WT Fed - City National Bank - Zuber Lawler LLP` → NEGATIVE
- Wire service charges are ALWAYS negative (they're fees)

**Check if in doubt:**
- Law firms (Zuber Lawler LLP) = you're paying them → NEGATIVE
- Your own companies (Popstand Inc) = they're paying you → POSITIVE
- Vendors, service providers = you're paying them → NEGATIVE

### Rule 3: Amount Formatting
- Remove dollar signs and commas
- Use exactly 2 decimal places
- Include the negative sign for debits: `-25000.00` not `25000.00`

### Rule 4: Transaction Order
- Extract transactions in chronological order (date ascending)
- If multiple transactions on same date, preserve order from PDF

### Rule 5: Balance Column
- Include ending balance for the day when shown
- Typically appears at the end of a day's transactions
- Leave empty if not shown for that specific transaction

## Step-by-Step Extraction Process

### Before Starting
1. Open the Wells Fargo PDF
2. Identify the statement period (e.g., "March 1 - March 31, 2022")
3. Determine the output filename: `2022-03_wells-fargo_checking.csv`
4. Note the beginning and ending balance for verification

### During Extraction

1. **Locate the "Deposits and Other Additions" section**
   - Read each transaction carefully
   - For each transaction, create a CSV row with:
     - Date in YYYY-MM-DD format
     - Exact description
     - **POSITIVE amount**
     - Balance (if shown)
     - Type: `Credit`
     - Source: PDF filename

2. **Locate the "Withdrawals and Other Subtractions" section**
   - Read each transaction carefully
   - For each transaction, create a CSV row with:
     - Date in YYYY-MM-DD format
     - Exact description
     - **NEGATIVE amount** (add minus sign)
     - Balance (if shown)
     - Type: `Debit`
     - Source: PDF filename

3. **Sort all transactions by date**
   - Combine deposits and withdrawals
   - Sort chronologically (earliest to latest)
   - Maintain order within same-day transactions

4. **Write CSV file**
   - Include header row
   - One transaction per line
   - Proper CSV escaping for commas in descriptions

### After Extraction - Verification Checklist

Run these checks before submitting for review:

- [ ] **Balance verification**: Does the ending balance in CSV match the PDF?
- [ ] **Transaction count**: Count total transactions in PDF vs CSV
- [ ] **Date format**: All dates in YYYY-MM-DD format?
- [ ] **Sign check**:
  - All deposits (Credits) are positive?
  - All withdrawals (Debits) are negative?
  - Wire service charges are negative?
- [ ] **Description accuracy**: Spot-check 5-10 random descriptions
- [ ] **Source field**: All rows have correct PDF filename?
- [ ] **No empty amounts**: Every transaction has an amount value?

### Validation Queries

After creating the CSV, answer these questions:

1. **How many total transactions?** (should match PDF)
2. **What's the sum of all Credits (positive amounts)?**
3. **What's the sum of all Debits (negative amounts)?**
4. **What's the ending balance?** (should match PDF)
5. **Any wire transfers to law firms?** (should be NEGATIVE)
6. **Any wire transfers from Popstand/companies?** (should be POSITIVE)

## Common Errors to Avoid

### Error 1: Wrong Sign on Wire Transfers
❌ **Wrong:**
```csv
2022-04-25,WT Fed - City National Bank - Zuber Lawler LLP,25000.00,,,Credit,043022 WellsFargo.pdf,
```

✅ **Correct:**
```csv
2022-04-25,WT Fed - City National Bank - Zuber Lawler LLP,-25000.00,,,Debit,043022 WellsFargo.pdf,
```

### Error 2: Missing Negative Sign
All purchases, fees, and withdrawals MUST have negative amounts.

### Error 3: Wrong Date Format
❌ Wrong: `04/25/2022` or `4-25-22`
✅ Correct: `2022-04-25`

### Error 4: Inconsistent Source Field
Use the exact PDF filename for all transactions in that month.

## Example Transactions

### Deposits Section (Credits - Positive Amounts)
```csv
2022-04-04,WT Fed - Jpmorgan Chase Ban - Popstand Inc,3000.0,,Credit,,043022 WellsFargo.pdf,
2022-04-15,Gusto Pay 372877,5204.61,,Credit,,043022 WellsFargo.pdf,
2022-04-18,Mobile Deposit : Ref Number :718180041673,3850.0,,Credit,,043022 WellsFargo.pdf,
2022-04-29,Interest Payment,1.84,208931.41,Credit,,043022 WellsFargo.pdf,
```

### Withdrawals Section (Debits - Negative Amounts)
```csv
2022-04-01,Purchase - Uber Trip Help.Uber.Com CA,-46.84,,Debit,,043022 WellsFargo.pdf,
2022-04-04,Wire Trans Svc Charge,-15.0,,Debit,,043022 WellsFargo.pdf,
2022-04-04,Mortgage Serv CT Mtg Paymt 040122,-4479.2,,Debit,,043022 WellsFargo.pdf,
2022-04-25,WT Fed - City National Bank - Zuber Lawler LLP,-25000.0,,Debit,,043022 WellsFargo.pdf,
2022-04-27,ATM Withdrawal - 636 W Ventura St Fillmore CA,-1000.0,,Debit,,043022 WellsFargo.pdf,
```

## Monthly Extraction Workflow

For each month (January - December 2022):

1. **Pre-extraction**
   - Mark month as "In Progress" in `docs/WELLS_FARGO_EXTRACTION_TRACKING.md`
   - Open source PDF: `personal/2022/source-documents/Tax - Finance Documents/2022 Tax Info/Well Fargo Statements/MMDDYY WellsFargo.pdf`

2. **Extraction**
   - Use AI vision to read PDF
   - Follow all rules in this document
   - Generate CSV following standard schema
   - Run verification checklist

3. **Save Output**
   - Save to: `personal/2022/generated-files/extracted/YYYY-MM_wells-fargo_checking.csv`
   - Commit to git with message: `feat: Re-extract Wells Fargo YYYY-MM statement with improved accuracy`

4. **Human Review**
   - User reviews CSV against PDF
   - User checks critical transactions (wire transfers, large amounts)
   - User approves or requests corrections

5. **Completion**
   - Mark month as "✅ Done" in tracking document
   - Move to next month

## Tips for AI Assistants

- **Take your time** - accuracy is more important than speed
- **When in doubt about a sign, check the section header** - let the PDF structure guide you
- **Double-check wire transfers** - these are frequently large amounts and easy to mistake
- **Verify against balance** - if running balance is shown, verify your amounts make mathematical sense
- **Ask questions** - if a transaction is ambiguous, add a note and ask the user
- **Use vision carefully** - OCR errors can happen, verify amounts look reasonable

## Troubleshooting

**Q: The balance doesn't match at the end**
- Check for missing transactions
- Verify all signs are correct (positive/negative)
- Check for typos in amounts

**Q: Not sure if wire transfer is incoming or outgoing**
- Check which section of the PDF it appears in
- Law firms, vendors, services = outgoing (negative)
- Your companies, clients, customers = incoming (positive)

**Q: Transaction appears in both deposits AND withdrawals**
- This shouldn't happen - check the PDF carefully
- May be two separate transactions with similar descriptions
- Include both with appropriate signs

**Q: Description contains commas**
- Use proper CSV escaping (wrap in quotes if needed)
- Example: `"Purchase - Store, Inc. Los Angeles CA"`

## Success Criteria

An extraction is considered successful when:

1. ✅ All transactions present and accounted for
2. ✅ All amounts have correct sign (positive/negative)
3. ✅ Ending balance matches PDF
4. ✅ Transaction count matches PDF
5. ✅ Date format consistent (YYYY-MM-DD)
6. ✅ User approves after review
7. ✅ No obvious errors (like positive law firm payments)

---

## Revision History

- 2025-10-14: Initial version created after identifying sign errors in original extraction
