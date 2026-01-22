# S-Corp vs C-Corp Scenario Analysis

**DISCLAIMER:** This is a simulation with estimated numbers for planning purposes only. Actual tax liability may differ. Consult with Brandon before making decisions.

---

## Starting Position

| | Amount |
|---|--------|
| **2023 Net** | ($15,991) |
| **2024 Net** | ($1,918) |
| **2025 Net** | $73,251 |
| **Cumulative NOL** | $17,909 |
| **Cash in Bank** | $92,617 |
| **Rami's Contribution** | $20,000 (undocumented) |

**Goal:** Pay Kurt and Rami each $20,000 ($40,000 total)

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
| Late filing penalty | ~5%/month | Max 25% of tax owed |
| Late payment penalty | ~0.5%/month | Plus interest (~8%) |
| Estimated 2023 late penalty | ~$500 | On $0 tax (minimum fees) |
| Estimated 2024 late penalty | ~$500 | On $0 tax (minimum fees) |

---

## Scenario 1: Stay C-Corp, Pay Corporate Tax, Distribute Later

### How it works:
1. File 2023, 2024, 2025 as C-Corp
2. Use NOL to offset 2025 income
3. Pay corporate tax on remaining profit
4. Keep money in corp, pay salaries over time in 2026+

### Calculation:

```
2025 Gross Profit:                    $73,251
Less: NOL Carryforward                ($17,909)
─────────────────────────────────────────────
Taxable Income:                       $55,342

Corporate Tax (21%):                  $11,622
Late Filing Penalties (est):           $1,000
─────────────────────────────────────────────
Total Tax + Penalties:                $12,622

Cash Before Tax:                      $92,617
Less: Tax + Penalties                ($12,622)
─────────────────────────────────────────────
Cash Remaining:                       $79,995
```

### Then pay Kurt & Rami $20k each as salary in 2026:

```
Salaries to pay:                      $40,000
Employer payroll tax (7.65%):          $3,060
─────────────────────────────────────────────
Total cost to company:                $43,060

Cash after salaries:                  $36,935
```

### What Kurt & Rami receive (each):

```
Gross salary:                         $20,000
Less: Employee payroll tax (7.65%)    ($1,530)
Less: Federal income tax (~25%)       ($5,000)
Less: CA state tax (~9.3%)            ($1,860)
─────────────────────────────────────────────
Net take-home (each):                 $11,610
```

### Scenario 1 Summary:

| | Amount |
|---|--------|
| Corporate tax paid | $11,622 |
| Penalties | $1,000 |
| Kurt receives (net) | $11,610 |
| Rami receives (net) | $11,610 |
| Cash left in company | $36,935 |
| **Total tax burden** | **~$29,682** |

---

## Scenario 2: Elect S-Corp for 2025, Pass-Through Income

### How it works:
1. File 2023, 2024 as C-Corp (losses stay in corp)
2. Elect S-Corp effective Jan 1, 2025
3. 2025 profit passes through to Kurt's personal return
4. Pay "reasonable compensation" as salary, rest as distribution

**Problem:** C-Corp NOL doesn't transfer to S-Corp. The $17,909 NOL stays trapped in the C-Corp and can't offset S-Corp pass-through income.

### Calculation (assuming 100% Kurt ownership):

```
2025 S-Corp Profit:                   $73,251
Less: Kurt's "reasonable salary"     ($40,000)  (example)
─────────────────────────────────────────────
Pass-through to Kurt:                 $33,251

Kurt's Tax on Pass-Through:
  Federal (37%):                      $12,303
  CA State (9.3%):                     $3,092
─────────────────────────────────────────────
Tax on pass-through:                  $15,395

Kurt's Tax on Salary ($40k):
  Federal (37%):                      $14,800
  CA State (9.3%):                     $3,720
  Employee payroll (7.65%):            $3,060
─────────────────────────────────────────────
Tax on salary:                        $21,580

Employer payroll tax:                  $3,060
Late penalties (est):                  $1,000
─────────────────────────────────────────────
Total taxes (S-Corp scenario):        $41,035
```

### What about Rami?

If Rami has no equity, he can only be paid as:
- **Employee** (salary + payroll taxes)
- **Contractor** (1099, he pays self-employment tax)

If Rami has equity (say 20%), his share passes through to HIS taxes.

### Scenario 2 Summary (Kurt 100% owner):

| | Amount |
|---|--------|
| Kurt's salary | $40,000 gross |
| Kurt's pass-through income | $33,251 |
| Total tax burden | ~$41,035 |
| Kurt's net after all taxes | ~$32,216 |
| Rami receives | $0 (no equity) |
| Cash left in company | $49,191 |

**Note:** S-Corp requires "reasonable compensation" - you can't pay $0 salary and take all distributions.

---

## Scenario 3: Stay C-Corp, Pay Kurt & Rami as Contractors

### How it works:
1. File as C-Corp
2. Pay Kurt and Rami as 1099 contractors (no payroll tax for company)
3. They pay self-employment tax on their end

### Calculation:

```
2025 Gross Profit:                    $73,251
Less: Contractor payments            ($40,000)
Less: NOL Carryforward               ($17,909)
─────────────────────────────────────────────
Taxable Income:                       $15,342

Corporate Tax (21%):                   $3,222
Late penalties (est):                  $1,000
─────────────────────────────────────────────
Total corporate tax:                   $4,222

Cash remaining:                       $48,395
```

### What Kurt & Rami receive (each, as contractor):

```
Gross 1099 payment:                   $20,000
Less: Self-employment tax (15.3%)     ($3,060)
Less: Federal income tax (~30%)       ($6,000)
Less: CA state tax (~9.3%)            ($1,860)
─────────────────────────────────────────────
Net take-home (each):                  $9,080
```

### Scenario 3 Summary:

| | Amount |
|---|--------|
| Corporate tax paid | $3,222 |
| Penalties | $1,000 |
| Kurt receives (net) | $9,080 |
| Rami receives (net) | $9,080 |
| Cash left in company | $48,395 |
| **Total tax burden** | **~$26,982** |

---

## Scenario 4: Don't Pay Out Now, Salary Over Time

### How it works:
1. File as C-Corp, pay corporate tax
2. Keep all money in company
3. Pay Kurt (and Rami if employee) reasonable salaries in 2026-2027
4. Spread out personal income to lower tax brackets

### Calculation:

```
2025 Profit after NOL:                $55,342
Corporate Tax (21%):                  $11,622
Late penalties:                        $1,000
─────────────────────────────────────────────
Cash remaining:                       $79,995
```

### Pay $3,000/month salary to Kurt in 2026:

```
Annual salary:                        $36,000
Employer payroll (7.65%):              $2,754
─────────────────────────────────────────────
Cost to company:                      $38,754

Cash after 1 year:                    $41,241
```

### Kurt's take-home (lower bracket):

```
Gross salary:                         $36,000
Less: Payroll (7.65%):                ($2,754)
Less: Federal (~22%):                 ($7,920)
Less: CA (~6%):                       ($2,160)
─────────────────────────────────────────────
Net take-home:                        $23,166
```

### Scenario 4 Summary:

| | Amount |
|---|--------|
| Corporate tax paid | $11,622 |
| Kurt receives (2026) | $23,166 |
| Rami receives | $0 (or separate arrangement) |
| Cash left in company | $41,241 |
| **Benefit:** Lower personal tax bracket |

---

## Scenario Comparison

| Scenario | Corp Tax | Personal Tax | Total Tax | Kurt Net | Rami Net | Cash Left |
|----------|----------|--------------|-----------|----------|----------|-----------|
| **1. C-Corp, salary later** | $12,622 | $17,060 | $29,682 | $11,610 | $11,610 | $36,935 |
| **2. S-Corp 2025** | $0 | $41,035 | $41,035 | $32,216 | $0* | $49,191 |
| **3. C-Corp, 1099 contractors** | $4,222 | $22,760 | $26,982 | $9,080 | $9,080 | $48,395 |
| **4. C-Corp, salary over time** | $12,622 | $12,834 | $25,456 | $23,166 | TBD | $41,241 |

*Rami would need equity to receive S-Corp distributions

---

## Payment Method Options

### Option A: W-2 Salary
- Company pays employer payroll tax (7.65%)
- Employee pays employee payroll tax (7.65%)
- Most "legitimate" for ongoing relationship
- Required for S-Corp shareholders who work in business

### Option B: 1099 Contractor
- No employer payroll tax
- Contractor pays 15.3% self-employment tax
- Good for one-time or project-based payments
- Less paperwork for company

### Option C: Distributions (S-Corp or C-Corp dividends)
- **S-Corp:** No payroll tax on distributions (but must pay reasonable salary first)
- **C-Corp:** Dividends are double-taxed (corp tax + personal dividend tax)
- **C-Corp qualified dividends:** 15-20% personal rate

### Option D: Shareholder Loan Repayment
- If Kurt/Rami have loans to company, repayment is not income
- Tax-free way to get money out (up to loan amount)
- Kurt has ~$17k in expenses he paid personally - could be structured as loan

---

## Rami's $20k - How It Affects Things

### If treated as LOAN:
- Company owes Rami $20k
- Repayment is NOT taxable to Rami
- Rami could get his $20k back tax-free
- Then any additional payments would be taxable (salary/contractor)

### If treated as EQUITY (say 20% ownership):
- Rami owns 20% of company
- S-Corp: 20% of profit passes through to Rami's taxes
- C-Corp: 20% of dividends go to Rami
- Complicates future decisions

### Recommendation:
**Treat as LOAN** - Cleaner, lets Rami get his $20k back tax-free, doesn't complicate ownership.

---

## Kurt's $17k Personal Expenses

Kurt paid ~$17k of business expenses personally (2023-2025).

### Option 1: Shareholder Loan
- Company owes Kurt $17k
- Reimburse tax-free (loan repayment)
- Document with promissory note

### Option 2: Capital Contribution
- Kurt contributed $17k to company
- Increases his basis
- No immediate tax benefit
- Helps if company is sold later

### Recommendation:
**Treat as LOAN** - Can reimburse Kurt tax-free.

---

## Recommended Approach

Based on the scenarios, here's a practical path:

### 1. File 2023 & 2024 as C-Corp
- Both years had losses, no tax due
- Pay late filing penalties (~$500-1000)
- NOL of $17,909 carries forward

### 2. File 2025 as C-Corp
- Use NOL to reduce taxable income: $73,251 - $17,909 = $55,342
- Pay corporate tax: ~$11,622
- Pay late filing penalty: ~$500

### 3. Document Kurt & Rami loans
- Kurt: $17,000 (personal expenses paid)
- Rami: $20,000 (capital contribution → recharacterize as loan)

### 4. Reimburse loans (tax-free)
- Pay Kurt $17,000
- Pay Rami $20,000
- Cash remaining: $92,617 - $12,122 - $37,000 = $43,495

### 5. Pay salaries in 2026
- Put Kurt on payroll at reasonable rate ($4-5k/month)
- Rami as contractor for specific projects
- Spread income over time for lower tax brackets

### Result:
- Kurt gets $17k tax-free (loan repayment) + salary income
- Rami gets $20k tax-free (loan repayment)
- Company keeps ~$43k for operations
- Lower overall tax burden by spreading income

---

## Questions for Brandon

1. Can we recharacterize Rami's $20k as a loan retroactively?
2. Can Kurt's personal expenses be documented as a shareholder loan now?
3. What's the actual late filing penalty for a C-Corp with no tax due?
4. Is the NOL carryforward straightforward, or are there limitations?
5. What's considered "reasonable compensation" if we elect S-Corp?

---

*Last updated: 2025-01-21*
*This is a planning document with estimates. Consult accountant before taking action.*
