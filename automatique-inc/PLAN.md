# Automatique Inc - Tax Planning & Documentation

## Overview

| Field | Value |
|-------|-------|
| **Legal Name** | Automatique, Inc. |
| **EIN** | 38-4207516 |
| **Structure** | C-Corporation (Delaware) |
| **Incorporated** | May 7, 2023 |
| **Banking** | Mercury |
| **Registered Agent** | Legalinc Corporate Services, Inc. |
| **Principal Address** | 662 Mountain View Street, Fillmore, CA 93015 |

**Tax Years to Address:**
- **2023** - Partial year (May 7 - Dec 31) - ~8 months of operation
- **2024** - Full year
- **2025** - Current year (partial)

**Ownership (as of 2/7/2024):**
- **Kurt Braget:** 8,500,000 shares (85% of authorized) - formally documented
- **Rami:** ~$20,000 startup capital contribution - **NOT DOCUMENTED** (needs formalization)

**Full company profile:** See `generated-files/COMPANY_PROFILE.md`

---

## Why We're Doing This

1. **Overdue payments** - Contractors and founders need to be paid (rent, bills, etc.)
2. **Avoid falling further behind** - Business has been operating but taxes not filed
3. **The business made money** - Need to properly account for income and structure distributions

---

## Key Questions to Resolve

### Business Structure
- [ ] **C-Corp vs S-Corp** - Stripe Atlas defaulted to C-Corp, but S-Corp may be better for pass-through taxation
- [ ] **Can we retroactively elect S-Corp?** - Since we haven't filed yet, ask accountant Brandon if we can file Form 2553 retroactively
- [ ] **What's the deadline for S-Corp election?** - Typically 2 months 15 days into tax year, but late election relief exists

### Tax Implications
- [ ] **C-Corp scenario** - Corporate tax on profits, then personal tax on distributions (double taxation)
- [ ] **S-Corp scenario** - Pass-through to shareholders, single level of tax, but requires "reasonable salary" for owner-employees
- [ ] **Calculate both scenarios** - Once we have income/expense numbers, model tax liability both ways

### Payments to Founders/Contractors
- [ ] **How to pay Kurt and Rami** - W-2 wages vs distributions vs combination
- [ ] **Contractor payments** - Need 1099s for any payments over $600
- [ ] **Backpay considerations** - How to handle payments owed from prior periods

---

## Source Documents Needed

### From Stripe Atlas
- [ ] Certificate of Incorporation
- [ ] Bylaws
- [ ] EIN confirmation letter
- [ ] Stock certificates / Cap table
- [ ] Any annual reports or filings

### From Mercury
- [ ] 2024 bank statements (all months)
- [ ] 2025 bank statements (all months through current)
- [ ] Transaction exports (CSV)
- [ ] Any 1099s issued by Mercury

### From Privacy.com
- [ ] 2024 Privacy.com statement (CSV export preferred)
- [ ] 2025 Privacy.com statement (CSV export preferred)
- [ ] Identify which cards/transactions are Automatique-related vs personal

**Note:** Privacy.com transactions will also appear in Wells Fargo when they post. We'll use the same deduplication strategy from 2022 (Privacy.com record preferred, match within 5-day window by amount).

### From Personal Records (Kurt)
- [ ] Wells Fargo transactions related to Automatique expenses
- [ ] Any contractor payment records
- [ ] Outgoing wires for business expenses
- [ ] Receipts for business expenses paid personally

### From Other Sources
- [ ] Any client invoices or contracts (for income verification)
- [ ] Contractor agreements
- [ ] Any revenue from Stripe (if applicable)

---

## Financial Tracking Plan

### Income (2024 + 2025)
| Source | 2024 | 2025 | Notes |
|--------|------|------|-------|
| Client payments (Auto Routing) | $14,600 | $0 | Feb $2,500 + Apr $12,100 |
| Capital contribution (Rami wire) | $20,000 | $0 | Jun 14, 2024 - NOT REVENUE |
| **Total Revenue** | **$14,600** | **$0** | Excludes Rami's capital |

### Expenses (2024 + 2025)
| Category | 2024 | 2025 | Notes |
|----------|------|------|-------|
| George (contractor) | $10,601.06 | $0 | International wire payments |
| Exchange fees | $80.90 | $0 | Wire transfer fees |
| Maxima | $2,500.00 | $0 | ACH payment (unknown) |
| PARO MARKETPLACE | $3,449.60 | $0 | ACH pull (unknown) |
| Bitrise Limited | $840.00 | $210.00 | CI/CD service |
| OpenAI | $360.00 | $200.00 | AI API |
| Heroku | $259.60 | $118.48 | Hosting |
| Notion | $242.00 | $44.00 | Productivity |
| Google Workspace | $72.00 | $24.00 | Email/docs |
| Google Cloud | $2.13 | $0.54 | Cloud services |
| Slack | $12.41 | $42.29 | Communication |
| Whimsical | $0 | $12.00 | Design tool |
| **Total Expenses** | **$15,857.41** | **$651.31** | |

### Net Profit (UPDATED)
| Year | Revenue | Expenses | Net Profit | Notes |
|------|---------|----------|------------|-------|
| 2024 | $14,600 | $15,857.41 | **-$1,257.41** | Operating loss |
| 2025 (Jan) | $0 | $651.31 | -$651.31 | YTD |

**Important Notes:**
- Rami's $20,000 wire is capital contribution, not revenue
- George contractor payments (~$10,600) may require 1099 filing
- Operating at a loss in 2024 despite appearances (Rami's capital masked it)

---

## Tax Scenario Comparison

### Scenario A: C-Corp (Current Structure)
```
Corporate Level:
  Net Profit: $___
  Federal Corporate Tax (21%): $___
  State Tax (CA ~8.84%): $___
  After-Tax Profit: $___

Personal Level (if distributed as dividends):
  Qualified Dividends to Kurt: $___
  Qualified Dividends to Rami: $___
  Tax on Dividends (~20% federal + 13.3% CA): $___

Total Tax Burden: $___
```

### Scenario B: S-Corp (If Restructured)
```
Pass-Through Income:
  Net Profit: $___
  Kurt's Share (___%): $___
  Rami's Share (___%): $___

Reasonable Salary Requirement:
  Kurt's W-2 Wages: $___
  Rami's W-2 Wages: $___
  Payroll Taxes on Wages: $___

Remaining Distributions (no payroll tax):
  Kurt's Distributions: $___
  Rami's Distributions: $___

Personal Tax on Pass-Through:
  Federal (~35%): $___
  CA (~9.3%): $___

Total Tax Burden: $___
```

### Comparison
| Metric | C-Corp | S-Corp | Difference |
|--------|--------|--------|------------|
| Total Tax | $__ | $__ | $__ |
| Cash to Kurt | $__ | $__ | $__ |
| Cash to Rami | $__ | $__ | $__ |

---

## Action Plan

### Phase 1: Document Gathering
1. [ ] Download all Mercury statements (2024 + 2025)
2. [ ] Export Mercury transactions to CSV
3. [ ] Get Stripe Atlas incorporation documents
4. [ ] Download Privacy.com statements (2024 + 2025 CSV exports)
5. [ ] Identify Wells Fargo transactions related to Automatique
6. [ ] Gather any contractor payment records

### Phase 2: Financial Extraction
1. [ ] Extract all income transactions from Mercury
2. [ ] Extract all expense transactions from Mercury
3. [ ] Extract Automatique-related expenses from personal Wells Fargo
4. [ ] Categorize all transactions
5. [ ] Create summary totals by year

### Phase 3: Structure Decision
1. [ ] Calculate taxes under C-Corp scenario
2. [ ] Calculate taxes under S-Corp scenario
3. [ ] Consult with Brandon (accountant) on:
   - Feasibility of retroactive S-Corp election
   - Best approach for founder compensation
   - Any compliance issues to address
4. [ ] Make decision on business structure

### Phase 4: Filing & Payments
1. [ ] Prepare corporate tax returns (1120 or 1120-S)
2. [ ] Calculate founder distributions/wages
3. [ ] Set up payroll if needed (for W-2 wages)
4. [ ] Issue any required 1099s to contractors
5. [ ] File taxes and make payments

---

## Notes & Decisions Log

### 2025-01-19 (Later)
- Extracted all 12 Stripe Atlas documents
- Created `generated-files/COMPANY_PROFILE.md` with company details
- Key finding: Company incorporated 5/7/2023 - so there IS a 2023 partial tax year
- Key finding: Rami's $20k contribution not documented - needs formalization
- Next step: Process Mercury statements for transaction data

### 2025-01-19
- Started planning document
- No Automatique source documents found in project yet
- Need to download from Mercury and Stripe Atlas

---

## Accountant Communication

**Accountant:** Brandon
**Key Questions for Brandon:**
1. Can we retroactively elect S-Corp status for 2024? 2025?
2. What's the best way to handle overdue founder payments?
3. Any penalties we should be aware of for late filing?
4. Recommended approach for reasonable salary (S-Corp)?
5. **Rami's $20k contribution:** What's the best way to document this retroactively? Stock, note, or loan?
6. **2023 partial year:** What needs to be filed for the May-Dec 2023 period?
7. **Delaware Franchise Tax:** What's owed for 2023 and 2024? Any penalties?
8. **California compliance:** Is Automatique registered as a foreign corporation in CA? What filings are needed?
