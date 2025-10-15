# Archive: 2025-10-14 Pre-Reextraction

## Reason for Archive

Wells Fargo 2022 checking account statements are being re-extracted using a formal, documented process to improve accuracy.

## Issue Identified

During analysis of the top 10 largest credits for 2022, a significant error was discovered:
- **Transaction:** Wire transfer to Zuber Lawler LLP (law firm) for $25,000 on 2022-04-25
- **Error:** Marked as POSITIVE (income/credit) when it should be NEGATIVE (expense/debit)
- **Impact:** Inflated income by $25,000 in top 10 analysis

This error indicated a systematic problem with the original extraction process, which was done manually without a formal procedure for determining transaction signs.

## Root Cause

Original extraction method:
- Manual/vision-based extraction directly from PDFs
- No documented process for handling Wells Fargo's two-section format:
  - "Deposits and Other Additions" (Credits)
  - "Withdrawals and Other Subtractions" (Debits)
- Wire transfers particularly problematic (can be incoming or outgoing)
- No validation checks for obvious errors

## Solution

Created comprehensive extraction process document: `docs/WELLS_FARGO_EXTRACTION_PROCESS.md`

Key improvements:
1. Clear rules for determining positive/negative amounts based on PDF section
2. Explicit handling of wire transfers (check which section they appear in)
3. Verification checklist for each extraction
4. Example transactions with correct formatting
5. Common error patterns to avoid

## Files Archived

### Wells Fargo Extracted Files (12 files)
- `2022-01_wells-fargo_checking.csv`
- `2022-02_wells-fargo_checking.csv`
- `2022-03_wells-fargo_checking.csv`
- `2022-04_wells-fargo_checking.csv` ⚠️ Contains known sign error
- `2022-05_wells-fargo_checking.csv`
- `2022-06_wells-fargo_checking.csv`
- `2022-07_wells-fargo_checking.csv`
- `2022-08_wells-fargo_checking.csv`
- `2022-09_wells-fargo_checking.csv`
- `2022-10_wells-fargo_checking.csv`
- `2022-11_wells-fargo_checking.csv`
- `2022-12_wells-fargo_checking.csv`

### Downstream Files (contain Wells Fargo data)
- `2022_all-transactions_merged_2025-10-12.csv` (from merged/)
- `2022_all-transactions_merged_2025-10-13.csv` (from merged/)
- `2022_deduped_2025-10-14.csv` (from merged-deduped/)

## Known Issues in Archived Files

**Confirmed Issues:**
- April 2022: Zuber Lawler LLP wire transfer (+$25,000 should be -$25,000)

**Potential Issues:**
- Other wire transfers may have similar sign errors
- Need to verify all months during re-extraction

## Re-extraction Plan

1. Archive all existing Wells Fargo CSVs and dependent files
2. Re-extract each month (Jan-Dec 2022) following new process
3. Human review and approval for each month
4. Regenerate merged and deduplicated files after all months complete

## Verification Method

For performance comparison after re-extraction:
1. Compare transaction counts (should match)
2. Compare specific transactions (descriptions should match)
3. Check for sign differences (focus on wire transfers, large amounts)
4. Verify ending balances match PDFs

---

**Archive Date:** 2025-10-14
**Archived By:** Automated process
**Related Document:** `docs/WELLS_FARGO_EXTRACTION_PROCESS.md`
**Tracking Document:** `docs/WELLS_FARGO_EXTRACTION_TRACKING.md`
