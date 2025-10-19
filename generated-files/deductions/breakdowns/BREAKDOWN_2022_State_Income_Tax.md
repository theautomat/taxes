# 2022 State Income Tax Deduction
**Schedule A, Line 5a: State and Local Income Taxes**
**State:** California
**Analysis Date:** 2025-10-18

---

## Overview

This document covers **California state income tax withheld** from your W-2 wages in 2022.

**Important:** This is a component of your Schedule A itemized deductions (Line 5a). See the master document: `BREAKDOWN_2022_Schedule_A_Itemized_Deductions.md`

---

## ⚠️ SALT Cap Limitation

**Your state income tax ALONE exceeds the $10,000 federal SALT cap.**

```
CA State Income Tax Withheld:  $25,600+
Federal SALT Cap:              $10,000
────────────────────────────────────────
Excess (non-deductible):       $15,600+
```

This means:
- **Federal:** Only $10,000 deductible (when combined with property tax)
- **California:** State income tax is NOT deductible on your state return (can't deduct state tax from state tax)

**See:** `BREAKDOWN_2022_SALT_Cap_Analysis.md` for detailed explanation of how the cap works.

---

## 2022 CA State Income Tax Withheld

**Total CA State Income Tax: $25,600 - $26,000** (estimated)

### NFT Genius W-2 Wages

**Employer:** NFT Genius
**CA State Income Tax Withheld:** $23,627.34

**Details:**
- 24 bi-monthly paychecks (Jan 15 - Dec 30, 2022)
- Salary increased from $120k to $240k on August 16, 2022
- Regular withholding throughout the year

**Source:** `generated-files/extracted/nft-genius/2022_nft-genius_gusto-paystubs-detailed.csv`

**Verification:**
```bash
grep "CA State Income Tax" generated-files/extracted/nft-genius/2022_nft-genius_gusto-paystubs-detailed.csv | \
  awk -F',' '{sum += $3} END {printf "%.2f\n", -sum}'
# Result: 23627.34
```

---

### Popstand W-2 Wages

**Employer:** Popstand
**CA State Income Tax Withheld:** ~$2,000 - $2,400 (estimated)

**Details:**
- 12 monthly payroll payments of $2,210.83
- Total wages: $26,530
- CA withholding estimated at ~7.5-9% rate

**Note:** Popstand also issued K-1 distributions (wire transfers), but those are NOT subject to withholding. Only W-2 wages have state tax withheld.

**Source:** `source-documents/Tax - Finance Documents/2022 Tax Info/Popstand/popstand-wages-summary.md`

---

## Total State Income Tax Withheld

**Combined Total:**
```
NFT Genius:    $23,627.34
Popstand:      ~$2,000-2,400
──────────────────────────
Total:         ~$25,600-26,000
```

---

## How to Report State Income Tax

### Federal (IRS)

**Schedule A (Form 1040), Line 5a:**
- State and local income taxes = **$25,600** (or your exact W-2 Box 17 total)
- This amount is combined with property tax (Line 5c) and limited to $10,000 total on Line 5e

**Where to Find This Number:**
- **W-2 Box 17:** State income tax withheld
- Add up Box 17 from all W-2 forms:
  - NFT Genius W-2: $23,627.34
  - Popstand W-2: ~$2,000-2,400

**Tax Impact (Federal):**
- You enter $25,600 on Line 5a
- Combined with property tax ($3,095) on Line 5c
- Total SALT (Line 5e): LIMITED TO $10,000
- Tax savings: $10,000 × 24% = ~$2,400

---

### California (Franchise Tax Board)

**State income tax is NOT deductible on your California return.**

Why? You can't deduct state taxes from state taxes (circular logic).

**California Schedule CA:**
- Remove the federal SALT cap (CA has no cap on property taxes)
- But state income tax still not deductible on state return

---

## SALT Cap Impact

**The Problem:**
Your state income tax ($25,600) ALONE exceeds the federal SALT cap ($10,000) by $15,600.

**What This Means:**
```
Line 5a (State income tax):        $25,600
Line 5c (Property tax):             $3,095
───────────────────────────────────────────
Subtotal (before cap):             $28,695

Line 5e (after SALT cap):          $10,000  ← CAPPED
───────────────────────────────────────────
Non-deductible amount:             $18,695
```

**Impact:**
- You paid $28,695 in state and local taxes
- IRS only allows $10,000 deduction
- You "lose" $18,695 in deductions due to the cap
- Property tax deduction provides no additional federal benefit (bucket already full)

**See:** `BREAKDOWN_2022_SALT_Cap_Analysis.md` for detailed explanation.

---

## Estimated State Tax Payments

**Did you make estimated tax payments in 2022?**

If you made quarterly estimated tax payments to California (beyond W-2 withholding), those also count toward Line 5a.

**To Add:**
- Q1 2022 estimated payment (paid April 15, 2022)
- Q2 2022 estimated payment (paid June 15, 2022)
- Q3 2022 estimated payment (paid September 15, 2022)
- Q4 2022 estimated payment (paid January 15, 2023 - for 2022 tax year)

**Where to Find:**
- Check bank statements for payments to "CA Franchise Tax Board" or "FTB"
- Check prior year tax return (2021) for estimated payment vouchers

**Note:** This analysis currently only includes W-2 withholding. If you made estimated payments, add those amounts to the total.

---

## Alternative: State Sales Tax Election

**Instead of deducting state income tax, you can elect to deduct state sales tax.**

**IRS Rules:**
- You can deduct EITHER state income tax OR state sales tax (not both)
- Most people deduct income tax because it's usually higher
- Sales tax election makes sense only in states with no income tax (e.g., Texas, Florida)

**Your Situation:**
- State income tax: $25,600+
- State sales tax: Likely ~$2,000-3,000 (rough estimate)
- **Decision:** Deduct income tax (much higher)

---

## Tax Forms Required

### What You Receive:
- **Form W-2** (from each employer)
  - Box 17: State income tax withheld
  - NFT Genius W-2: $23,627.34
  - Popstand W-2: ~$2,000-2,400

### What You File:
- **Schedule A (Form 1040)** - Itemized Deductions
  - Line 5a: State and local income taxes = **$25,600**
  - Attach W-2 forms to your tax return

---

## Summary

**2022 CA State Income Tax Withheld:** ~$25,600-26,000

**Federal Tax Impact:**
- Reported on Schedule A, Line 5a
- Combined with property tax, limited to $10,000 total
- Tax savings: $10,000 × 24% = ~$2,400 (if in 24% bracket)

**California Tax Impact:**
- Not deductible on CA return

**SALT Cap Reality:**
- You already exceeded the $10k cap from income tax alone
- Property tax provides no additional federal benefit

---

## Related Documents

- **Master Deduction Summary:** `BREAKDOWN_2022_Schedule_A_Itemized_Deductions.md`
- **SALT Cap Analysis:** `BREAKDOWN_2022_SALT_Cap_Analysis.md`
- **Property Tax:** `BREAKDOWN_2022_Property_Taxes.md`
- **NFT Genius Payroll:** `generated-files/extracted/nft-genius/2022_nft-genius_gusto-paystubs-detailed.csv`
- **Popstand Wages:** `source-documents/Tax - Finance Documents/2022 Tax Info/Popstand/popstand-wages-summary.md`

---

*Last Updated: 2025-10-18*
*Source: W-2 forms from NFT Genius and Popstand*
*Note: This is an analysis document. Consult a qualified tax professional for tax advice.*
