# S-Corp vs C-Corp Scenario Analysis

**DISCLAIMER:** This is a simulation with estimated numbers for planning purposes only. Actual tax liability may differ. Consult with Brandon before making decisions.

---

## Glossary

| Term | Meaning |
|------|---------|
| **NOL** | Net Operating Loss - when a business loses money, those losses can be "carried forward" to offset future profits and reduce taxes |
| **Pass-through** | S-Corp income "passes through" to shareholders' personal tax returns (no corporate tax) |
| **Reasonable compensation** | IRS requires S-Corp owner-employees to pay themselves a "reasonable" salary before taking distributions |
| **Basis** | Your investment in the company - affects taxes when you sell or take money out |

---

## Starting Position

| | Amount |
|---|--------|
| **2023 Net** | ($15,991) loss |
| **2024 Net** | ($1,918) loss |
| **2025 Net** | $73,251 profit |
| **NOL (losses to carry forward)** | $17,909 |
| **Cash in Bank** | $92,617 |
| **Rami's Loan to Company** | $20,000 |
| **Kurt's Personal Expenses Paid** | ~$17,000 (not a loan - paid for business) |

**Key Difference:**
- **Rami:** Gave the company a $20k loan (can be repaid tax-free)
- **Kurt:** Paid business expenses from personal funds (could be reimbursed as expense, or treated as capital contribution - need to ask Brandon)

---

## Assumptions

| Item | Rate | Notes |
|------|------|-------|
| C-Corp federal tax | 21% | Flat rate |
| Kurt's marginal rate | 37% federal | High income bracket |
| Kurt's CA state rate | 9.3% | CA resident |
| Kurt's combined rate | ~45% | Federal + state |
| Payroll taxes (employer) | 7.65% | Social Security + Medicare |
| Payroll taxes (employee) | 7.65% | Withheld from salary |
| Self-employment tax | 15.3% | For 1099 contractors |
| Late filing penalty | ~5%/month | Max 25% of tax owed |
| Late payment penalty | ~0.5%/month | Plus interest (~8%) |
| Estimated late penalties | ~$1,000 | For 2023+2024 filings |

---

## Scenario Summary Table

| # | Scenario | Corp Tax | Personal Tax | Total Tax | Kurt Gets | Rami Gets | Cash Left |
|---|----------|----------|--------------|-----------|-----------|-----------|-----------|
| 1 | C-Corp, repay Rami, Kurt $0 | $11,622 | $0 | ~$12,622 | $0 | $20,000 | $59,995 |
| 2 | C-Corp, repay Rami, pay Kurt salary | $11,622 | ~$8,500 | ~$21,622 | $11,610 | $20,000 | $36,875 |
| 3 | C-Corp, pay both as contractors | $4,222 | ~$22,760 | ~$26,982 | $9,080 | $9,080 | $48,395 |
| 4 | C-Corp, salary spread over 2026 | $11,622 | ~$12,834 | ~$25,456 | $23,166 | $20,000 | $21,241 |
| 5 | S-Corp 2025 (Kurt 100% owner) | $0 | ~$41,035 | ~$41,035 | $32,216 | $0 | $49,191 |
| 6 | S-Corp 2025 (Kurt 80%, Rami 20%) | $0 | ~$45,000 | ~$45,000 | $25,773 | $6,443 | $49,191 |

---

## Scenario 1: C-Corp, Repay Rami's Loan, Kurt Takes Nothing ⭐

**This is the simplest, lowest-tax option.**

### How it works:
1. File 2023, 2024, 2025 as C-Corp
2. Use NOL ($17,909) to offset 2025 profit
3. Pay corporate tax on remaining profit
4. Repay Rami's $20k loan (tax-free to him)
5. Kurt takes nothing - keeps cash in business for future

### Calculation:

```
2025 Gross Profit:                    $73,251
Less: NOL Carryforward               ($17,909)
─────────────────────────────────────────────
Taxable Income:                       $55,342

Corporate Tax (21%):                  $11,622
Late Filing Penalties (est):           $1,000
─────────────────────────────────────────────
Total Tax + Penalties:                $12,622

Starting Cash:                        $92,617
Less: Tax + Penalties                ($12,622)
Less: Repay Rami's Loan              ($20,000)
─────────────────────────────────────────────
Cash Remaining in Business:           $59,995
```

### What everyone gets:

| Person | Amount | Tax on It |
|--------|--------|-----------|
| Kurt | $0 | $0 |
| Rami | $20,000 | $0 (loan repayment) |
| Company | $59,995 cash | - |

### Why this works:
- Rami's $20k is a **loan repayment**, not income - no tax for him
- Kurt can pay himself later in 2026+ when it makes sense
- Company has $60k runway for operations
- **Total tax burden: ~$12,622** (lowest of all scenarios)

---

## Scenario 2: C-Corp, Repay Rami, Pay Kurt $20k Salary

### How it works:
1. File as C-Corp, use NOL
2. Pay corporate tax
3. Repay Rami's $20k loan (tax-free)
4. Pay Kurt $20k as W-2 salary (taxable)

### Calculation:

```
2025 Gross Profit:                    $73,251
Less: NOL Carryforward               ($17,909)
─────────────────────────────────────────────
Taxable Income:                       $55,342

Corporate Tax (21%):                  $11,622
Late Penalties:                        $1,000
─────────────────────────────────────────────
Total Corp Tax:                       $12,622

Starting Cash:                        $92,617
Less: Corp Tax + Penalties           ($12,622)
Less: Repay Rami Loan                ($20,000)
Less: Kurt Salary                    ($20,000)
Less: Employer Payroll Tax (7.65%)    ($1,530)
─────────────────────────────────────────────
Cash Remaining:                       $38,465
```

### What Kurt receives (net):

```
Gross salary:                         $20,000
Less: Employee payroll tax (7.65%)    ($1,530)
Less: Federal income tax (~25%)       ($5,000)
Less: CA state tax (~9.3%)            ($1,860)
─────────────────────────────────────────────
Kurt's net take-home:                 $11,610
```

### Summary:

| Person | Gross | Net After Tax |
|--------|-------|---------------|
| Kurt | $20,000 | $11,610 |
| Rami | $20,000 | $20,000 (tax-free) |
| Company | - | $38,465 cash |

**Total tax burden: ~$21,622**

---

## Scenario 3: C-Corp, Pay Both as 1099 Contractors

### How it works:
1. Don't repay Rami's loan - pay him as contractor instead
2. Pay Kurt as contractor too
3. Contractor payments reduce corporate taxable income
4. Both pay self-employment tax on their end

### Calculation:

```
2025 Gross Profit:                    $73,251
Less: Contractor payments            ($40,000)
Less: NOL Carryforward               ($17,909)
─────────────────────────────────────────────
Taxable Income:                       $15,342

Corporate Tax (21%):                   $3,222
Late penalties:                        $1,000
─────────────────────────────────────────────
Total Corp Tax:                        $4,222

Starting Cash:                        $92,617
Less: Corp Tax + Penalties            ($4,222)
Less: Pay Kurt                       ($20,000)
Less: Pay Rami                       ($20,000)
─────────────────────────────────────────────
Cash Remaining:                       $48,395
```

### What each person receives (net):

```
Gross 1099 payment:                   $20,000
Less: Self-employment tax (15.3%)     ($3,060)
Less: Federal income tax (~25%)       ($5,000)
Less: CA state tax (~9.3%)            ($1,860)
─────────────────────────────────────────────
Net take-home (each):                  $10,080
```

### Summary:

| Person | Gross | Net After Tax |
|--------|-------|---------------|
| Kurt | $20,000 | $10,080 |
| Rami | $20,000 | $10,080 |
| Company | - | $48,395 cash |

**Total tax burden: ~$26,982**

**Note:** In this scenario, Rami's $20k loan would still be owed - could repay later.

---

## Scenario 4: C-Corp, Repay Rami, Pay Kurt Salary Over 2026

### How it works:
1. File 2025 as C-Corp, pay corporate tax
2. Repay Rami's $20k loan immediately (tax-free)
3. Put Kurt on salary in 2026 at $3k/month
4. Spreading income keeps Kurt in lower tax bracket

### Calculation:

```
2025 Corp Tax + Penalties:            $12,622
Repay Rami Loan:                      $20,000
─────────────────────────────────────────────
Cash after 2025:                      $59,995

2026 Kurt Salary ($3k/month × 12):    $36,000
Employer Payroll Tax:                  $2,754
─────────────────────────────────────────────
Cash after 2026:                      $21,241
```

### What Kurt receives in 2026 (lower bracket):

```
Gross salary:                         $36,000
Less: Payroll (7.65%):                ($2,754)
Less: Federal (~22%):                 ($7,920)
Less: CA (~6%):                       ($2,160)
─────────────────────────────────────────────
Kurt's net take-home:                 $23,166
```

### Summary:

| Person | Gross | Net After Tax |
|--------|-------|---------------|
| Kurt (2026) | $36,000 | $23,166 |
| Rami | $20,000 | $20,000 (tax-free) |
| Company | - | $21,241 cash |

**Total tax burden: ~$25,456**

**Benefit:** Kurt gets more money by spreading income into lower brackets.

---

## Scenario 5: Elect S-Corp for 2025 (Kurt 100% Owner)

### How it works:
1. Elect S-Corp effective Jan 1, 2025
2. All profit passes through to Kurt's personal taxes
3. Must pay Kurt "reasonable compensation" (salary)
4. Can't use C-Corp NOL (trapped in prior C-Corp years)

### Problem: NOL is LOST
The $17,909 NOL from 2023-2024 stays in the C-Corp. It can't be used to offset S-Corp pass-through income. This makes S-Corp more expensive.

### Calculation:

```
2025 S-Corp Profit:                   $73,251
Less: Kurt's "reasonable salary"     ($40,000)
─────────────────────────────────────────────
Pass-through to Kurt:                 $33,251

Taxes:
  Tax on salary:                      $21,580
  Tax on pass-through:                $15,395
  Employer payroll:                    $3,060
  Late penalties:                      $1,000
─────────────────────────────────────────────
Total tax burden:                     $41,035
```

### Summary:

| Person | Amount | Net After Tax |
|--------|--------|---------------|
| Kurt | $73,251 (salary + pass-through) | ~$32,216 |
| Rami | $0 (no equity) | $0 |
| Company | - | $49,191 cash |

**Total tax burden: ~$41,035** (highest!)

**Note:** Rami's $20k loan still owed. He has no equity so gets no S-Corp distributions.

---

## Scenario 6: S-Corp with Rami as 20% Owner

### How it works:
1. Give Rami 20% equity (for his $20k contribution)
2. Elect S-Corp for 2025
3. Profit passes through: 80% Kurt, 20% Rami
4. Both must report income on personal taxes

### Calculation:

```
2025 S-Corp Profit:                   $73,251
Less: Kurt salary                    ($40,000)
─────────────────────────────────────────────
Pass-through:                         $33,251
  Kurt (80%):                         $26,601
  Rami (20%):                          $6,650

Kurt's total income: $40,000 + $26,601 = $66,601
Rami's total income: $6,650
```

### Summary:

| Person | Income | Estimated Tax | Net |
|--------|--------|---------------|-----|
| Kurt | $66,601 | ~$30,000 | ~$36,601 |
| Rami | $6,650 | ~$2,000 | ~$4,650 |
| Company | - | $49,191 cash | - |

**Total tax burden: ~$45,000**

**Problems:**
- Rami now owns 20% of company permanently
- Complicates future decisions
- Higher total tax than C-Corp options

---

## Comparison: All Scenarios

| # | Scenario | Total Tax | Kurt Net | Rami Net | Cash Left | Notes |
|---|----------|-----------|----------|----------|-----------|-------|
| **1** | **C-Corp, repay Rami, Kurt $0** | **$12,622** | **$0** | **$20,000** | **$59,995** | ⭐ Lowest tax |
| 2 | C-Corp, repay Rami, Kurt $20k | $21,622 | $11,610 | $20,000 | $38,465 | |
| 3 | C-Corp, 1099 contractors | $26,982 | $10,080 | $10,080 | $48,395 | Rami loan still owed |
| 4 | C-Corp, salary over 2026 | $25,456 | $23,166 | $20,000 | $21,241 | Best for Kurt long-term |
| 5 | S-Corp (Kurt 100%) | $41,035 | $32,216 | $0 | $49,191 | Loses NOL |
| 6 | S-Corp (Rami 20%) | $45,000 | $36,601 | $4,650 | $49,191 | Complicates ownership |

---

## Recommendation

### Best Option: Scenario 1 or 4

**If you want to minimize taxes now:**
→ **Scenario 1:** Pay corp tax, repay Rami's loan, keep cash. Total tax: ~$12,622

**If you want Kurt to get paid:**
→ **Scenario 4:** Pay corp tax, repay Rami, put Kurt on salary in 2026 at lower bracket. Total tax: ~$25,456, Kurt nets $23k+.

### Why NOT S-Corp:
- Loses the $17.9k NOL (can't use to offset income)
- Higher total tax burden
- Requires "reasonable compensation" complexity
- If Rami gets equity, complicates everything

### Rami's $20k:
- Keep it as a loan
- Repay it tax-free
- Don't convert to equity (keeps things simple)

### Kurt's $17k in personal expenses:
- Ask Brandon how to handle
- Could be expense reimbursement (deductible to corp)
- Could be capital contribution (no immediate deduction)
- Different from a loan since it was paying business expenses

---

## Questions for Brandon

1. **Kurt's $17k expenses:** Can these be reimbursed as business expenses? Or should they be treated as capital contribution?
2. **Rami's loan repayment:** Any documentation needed to prove it was a loan?
3. **Late penalties:** What's the actual amount for filing 2023/2024 late with no tax due?
4. **NOL carryforward:** Any limitations on using the $17.9k NOL?
5. **S-Corp election:** If we did want to elect S-Corp for 2026+, what's the process?

---

*Last updated: 2025-01-21*
*This is a planning document with estimates. Consult accountant before taking action.*
