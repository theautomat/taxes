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
| **Mercury Bank** | Company checking account | ✅ DONE | `mercury-checking-2024.csv`, `mercury-checking-2025.csv` |
| **Stripe Atlas** | Incorporation docs, EIN | ✅ DONE | `COMPANY_PROFILE.md` |
| **Wells Fargo 2023** | Personal bank statements | ✅ DONE | `2023/generated-files/extracted/wells-fargo/` (12 months) |
| **Wells Fargo 2024** | Personal bank statements | ✅ DONE | `2024/generated-files/extracted/wells-fargo/` (12 months) |
| **Wells Fargo 2025** | Personal bank statements | ✅ DONE | `2025/generated-files/extracted/wells-fargo/` (12 months) |
| **Privacy.com 2023** | AUTOMATIQUE expenses | ✅ DONE | `2023/generated-files/extracted/privacy-com/` |
| **Privacy.com 2024** | AUTOMATIQUE expenses | ✅ DONE | `2024/generated-files/extracted/privacy-com/` |

---

## Accountant Packages - READY FOR REVIEW

| Year | Package | Status |
|------|---------|--------|
| 2023 | `2023/generated-files/2023_ACCOUNTANT_PACKAGE.md` | ✅ COMPLETE |
| 2024 | `2024/generated-files/2024_ACCOUNTANT_PACKAGE.md` | ✅ COMPLETE |
| 2025 | `2025/generated-files/2025_ACCOUNTANT_PACKAGE.md` | ✅ COMPLETE (YTD) |

---

## Financial Summary

### Three-Year Overview

```
AUTOMATIQUE, INC.
EIN: 38-4207516
Structure: C-Corporation (Delaware)
Incorporated: May 7, 2023

═══════════════════════════════════════════════════════════════
                        2023        2024        2025 (YTD)
═══════════════════════════════════════════════════════════════
REVENUE
  Client Income         $0       $12,100           $0
───────────────────────────────────────────────────────────────
TOTAL REVENUE           $0       $12,100           $0

EXPENSES
  Mercury (company)     $0      $13,357         $651
  Personal (reimb)  $15,991        $660         $624
───────────────────────────────────────────────────────────────
TOTAL EXPENSES      $15,991     $14,017       $1,275

NET PROFIT/LOSS    ($15,991)   ($1,917)     ($1,275)
═══════════════════════════════════════════════════════════════

CUMULATIVE NOL: ~$19,184

CAPITAL
  Rami contribution     $0      $20,000           $0

CASH BALANCE (EOY)      $0      $18,743      $18,091
═══════════════════════════════════════════════════════════════
```

### 2023 (Partial Year: May 7 - Dec 31)
| Category | Amount | Notes |
|----------|--------|-------|
| Revenue | $0 | No client income |
| Expenses (Personal) | $15,991 | All paid personally by Kurt |
| **Net** | **($15,991)** | Loss |

**Key 2023 Expenses:**
- Contractor payments: $10,000 (Pablo app development)
- Developer tools: $2,411 (GitHub, Heroku, Sentry, Bitrise, etc.)
- AI/ML tools: $1,748 (ChatGPT, OpenAI, Midjourney, ElevenLabs)
- Domains & marketing: $1,206
- Incorporation: $500 (Stripe Atlas)
- Legal services: $125 (LegalZoom registered agent)

### 2024 (Full Year)
| Category | Amount | Notes |
|----------|--------|-------|
| Revenue | $12,100 | KOOP CO./BlendFi software dev |
| Expenses (Mercury) | $13,357 | Company-paid expenses |
| Expenses (Personal) | $660 | LegalZoom + Google Workspace |
| Capital Contribution | $20,000 | Rami wire (NOT revenue) |
| **Net** | **($1,917)** | Loss |

**Key 2024 Expenses:**
- George (contractor): $8,105 (international developer)
- PARO MARKETPLACE: $3,450 (accounting firm - bad experience)
- Bitrise: $840 (CI/CD)
- OpenAI: $360 (AI API)
- LegalZoom: $372 (registered agent - personal)
- Google Workspace: $360 (Feb-Dec)
- Heroku: $260 (hosting)
- Notion: $176 (productivity)

### 2025 (YTD - January)
| Category | Amount | Notes |
|----------|--------|-------|
| Revenue | $0 | No client income yet |
| Expenses (Mercury) | $651 | January only |
| Expenses (Personal) | $624 | Full year projected |
| **Net (projected)** | **($1,275)** | Loss |

**Monthly burn rate:** ~$703
**Cash runway:** ~26 months

---

## Outstanding Items

### 1. George Contractor Info (for 1099)
- [ ] Full legal name
- [ ] Address
- [ ] Tax ID (SSN or foreign equivalent)
- [ ] Total paid in 2024: $8,105.31
- **Question:** Is 1099 required for international contractor?

### 2. Rami's $20,000 Contribution
- [ ] Formalize the contribution (stock, loan, SAFE, or capital contribution?)
- Wire received: June 14, 2024
- Currently undocumented

### 3. Delaware Franchise Tax
- [ ] Verify 2023 payment status
- [ ] Verify 2024 payment status
- Due: March 1 each year

### 4. S-Corp Election Decision
- [ ] Brandon to advise: S-Corp vs C-Corp
- [ ] If S-Corp: Can we retroactively elect for 2023/2024?

---

## Questions for Brandon

### Structure
1. **S-Corp vs C-Corp:** Which is better given ~$19k cumulative losses?
2. **Retroactive Election:** Can we elect S-Corp for prior years to pass through losses?

### Treatment
3. **Rami's $20k:** How to document? (equity, loan, contribution?)
4. **Personal Expenses:** Kurt paid ~$17k of business expenses personally - loan or contribution?
5. **George 1099:** Required for international contractor?

### Compliance
6. **Delaware Franchise Tax:** Status and any penalties?
7. **California Foreign Corp:** Any CA compliance requirements?
8. **Late Filing:** Penalties for 2023/2024 returns?

### NOL
9. **Cumulative Loss:** Best way to utilize ~$19k NOL?

---

## Completed Tasks

- [x] Extract Mercury 2024 transactions
- [x] Extract Mercury 2025 transactions
- [x] Extract Wells Fargo 2023 (12 months)
- [x] Extract Wells Fargo 2024 (12 months)
- [x] Extract Wells Fargo 2025 (12 months)
- [x] Extract Privacy.com 2023 AUTOMATIQUE expenses
- [x] Extract Privacy.com 2024 AUTOMATIQUE expenses
- [x] Create 2023 Accountant Package
- [x] Create 2024 Accountant Package
- [x] Create 2025 Accountant Package
- [x] Clarify PARO MARKETPLACE transaction
- [x] Clarify Maxima refund transaction
- [x] Clarify Auto Routing (BlendFi) payments

---

## Next Steps

1. [ ] Get George contractor info for 1099
2. [ ] Formalize Rami's $20k contribution
3. [ ] Verify Delaware Franchise Tax status
4. [ ] Send packages to Brandon for review
5. [ ] Schedule meeting with Brandon to discuss questions

---

*Last updated: 2025-01-21*
