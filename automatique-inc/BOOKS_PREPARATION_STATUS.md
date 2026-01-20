# Automatique Inc - Books Preparation Status

## Goal

Prepare clean, simple financial summary for accountant Brandon to:
1. See income, expenses, profit/loss at a glance (2023, 2024, 2025)
2. Advise on C-Corp vs S-Corp election
3. Determine optimal payment structure (Beau, Rami)
4. File taxes correctly

---

## Data Sources & Status

| Source | Description | Status | Output |
|--------|-------------|--------|--------|
| **Mercury Bank** | Company checking account | ✅ DONE | `mercury-checking-2024.csv`, `mercury-checking-2025.csv` |
| **Stripe Atlas** | Incorporation docs, EIN | ✅ DONE | `COMPANY_PROFILE.md` |
| **Wells Fargo** | Personal expenses for business | ⏳ WAITING | Need statements from Beau |
| **Privacy.com** | Virtual cards for subscriptions | ⏳ WAITING | Need 2024-2025 statements |
| **Other receipts** | Any business expenses paid elsewhere | ⏳ WAITING | Need from Beau |

---

## Financial Summary (What We Know)

### 2023 (Partial Year: May 7 - Dec 31)
| Category | Amount | Notes |
|----------|--------|-------|
| Revenue | $0 | No Mercury activity |
| Expenses | $0 | No Mercury activity |
| **Net** | **$0** | Company was dormant in Mercury |

**Note:** May have personal expenses that should be reimbursed. Need Wells Fargo/Privacy.com data.

### 2024 (Full Year)
| Category | Amount | Notes |
|----------|--------|-------|
| Revenue (KOOP CO.) | $12,100 | Software dev ($9,600 + $2,500 on Apr 8) |
| Revenue (Studio Maxima) | $0 | $2,500 deposit (Feb 22) then refunded (May 10) |
| Capital Contribution | $20,000 | Rami wire Jun 14 (NOT revenue) |
| Expenses (Mercury) | -$15,857.41 | Contractors, SaaS, fees |
| **Net Operating** | **-$3,757.41** | Loss before personal expenses |

**Key 2024 Expenses (from Mercury):**
| Vendor | Amount | Category |
|--------|--------|----------|
| George (contractor) | $10,601.06 | Contractor - international, may need 1099 |
| PARO MARKETPLACE | $3,449.60 | **Accounting firm** (bad experience, couldn't cancel) |
| Maxima | $2,500.00 | **Client refund** (difficult client, we refunded deposit) |
| Bitrise Limited | $840.00 | CI/CD Software |
| OpenAI | $360.00 | AI API |
| Heroku | $259.60 | Hosting |
| Notion | $242.00 | Productivity |
| Exchange Fees | $80.90 | Bank Fees |
| Google Workspace | $72.00 | Email/Docs |
| Slack | $12.41 | Communication |
| Google Cloud | $2.13 | Cloud |

**Note on Maxima:** The -$2,500 expense was a refund of a deposit they paid. If the original deposit came in before Feb 2024 or via different account, we need to find it. Net revenue from Maxima = $0.

### 2025 (YTD - January only)
| Category | Amount | Notes |
|----------|--------|-------|
| Revenue | $0 | No deposits yet |
| Expenses | -$651.31 | SaaS subscriptions |
| **Net** | **-$651.31** | Loss |

---

## What's Missing

### 1. Personal Expenses Paid for Business (Wells Fargo / Privacy.com)
These are business expenses Beau paid personally that should be tracked:
- Software subscriptions
- Domain registrations
- Hosting services
- Any other business tools

**Action:** Beau to provide Wells Fargo and Privacy.com statements

### 2. Categorization Verification
Clarified transactions:
- [x] **PARO MARKETPLACE** ($3,449.60) - Accounting firm (bad experience, couldn't stop payment). Category: Professional Services - Accounting
- [x] **Maxima** ($2,500.00) - REFUND to client. They paid deposit for dev work, we refunded because difficult client. NET REVENUE FROM MAXIMA = $0
- [x] **Auto Routing** ($14,600) - Payments from **BlendFi** (1/BLENDFI INC) for software development services

### 3. George Contractor Info (for 1099)
- [ ] Full legal name
- [ ] Address
- [ ] Tax ID (SSN or foreign equivalent)
- [ ] Total paid in 2024: $10,601.06

---

## Deliverable for Accountant

### Simple One-Page Summary

```
AUTOMATIQUE, INC.
EIN: 38-4207516
Structure: C-Corporation (Delaware)
Incorporated: May 7, 2023

═══════════════════════════════════════════════════════
                    2023        2024        2025 (YTD)
═══════════════════════════════════════════════════════
REVENUE
  Client Income      $0       $14,600         $0
  (Bloom/SUO TECH)   $0          $0           $0
───────────────────────────────────────────────────────
TOTAL REVENUE        $0       $14,600         $0

EXPENSES
  Mercury (direct)   $0      -$15,857        -$651
  Personal (reimb)   TBD         TBD          TBD
───────────────────────────────────────────────────────
TOTAL EXPENSES       TBD         TBD          TBD

NET PROFIT/LOSS      TBD      ~-$1,257       -$651
═══════════════════════════════════════════════════════

CAPITAL
  Rami contribution  $0       $20,000         $0

POTENTIAL PAYMENTS
  Beau (owner)       TBD         TBD          TBD
  Rami (partner)     TBD         TBD          TBD

QUESTIONS FOR ACCOUNTANT
1. Should we elect S-Corp retroactively?
2. How to handle Rami's $20k (equity vs loan vs contribution)?
3. Optimal payment structure for Beau and Rami?
4. Any penalties for late filing 2023/2024?
5. George 1099 - required for international contractor?
```

---

## Next Steps

### Immediate
1. [ ] Beau provides Wells Fargo 2023-2024 statements
2. [ ] Beau provides Privacy.com 2024-2025 CSV exports
3. [ ] Clarify PARO MARKETPLACE and Maxima transactions

### After Data Received
4. [ ] Extract/categorize personal expenses for business
5. [ ] Merge all sources into consolidated view
6. [ ] Identify any missing documentation

### Final Preparation
7. [ ] Create clean summary for accountant
8. [ ] Model C-Corp vs S-Corp scenarios
9. [ ] Model payment scenarios (Beau + Rami at different amounts)
10. [ ] Send to Brandon for review

---

## Questions to Answer Before Accountant Meeting

**For Beau:**
- How much do you want to pay yourself? (affects tax bracket)
- Any other income in 2024 from other sources?
- Are there expenses from 2023 we should capture?

**For Rami:**
- Confirm profit share percentage (10%/15%/20%)
- Is $20k treated as investment (equity) or loan?

**For Accountant:**
- C-Corp vs S-Corp - which is better given our situation?
- Can we retroactively elect S-Corp for 2024?
- How to formalize Rami's ownership/contribution?
- 1099 requirements for international contractor (George)?
- Late filing penalties estimate?

---

*Last updated: 2025-01-19*
