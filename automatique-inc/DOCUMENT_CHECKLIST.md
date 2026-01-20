# Automatique Inc - Document Gathering Checklist

## Already Have (in existing source-documents)

### Privacy.com (in `source-documents/Archive (Organizations)/Privacy.com Transactions/`)
- [x] `Privacy.com Statement 2024-01-01 - 2024-12-31.csv` - **Already downloaded!**
- [x] `Privacy.com Statement 2024-01-01 - 2024-12-31.pdf`
- [ ] 2025 statement - Not available yet (year just started)

---

## Need to Download

### From Stripe Atlas (https://atlas.stripe.com) - COMPLETE

**Status:** All 12 Stripe Atlas documents downloaded and processed.
**Summary:** See `generated-files/COMPANY_PROFILE.md` for extracted information.

**Corporate Formation Documents:**
- [x] Certificate of Incorporation (Delaware) - **Incorporated 5/7/2023**
- [x] Bylaws - **Standard corporate bylaws**
- [x] EIN Confirmation Letter (IRS SS-4) - **EIN: 38-4207516**
- [x] Initial Board Resolutions (Action by Incorporator + Initial Board Consent)
- [x] Stock Purchase Agreement (Kurt Braget - 8.5M shares for $85)
- [x] 83(b) Election forms - **Filed with proof of mailing**

**Cap Table / Ownership:**
- [x] Cap table: Kurt Braget owns 8,500,000 shares (85% of 10M authorized)
- [x] Stock issuance: Common Stock Purchase Agreement dated 2/7/2024
- [ ] **ISSUE:** Rami's ~$20k contribution NOT documented - needs formalization

**Registered Agent:**
- [x] Registered agent: Legalinc Corporate Services, Inc.
- [x] Address: 651 N Broad St, Suite 201, Middletown, DE 19709

**Annual Compliance:**
- [ ] Delaware Franchise Tax receipts (due March 1 each year) - **Status unknown**
- [ ] Any state filings or annual reports - **Need to verify**

---

### From Mercury (https://mercury.com)

**Bank Statements:**
- [ ] 2024 monthly statements (Jan-Dec) - PDF or download all at once
- [ ] 2025 monthly statements (Jan only so far)

**Transaction Export (MOST IMPORTANT):**
- [ ] 2024 full year CSV export (all transactions)
- [ ] 2025 YTD CSV export
- How to export: Dashboard → Transactions → Export → CSV

**Tax Documents:**
- [ ] Any 1099s from Mercury (1099-INT for interest income)
- [ ] Year-end tax statement if available

**Account Info:**
- [ ] Account number and routing number (for records)
- [ ] Any connected accounts or cards

---

### From Wells Fargo (Personal - for business expenses paid personally)

**2024 Statements:**
- [ ] All 12 monthly statements (Jan-Dec 2024)
- [ ] Or transaction CSV export for 2024

**2025 Statements:**
- [ ] January 2025 (if available)

**Note:** You already have 2022 Wells Fargo statements in `source-documents/Tax - Finance Documents/2022 Tax Info/Well Fargo Statements/`. Check if 2024 statements are there or need to be downloaded.

---

### From Privacy.com (for 2025)

- [ ] 2025 YTD statement when available (probably need to wait or export manually)

**Note:** You'll need to identify which Privacy.com transactions are Automatique business vs personal. Consider creating dedicated Privacy.com cards for Automatique going forward.

---

### From Contractors/Vendors

**For each contractor paid > $600:**
- [ ] Contractor name
- [ ] Address
- [ ] SSN or EIN (for 1099 filing)
- [ ] Total amount paid in 2024
- [ ] Total amount paid in 2025
- [ ] Payment records/invoices

**Known contractors to document:**
- [ ] Rami - amounts owed/paid
- [ ] Any other developers
- [ ] Any other service providers

---

### From Clients (Income Verification)

- [ ] Client contracts or agreements
- [ ] Invoices sent
- [ ] Any 1099s received from clients (if they issued)

---

## Quick Reference - Where to Find Things

| Document | Source | URL |
|----------|--------|-----|
| Incorporation docs | Stripe Atlas | https://atlas.stripe.com → Your Company → Documents |
| EIN Letter | Stripe Atlas | https://atlas.stripe.com → Your Company → Documents |
| Bank statements | Mercury | https://mercury.com → Statements |
| Transaction CSV | Mercury | https://mercury.com → Transactions → Export |
| Tax docs (1099) | Mercury | https://mercury.com → Settings → Tax Documents |
| Privacy.com | Privacy.com | https://privacy.com → Statements |
| Wells Fargo | Wells Fargo | https://wellsfargo.com → Statements & Documents |

---

## File Organization

When downloading, save to:
```
automatique-inc/source-documents/
├── stripe-atlas/          # All Stripe Atlas docs
├── mercury/               # Bank statements + CSV exports
├── privacy-com/           # (can copy from existing or re-download)
├── wells-fargo/           # Personal expenses for Automatique
└── contractors/           # Contractor info and payment records
```

---

## Priority Order

1. **Mercury transaction CSV** - This is the main source of income/expenses
2. **Stripe Atlas docs** - Need EIN, incorporation date, ownership structure
3. **Privacy.com 2024** - Already have it, just need to identify Automatique transactions
4. **Wells Fargo 2024** - For expenses paid personally
5. **Contractor records** - For 1099 filing

---

## Notes

- Automatique was formed via Stripe Atlas (C-Corp)
- Banking is through Mercury
- Need to determine C-Corp vs S-Corp election with accountant Brandon
- 2025 just started, so some docs may not be available yet
