# Automatique Inc - 2023 Tax Year Research

**Prepared:** February 5, 2026
**Tax Year:** 2023 (Partial Year: May 7 - December 31)
**Entity Type:** C-Corporation (Delaware)
**EIN:** 38-4207516

---

## 1. Existing Files Inventory

### Corporate Documents (automatique-inc/)
| File | Purpose |
|------|---------|
| `COMPANY_PROFILE.md` | Company details extracted from Stripe Atlas docs |
| `PLAN.md` | Tax planning & documentation overview |
| `SCORP_VS_CCORP_ANALYSIS.md` | S-Corp vs C-Corp evaluation |
| `SCORP_VS_CCORP_SCENARIOS.md` | Detailed tax scenario modeling |
| `RAMI_AGREEMENT_NOTES.md` | Rami's $20k contribution & deal terms |
| `RAMI_PROFIT_SHARE_SCENARIOS.md` | Profit sharing calculations |
| `LOAN_AGREEMENT_RAMI_ELHAJ.txt` | Draft loan agreement for Rami's $20k |
| `stripe-atlas/` | 12 incorporation documents (bylaws, cert of inc, EIN, 83(b), etc.) |

### 2023 Extracted Data (automatique-inc/2023/)
| Directory | Files | Description |
|-----------|-------|-------------|
| `source-documents/wells-fargo/` | 12 PDFs | Monthly Wells Fargo statements (personal account with business expenses) |
| `source-documents/privacy-com/` | 1 CSV | Privacy.com statement for 2023 |
| `generated-files/extracted/wells-fargo/` | 12 CSVs | Extracted monthly transactions from Wells Fargo PDFs |
| `generated-files/extracted/privacy-com/` | 1 CSV | Extracted Automatique-specific Privacy.com transactions (5 LegalZoom charges) |
| `generated-files/extracted/amazon/` | 1 CSV | 2023 Amazon purchases with business/personal classification |

### Accountant Package (automatique-inc/expenses-for-accountant/)
| File | Description |
|------|-------------|
| `ACCOUNTANT_SUMMARY_JAN2026.txt` | Complete expense summary for 2023-2025 |
| `EMAIL_TO_BRANDON.txt` | Cover email for accountant |
| `kurt-personal-expenses/2023_BUSINESS_EXPENSES.txt` | Detailed 2023 expense breakdown |
| `mercury-corporate-expenses/` | 2024-2025 Mercury account expenses (no Mercury in 2023) |

---

## 2. 2023 Financial Summary

### Revenue: $0

Automatique Inc had **no revenue** in 2023. The company was incorporated May 7, 2023 and spent the remainder of the year in development.

### Expenses: $16,815.90

All 2023 expenses were paid by Kurt personally (no Mercury corporate account until 2024).

| Category | Amount | Details |
|----------|--------|---------|
| Incorporation | $500.00 | Stripe Atlas (Delaware C-Corp) |
| Contractor Payments | $10,000.00 | 5 Zelle payments to "Pablo" via Popstand (Jul-Sep 2023) |
| Software & Services | $6,254.42 | Privacy.com virtual card charges |
| Office Equipment | $61.48 | Amazon (3 items) |
| **Total** | **$16,815.90** | |

#### Software & Services Breakdown ($6,254.42)
- **Developer Tools & Hosting:** $2,411.12 (GitHub, Heroku, Sentry, Bitrise, QuickNode, GCloud, Wasabi)
- **AI/ML Tools:** $2,511.60 (ElevenLabs, Humane AI Pin, Midjourney, ChatGPT, OpenAI API, OpenRouter)
- **Domains & Marketing:** $1,206.42 (Google Domains, Twitter/X API, Mailchimp)
- **Legal & Business:** $125.28 (LegalZoom registered agent)

### Net Operating Loss (NOL): ($15,991)

Per the S-Corp vs C-Corp analysis, the 2023 NOL is approximately $15,991. The accountant summary rounds to $16,815.90 in expenses. The slight difference may be due to the Privacy.com LegalZoom charges ($125.28) being separately extracted.

---

## 3. Comparison with Popstand S-Corp (2022)

### Popstand Inc (S-Corp) - What Was Needed for Filing

Popstand was an established S-Corp with significant activity:

| Item | Popstand 2022 | Automatique 2023 |
|------|---------------|-------------------|
| **Entity Type** | S-Corp | C-Corp |
| **Tax Form** | Form 1120-S | Form 1120 |
| **Revenue** | $2,064,789 | $0 |
| **Net Income** | $381,772 | ($15,991) loss |
| **W-2 Wages** | $30,000 (Kurt) | $0 |
| **K-1 Issued** | Yes (2 shareholders) | N/A (C-Corp) |
| **Distributions** | $164,567 per shareholder | $0 |
| **State Filing** | CA Form 100S ($5,799 due) | CA Form 100 (minimum $800 franchise tax) |
| **Payroll** | Yes (officer compensation $60,000) | No |

### Documents Popstand Needed
1. **Form 1120-S** (federal S-Corp return)
2. **Schedule K-1** for each shareholder
3. **W-2** for employee-shareholders
4. **CA Form 100S** (state S-Corp return)
5. Bank statements showing wire transfers and payroll
6. Expense documentation

### Documents Automatique Needs (2023)
1. **Form 1120** (federal C-Corp return) - NOT 1120-S since it's a C-Corp
2. **CA Form 100** (state C-Corp return)
3. **Delaware Franchise Tax** return/payment
4. Expense documentation (already prepared in accountant package)
5. **No K-1s needed** (C-Corp doesn't issue K-1s)
6. **No W-2s needed** (no employees paid in 2023)

---

## 4. C-Corp with No Revenue - How It Works

### Filing Requirements

Even with $0 revenue and only losses, Automatique must file:

1. **Federal Form 1120** - Corporate income tax return
   - Report $0 revenue, $16,816 in expenses
   - Result: Net Operating Loss (NOL) of ~$15,991
   - No tax due (losses = no taxable income)

2. **California Form 100** - State corporate return
   - California imposes an **$800 minimum franchise tax** regardless of income
   - This is owed even for loss years
   - Due date: March 15, 2024 (for 2023 tax year)
   - **Late penalties apply** since this is being filed in 2026

3. **Delaware Franchise Tax**
   - Due March 1, 2024 (for 2023)
   - Minimum ~$400 under Authorized Shares Method
   - **Late penalties apply**

### NOL Carryforward Rules (C-Corp)

- The 2023 NOL (~$15,991) can be carried forward **indefinitely**
- Can offset up to **80%** of future taxable income (post-2017 TCJA rule)
- The NOL stays trapped at the corporate level (cannot pass through to Kurt's personal return)
- If the company later elects S-Corp status, this C-Corp NOL generally **cannot be used** against S-Corp pass-through income (it stays in a "suspended" state)

### Per the Existing Scenario Analysis

The SCORP_VS_CCORP_SCENARIOS.md already models this well:
- **2023 NOL:** ($15,991)
- **2024 NOL:** ($1,918)
- **Cumulative NOL:** $17,909
- These NOLs offset 2025 profits when the company becomes profitable
- Under C-Corp treatment, the NOL saves approximately $3,761 in corporate tax (21% x $17,909)
- Under S-Corp treatment, the same loss could save ~$8,059 personally (45% x $17,909) but requires a retroactive S-Corp election

---

## 5. Key Facts for 2023 Tax Filing

### Critical Dates
| Date | Event |
|------|-------|
| May 7, 2023 | Company incorporated in Delaware |
| May 10, 2023 | EIN received from IRS |
| Jul-Sep 2023 | Contractor payments to Pablo ($10,000) |
| March 1, 2024 | Delaware Franchise Tax due (for 2023) |
| March 15, 2024 | Federal Form 1120 due (for 2023) |
| April 15, 2024 | CA Form 100 due (for 2023) |

All filings are overdue. Late filing penalties will apply to any amounts owed (primarily the CA $800 minimum franchise tax and Delaware franchise tax).

### Filing as Partial Year
- 2023 is a **short tax year** (May 7 - Dec 31, approximately 8 months)
- The tax return should cover only this period
- Expenses before May 7, 2023 ($114.95 in Amazon pre-incorporation purchases) may qualify as **startup costs** under IRC Section 195 (question for accountant)

### Contractor Payment Concern
- $10,000 paid to "Pablo" via Zelle through Popstand
- Need to determine: Does Automatique need to file **Form 1099-NEC** for Pablo, or does Popstand handle this since payments went through them?
- This is flagged as a question for Brandon in the accountant summary

### Expense Reimbursement
- All $16,815.90 was paid by Kurt personally
- Per Brandon's guidance: a payable should be recorded in 2023, with IRS AFR interest added when reimbursed
- This creates a liability on Automatique's balance sheet

---

## 6. Documents Still Needed / To Collect

### Already Have
- [x] Wells Fargo statements (12 months, extracted)
- [x] Privacy.com statement (extracted, Automatique charges identified)
- [x] Amazon purchases (categorized business vs personal)
- [x] Stripe Atlas incorporation documents (12 PDFs)
- [x] Expense breakdown for accountant

### Still Need
- [ ] **Confirmation from accountant on filing approach** (C-Corp vs retroactive S-Corp)
- [ ] **Delaware Franchise Tax filing status** - Has this been filed/paid for 2023?
- [ ] **California Statement of Information** - Due within 90 days of incorporation (Aug 2023)
- [ ] **Pre-incorporation expense ruling** - Can the $114.95 be deducted?
- [ ] **1099-NEC determination** - Does Automatique or Popstand file for Pablo?
- [ ] **83(b) election confirmation** - Was the IRS 83(b) election accepted? (Filed per Stripe Atlas docs, but not yet confirmed)

---

## 7. Accountant-Ready Status

The 2023 data is **largely ready for the accountant**:

1. **Expense documentation is complete** - The `expenses-for-accountant/` package includes:
   - Full summary (`ACCOUNTANT_SUMMARY_JAN2026.txt`)
   - Detailed 2023 breakdown (`kurt-personal-expenses/2023_BUSINESS_EXPENSES.txt`)
   - Cover email (`EMAIL_TO_BRANDON.txt`)

2. **Source data is extracted** - Wells Fargo, Privacy.com, and Amazon CSVs are all in `2023/generated-files/extracted/`

3. **Outstanding questions are documented** - Reimbursement procedure, 1099 requirements, pre-incorporation expenses, and S-Corp election feasibility are all listed in the accountant summary

### What Automatique's 2023 Form 1120 Should Show

```
INCOME
  Gross receipts:                           $0

DEDUCTIONS
  Salaries and wages:                       $0
  Other deductions:                    $16,816
    - Contractor payments:             $10,000
    - Software & services:              $6,254
    - Incorporation costs:                $500
    - Office equipment:                    $61

TAXABLE INCOME:                       ($16,816)
TAX DUE:                                   $0
NET OPERATING LOSS:                   ~$15,991
```

---

## 8. Differences from Popstand S-Corp Pattern

Since Automatique is a C-Corp (not an S-Corp like Popstand), the filing process differs:

| Aspect | Popstand (S-Corp) | Automatique (C-Corp) |
|--------|-------------------|----------------------|
| Federal form | 1120-S | 1120 |
| Income taxation | Pass-through to shareholders | Taxed at corporate level (21%) |
| Losses | Pass through to reduce shareholders' personal taxes | Stay trapped in corporation as NOL |
| K-1s | Required for each shareholder | Not issued |
| State form | CA 100S | CA 100 |
| Minimum CA tax | $800 | $800 |
| Payroll required | Yes (reasonable compensation) | Only if employees are paid |
| Delaware franchise tax | N/A (Popstand was CA corp) | Required ($400+ annually) |

The key disadvantage for 2023: the $15,991 loss cannot reduce Kurt's personal taxes (unlike an S-Corp where it would pass through). This is the primary argument for a retroactive S-Corp election, which could save approximately $7,200 in personal taxes.

---

*This research report consolidates information from existing files in the automatique-inc/ directory and compares the Automatique C-Corp structure with the Popstand S-Corp pattern from 2022.*
