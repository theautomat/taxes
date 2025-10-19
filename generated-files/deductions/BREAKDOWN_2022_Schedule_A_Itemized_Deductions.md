# 2022 Schedule A: Itemized Deductions
**Form:** Schedule A (Form 1040)
**Tax Year:** 2022
**Taxpayer:** Kurt (filing status: TBD)
**Analysis Date:** 2025-10-18

---

## What is Schedule A?

**Schedule A** is the IRS form where you claim **Itemized Deductions** instead of taking the Standard Deduction.

**You must choose ONE:**
- **Standard Deduction:** $12,950 (single) or $25,900 (married filing jointly) for 2022
- **Itemized Deductions:** Add up all eligible expenses on Schedule A

**You should itemize if your total itemized deductions exceed the standard deduction.**

---

## Your 2022 Itemized Deductions Summary

| Line | Category | Amount | Notes |
|------|----------|--------|-------|
| **5** | **State & Local Taxes (SALT)** | **$10,000** | **CAPPED** (see SALT analysis) |
| 5a | State income tax | $25,600+ | Limited by cap |
| 5c | Property tax | $3,095 | Limited by cap |
| 5e | Total SALT (after cap) | $10,000 | Maximum allowed |
| **8a** | **Mortgage Interest** | **$20,347** | Acquisition debt |
| **Other** | Charitable contributions, etc. | TBD | (if any) |
| **17** | **TOTAL ITEMIZED DEDUCTIONS** | **~$30,347+** | (SALT + Mortgage + Other) |

**Conclusion:** Your itemized deductions (~$30,347+) far exceed the standard deduction ($12,950 single / $25,900 MFJ), so **you should definitely itemize**.

**Tax Savings vs. Standard Deduction:**
- Extra deductions: ~$17,397+ (if single) or ~$4,447+ (if MFJ)
- Tax savings: ~$4,175+ federal (at 24% bracket)

---

## SALT Cap Impact (The Confusing Part)

**What is SALT?**
- SALT = State And Local Taxes
- It's NOT a deduction name, it's just IRS shorthand for "Line 5 on Schedule A"
- Includes: state income tax + property tax + local taxes

**The $10,000 Cap:**
```
What you paid:
  CA State Income Tax:     $25,600+
  Property Tax:             $3,095
  ─────────────────────────────────
  Total SALT paid:         $28,695+

What IRS allows (Schedule A Line 5e):
  Federal SALT deduction:  $10,000  ← CAPPED HERE
  ─────────────────────────────────
  Amount you can't deduct: $18,695+  ← Wasted
```

**Why This Matters:**
- You already exceeded the $10k SALT cap from state income tax alone
- Property tax provides **zero additional federal benefit** (bucket already full)
- See detailed analysis: `breakdowns/BREAKDOWN_2022_SALT_Cap_Analysis.md`

---

## Line-by-Line Breakdown

### Line 5: State and Local Taxes (SALT)

**Line 5a: State and Local Income Taxes**
- CA state income tax withheld: **$25,600+**
  - NFT Genius: $23,627.34
  - Popstand: ~$2,000-2,400
- **Details:** See `breakdowns/BREAKDOWN_2022_State_Income_Tax.md`

**Line 5c: Real Estate Taxes**
- Property tax paid (662 Mountain View): **$3,095.19**
- **Details:** See `breakdowns/BREAKDOWN_2022_Property_Taxes.md`

**Line 5e: Total State and Local Taxes**
- Calculated: $25,600 + $3,095 = $28,695+
- **Allowed (after cap): $10,000** ← YOU ENTER THIS ON YOUR TAX RETURN

**Federal Impact:**
- Deduction: $10,000
- Tax savings: ~$2,400 (at 24% bracket)

**California Impact:**
- No SALT cap on CA return
- You can deduct full $3,095 property tax (state income tax not deductible on state return)
- Tax savings: ~$288 (at 9.3% bracket)

---

### Line 8a: Home Mortgage Interest

**Mortgage Interest Paid (Form 1098 Box 1):**
- Total interest: $20,410.43
- After $750k loan limitation: **$20,347.09**
- Non-deductible portion: $63.34

**Details:** See `breakdowns/BREAKDOWN_2022_Mortgage_Interest.md`

**Tax Savings:**
- Federal: $20,347 × 24% = ~$4,883
- California: $20,347 × 9.3% = ~$1,892
- **Total: ~$6,775**

---

### Other Itemized Deductions (If Any)

**Line 10-15: Gifts to Charity**
- TBD (if you made charitable contributions)

**Line 16: Other Deductions**
- TBD (casualty losses, gambling losses, etc.)

---

## How to File Schedule A

### Federal (IRS)

**Step 1: Complete Schedule A**
1. Enter state income tax on Line 5a: $25,600
2. Enter property tax on Line 5c: $3,095
3. Calculate Line 5e (limited to $10,000): Enter $10,000
4. Enter mortgage interest on Line 8a: $20,347
5. Add other deductions (charitable, etc.) if any
6. Calculate Line 17: Total itemized deductions (~$30,347+)

**Step 2: Attach to Form 1040**
- Transfer Line 17 total to Form 1040 Schedule A line
- This reduces your taxable income

### California (Franchise Tax Board)

**Schedule CA (540) - California Adjustments**
- Remove the federal SALT cap limitation
- California allows full SALT deduction (no $10k cap)
- Adjust Line 5 to show full state and property taxes

**California SALT Deduction:**
- Property tax: $3,095 (full amount)
- State income tax: NOT deductible on state return (can't deduct state tax from state tax)

---

## Tax Forms Required

### What You Receive:
- **Form 1098** - Mortgage Interest Statement (from PHH Mortgage)
  - Box 1: Mortgage interest = $20,410.43
  - Box 10: Property taxes = $3,095.19
- **W-2 Forms** - Wage statements (from NFT Genius, Popstand)
  - Box 17: State income tax withheld

### What You File:
- **Form 1040** - U.S. Individual Income Tax Return
- **Schedule A** - Itemized Deductions (this document)
- **Schedule CA (540)** - California adjustments (if filing CA return)

---

## Standard Deduction vs. Itemized Comparison

**2022 Standard Deduction:**
- Single: $12,950
- Married Filing Jointly: $25,900
- Head of Household: $19,400

**Your Itemized Deductions:**
- SALT: $10,000
- Mortgage Interest: $20,347
- Other: TBD
- **Total: ~$30,347+**

**Decision:**
- **Single:** Itemize saves ~$17,397 more deductions = ~$4,175 tax savings
- **Married Filing Jointly:** Itemize saves ~$4,447 more deductions = ~$1,067 tax savings

**Recommendation:** Itemize unless you're married filing jointly with no other deductions

---

## Component Documents

Detailed breakdowns for each line item:

1. **State Income Tax (Line 5a):** `breakdowns/BREAKDOWN_2022_State_Income_Tax.md`
2. **Property Tax (Line 5c):** `breakdowns/BREAKDOWN_2022_Property_Taxes.md`
3. **SALT Cap Analysis:** `breakdowns/BREAKDOWN_2022_SALT_Cap_Analysis.md`
4. **Mortgage Interest (Line 8a):** `breakdowns/BREAKDOWN_2022_Mortgage_Interest.md`

---

## Summary

**Name of Deduction:** Itemized Deductions (Schedule A)
**Form:** Schedule A (Form 1040)
**Total Deduction Amount:** ~$30,347+

**Key Components:**
1. SALT (capped at $10k) - mostly from state income tax
2. Mortgage interest ($20,347) - fully deductible

**Tax Impact:**
- Federal savings: ~$7,283 (at 24% bracket)
- California savings: ~$2,180
- **Total estimated savings: ~$9,463**

---

*Last Updated: 2025-10-18*
*Note: This is an analysis document. Consult a qualified tax professional for tax advice.*
