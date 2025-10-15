# Popstand Inc - 2022 Wire Transfers Reconciliation

**Source:** Chase Bank statements (Popstand's account)
**Data:** Wire transfers FROM Popstand TO Kurt Braget
**Consolidated:** 2025-10-15

---

## Executive Summary

**Consolidated Wire Transfers (Chase statements):**
- Raw count: 65 wire transfers
- Raw total: $222,200.00

**After removing duplicates:**
- Clean count: 62 wire transfers
- Clean total: **$211,200.00**

**Comparison with Previous Summary:**
- Previous (from Wells Fargo deposits): $211,200.00 (62 wires)
- Current (from Chase outgoing): $211,200.00 (62 wires)
- **✅ Perfect Match!**

---

## Duplicate Transactions Identified

Three duplicate transactions were found and need to be excluded:

| Date | Amount | Location | Status |
|------|--------|----------|--------|
| 2022-05-06 | $5,000.00 | Appears in both May and December files | **DUPLICATE** |
| 2022-05-31 | $4,000.00 | Appears in both May and December files | **DUPLICATE** |
| 2022-07-19 | $2,000.00 | Already marked "(duplicate entry)" | **DUPLICATE** |

**Total duplicate amount:** $11,000.00

**Explanation:** The December CSV file incorrectly included May transactions (lines 2-3) before the December transactions. These were properly recorded in the May file and should not be double-counted.

---

## Monthly Breakdown (After Removing Duplicates)

| Month | Number of Wires | Total Amount |
|-------|----------------|--------------|
| January 2022 | 9 | $27,000.00 |
| February 2022 | 5 | $16,000.00 |
| March 2022 | 7 | $26,500.00 |
| April 2022 | 5 | $16,000.00 |
| May 2022 | 2 | $9,000.00 |
| June 2022 | 6 | $27,500.00 |
| July 2022 | 5 | $18,500.00 |
| August 2022 | 5 | $17,000.00 |
| September 2022 | 4 | $16,000.00 |
| October 2022 | 6 | $15,500.00 |
| November 2022 | 4 | $11,200.00 |
| December 2022 | 4 | $11,000.00 |
| **TOTAL** | **62 wires** | **$211,200.00** |

---

## Data Sources

### Original Files (Archived):
- `kurtis_braget_jan-april-2022.txt` (26 transactions)
- `kurtis_braget_may_2022.txt` (2 transactions)
- `kurtis_braget_june_2022.txt` (6 transactions)
- `kurtis-braget-payments-july-nov.txt` (25 transactions)
- `kurtis_braget_transactions-december.txt` (6 transactions, includes 2 May duplicates)

### Consolidated File:
- `2022_popstand_wire-transfers.csv` (65 transactions, 3 marked as duplicates)

**Date Range:** 2022-01-04 to 2022-12-23

---

## Transaction Details

All wire transfers follow this format:
```
Online Domestic Wire Transfer Via: Wells Fargo NA/121000248
A/C: Aba/123006800 Albany OR 97321-2226 US
Ben: Kurtis Braget Agoura Hills CA 91301 US
Ref: Disbursement/Bnf/Disbursement/Time/[HH:MM]
```

**Special transactions with different references:**
- 2022-06-08: "Lawyer Payment 1/5" - $5,000.00
- 2022-07-06: "Lawyer Fees" - $5,000.00

These are still distributions to Kurt, just with descriptive references.

---

## Reconciliation with Tax Documents

### K-1 Schedule (Form 1120-S)
**Line 16D - Property Distributions:** $164,567.00

### Wire Transfers (Chase/Wells Fargo)
**Total Wire Transfers:** $211,200.00

### Discrepancy
**Difference:** $46,633.00 (Bank exceeds K-1 by 28%)

**Possible Explanations:**
1. **Timing differences:** Some 2022 wires may be recorded on 2021 or 2023 K-1
2. **Loan/advance payments:** Some wires may represent loans rather than distributions
3. **Accounting method:** Cash basis (bank) vs accrual basis (tax return) timing
4. **Reallocation:** Wires may include amounts later reallocated between shareholders

**Action Required:** Accountant consultation needed to reconcile the $46,633 discrepancy.

---

## Data Quality

✅ **All transactions validated:**
- All dates populated (2022-01-04 to 2022-12-23)
- All amounts populated (range: $400 to $7,000)
- All properly formatted as Chase wire transfers
- Consistent Source field: "Chase Statement"

✅ **Duplicates identified and documented**

✅ **Matches previous Wells Fargo analysis** (after duplicate removal)

---

## Changes from Previous Summary

### What Changed:
1. **Source:** Now using Chase bank statements (Popstand's outgoing wires) instead of Wells Fargo (Kurt's incoming deposits)
2. **Consolidation:** Combined 5 separate monthly files into one CSV
3. **Duplicate detection:** Identified 3 duplicate entries totaling $11,000

### What Stayed the Same:
- Total amount: $211,200.00
- Transaction count: 62 wires
- Monthly breakdown: Identical
- Date range: Same

**Conclusion:** The Chase statement data confirms the Wells Fargo deposit data. Both sources show the same wire transfers, validating the accuracy of both datasets.

---

## Files

### Active Files:
- **Consolidated CSV:** `generated-files/extracted/popstand/2022_popstand_wire-transfers.csv`
- **This reconciliation:** `generated-files/extracted/popstand/2022_popstand_wire-transfers_reconciliation.md`

### Archived Files (Redundant):
- `generated-files/extracted/2022_popstand_income-summary.md` → Move to archive
- `generated-files/extracted/2022_popstand-chase_wire-transfers-reconciliation.md` → Move to archive

---

**Document Created:** 2025-10-15
**Created By:** Claude Code (Accounting Assistant)
**For:** Kurt Braget
**Tax Year:** 2022
