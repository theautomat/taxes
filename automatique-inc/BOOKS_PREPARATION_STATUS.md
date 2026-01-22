# Automatique Inc - Books Preparation Status

## Goal

Prepare clean, simple financial summary for accountant Brandon to:
1. See income, expenses, profit/loss at a glance (2023, 2024, 2025)
2. Advise on C-Corp vs S-Corp election
3. Determine optimal payment structure (Kurt, Rami)
4. File taxes correctly

---

## Data Sources & Status

| Source | Description | Status | Output |
|--------|-------------|--------|--------|
| **Mercury Bank 2024** | Company checking account | ✅ DONE | `2024/generated-files/extracted/mercury/` |
| **Mercury Bank 2025** | Company checking account | ✅ DONE | `2025/generated-files/extracted/mercury/` |
| **Stripe Atlas** | Incorporation docs, EIN | ✅ DONE | `COMPANY_PROFILE.md` |
| **Wells Fargo 2023** | Personal bank statements | ✅ DONE | `2023/generated-files/extracted/wells-fargo/` (12 months) |
| **Wells Fargo 2024** | Personal bank statements | ✅ DONE | `2024/generated-files/extracted/wells-fargo/` (12 months) |
| **Wells Fargo 2025** | Personal bank statements | ✅ DONE | `2025/generated-files/extracted/wells-fargo/` (12 months) |
| **Privacy.com 2023** | AUTOMATIQUE expenses | ✅ DONE | `2023/generated-files/extracted/privacy-com/` |
| **Privacy.com 2024** | AUTOMATIQUE expenses | ✅ DONE | `2024/generated-files/extracted/privacy-com/` |
| **Privacy.com 2025** | AUTOMATIQUE expenses | ✅ DONE | `2025/generated-files/extracted/privacy-com/` |

---

## Accountant Packages - READY FOR REVIEW

| Year | Package | Status |
|------|---------|--------|
| 2023 | `2023/generated-files/2023_ACCOUNTANT_PACKAGE.md` | ✅ COMPLETE |
| 2024 | `2024/generated-files/2024_ACCOUNTANT_PACKAGE.md` | ✅ COMPLETE |
| 2025 | `2025/generated-files/2025_ACCOUNTANT_PACKAGE.md` | ✅ COMPLETE |

---

## Financial Summary

### Three-Year Overview

```
AUTOMATIQUE, INC.
EIN: 38-4207516
Structure: C-Corporation (Delaware)
Incorporated: May 7, 2023

═══════════════════════════════════════════════════════════════
                        2023        2024        2025
═══════════════════════════════════════════════════════════════
REVENUE                   $0      $12,100      $88,080
EXPENSES             $15,991      $14,018      $14,830
───────────────────────────────────────────────────────────────
NET INCOME          ($15,991)    ($1,918)     $73,251

CAPITAL
  Rami contribution       $0      $20,000           $0

CASH BALANCE (EOY)        $0      $18,743      $92,617
═══════════════════════════════════════════════════════════════

Prior Year NOL: $17,909 (2023 + 2024 losses)
2025 Estimated Taxable (after NOL): ~$55,342
```

### 2023 (Partial Year: May 7 - Dec 31)
| Category | Amount | Notes |
|----------|--------|-------|
| Revenue | $0 | No client income |
| Expenses (Personal) | $15,991 | All paid personally by Kurt |
| **Net** | **($15,991)** | Loss |

### 2024 (Full Year)
| Category | Amount | Notes |
|----------|--------|-------|
| Revenue | $12,100 | KOOP CO./BlendFi software dev |
| Expenses (Mercury) | $13,357 | Company-paid expenses |
| Expenses (Personal) | $660 | LegalZoom + Google Workspace |
| Capital Contribution | $20,000 | Rami wire (NOT revenue) |
| **Net** | **($1,918)** | Loss |

### 2025 (Full Year)
| Category | Amount | Notes |
|----------|--------|-------|
| Revenue | $88,080 | BlendFi, SUO Tech, Auto Routing |
| Expenses (Mercury) | $14,206 | Company-paid expenses |
| Expenses (Personal) | $624 | LegalZoom + Pablochat |
| **Net** | **$73,251** | **PROFIT** |

---

## Outstanding Items

### 1. Delaware Franchise Tax
- [ ] Check status via Stripe Atlas or Delaware website ($20 for full history)
- [ ] Pay any overdue 2023, 2024 taxes
- [ ] Due: March 1 each year (~$175-400)

### 2. Rami's $20,000 Contribution
- [ ] Formalize the contribution (stock, loan, SAFE, or capital contribution?)
- Wire received: June 14, 2024
- Currently undocumented

### 3. SEP-IRA / Retirement Contribution
- [ ] Ask Brandon about retroactive contribution for 2025
- Potential to reduce taxable income significantly
- With $73k profit, could contribute up to ~25% to SEP-IRA

### 4. S-Corp Election Decision
- [ ] Brandon to advise: S-Corp vs C-Corp
- [ ] If S-Corp: When to elect? (2025 or 2026?)

### 5. Subscription Audit (Cost Savings)
Identified ~$4,900/year in subscriptions to review:
- Bitrise ($1,569) - still using CI/CD?
- Slack ($267) - need team chat for solo work?
- Framer + Sketch ($480) - redundant design tools?
- Notion ($473) - using heavily?
- Various AI tools (Suno, Midjourney, Codeium, Wispr)

---

## Questions for Brandon

### Structure
1. **S-Corp vs C-Corp:** Which is better with $73k profit and $17.9k NOL?
2. **NOL Utilization:** Can prior losses offset 2025 income?

### Tax Planning
3. **SEP-IRA:** Can we contribute retroactively for 2025 to reduce taxes?
4. **Salary vs Distribution:** What's the optimal split if we elect S-Corp?

### Documentation
5. **Rami's $20k:** How to formalize? (equity, loan, contribution?)
6. **Personal Expenses:** Kurt paid ~$17k of business expenses personally - treatment?

---

## Completed Tasks

- [x] Extract Mercury 2024 transactions
- [x] Extract Mercury 2025 transactions (full year, 278 transactions)
- [x] Extract Wells Fargo 2023 (12 months)
- [x] Extract Wells Fargo 2024 (12 months)
- [x] Extract Wells Fargo 2025 (12 months)
- [x] Extract Privacy.com 2023 AUTOMATIQUE expenses
- [x] Extract Privacy.com 2024 AUTOMATIQUE expenses
- [x] Extract Privacy.com 2025 AUTOMATIQUE expenses
- [x] Create 2023 Accountant Package
- [x] Create 2024 Accountant Package
- [x] Create 2025 Accountant Package (corrected with full year data)
- [x] Clean up duplicate Mercury CSV files
- [x] Audit subscriptions for potential savings

---

## Next Steps

1. [ ] Check Delaware franchise tax status
2. [ ] Send packages to Brandon for review
3. [ ] Decide on Rami's $20k formalization
4. [ ] Make decision on S-Corp election
5. [ ] Review and cancel unnecessary subscriptions

---

*Last updated: 2025-01-21*
