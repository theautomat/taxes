# 2023 Expenses & Deductions Research Report

**Prepared:** 2026-02-05
**Tax Year:** 2023
**Purpose:** Identify expense/deduction categories and data gaps for 2023 tax filing

---

## 1. Summary of 2022 Expense Categories (Reference)

The 2022 tax year had the following deduction categories fully researched and documented. These serve as the baseline for what to track in 2023.

### 2022 Deduction Amounts by Category

| Category | 2022 Amount | Notes |
|----------|-------------|-------|
| **Schedule A - Itemized Deductions** | | |
| SALT (capped at $10k) | $10,000 | CA income tax $25,600 + property tax $3,095 = $28,695, capped |
| Mortgage Interest | $20,347 | PHH Mortgage, 662 Mountain View, 3.25% rate |
| **S-Corp Amendment (Popstand)** | $17,346 | Software/SaaS $11,920 + Office expenses $5,426 |
| **Business Software/SaaS (Privacy.com)** | $11,920 | Heroku $4,975, GoDaddy $1,771, Google Domains $1,817, QuickNode $1,189, etc. |
| **Vehicle Mileage (Pasadena office)** | $2,156 | 23 trips x 150mi x $0.625/mi (standard mileage rate) |
| **Home Office (simplified)** | $1,500 | 704 sq ft office, capped at $1,500 simplified method |
| **Home Office (actual, recommended)** | $4,087-$4,695 | Mortgage interest + property tax + utilities (business %) |
| **Business Meals (100% in 2022)** | $1,500+ est. | Dozens of restaurant transactions identified |
| **Business Equipment (Amazon)** | $1,142 | Office furniture, computer equipment, books |
| **Office Expenses (Pasadena)** | $337 | Parking; rent was reimbursed by NFT Genius |
| **Cell Phone (AT&T)** | $741-$890 | 50-60% business use of $1,483 total |
| **Utilities (home office portion)** | $514 | 15.2% of Edison $2,661, Gas $488, Water $230 |
| **Tesla Charging (business)** | $216 | Pasadena office + Las Vegas trip |
| **Personal Assistant** | $1,500 | Mark Cousineau, Zelle payment |
| **401(k) Contributions** | $8,000 | Already in W-2 Box 1 (ForUsAll via NFT Genius) |
| **TOTAL (estimated)** | **$53,430+** | Approx $20,491 in tax savings at 45.3% |

---

## 2. Key 2023 Tax Law Changes vs. 2022

| Item | 2022 | 2023 | Impact |
|------|------|------|--------|
| Standard deduction (single) | $12,950 | $13,850 | Higher threshold to beat |
| Business meals (restaurant) | 100% deductible | 50% deductible | Meals deduction cut in half |
| Bonus depreciation | 100% | 80% | Slightly less equipment benefit |
| Standard mileage rate | $0.585/$0.625 | $0.655 | Higher rate benefits vehicle deduction |
| SALT cap | $10,000 | $10,000 | No change |
| 401(k) contribution limit | $20,500 | $22,500 | Higher limit if contributing |

---

## 3. What 2023 Data Already Exists

### Source Documents Present

| Document | Location | Status |
|----------|----------|--------|
| Wells Fargo statements (all 12 months) | `personal/2023/source-documents/wells-fargo/` | PDF only, not extracted |
| Privacy.com statement (CSV + PDF) | `personal/2023/source-documents/privacy-com/` | CSV available, not extracted |
| Popstand Chase statements (12 months) | `personal/2023/source-documents/popstand-chase/` | PDF only |
| NFT Genius W-2 | `personal/2023/source-documents/nft-genius/2023-w2-nft-genius.pdf` | Present |
| Popstand tax return | `personal/2023/source-documents/popstand/2023-popstand-tax-return.pdf` | Present |
| 2023 annual property tax bill | `personal/shared/property-taxes/2023-annual-tax-bill.pdf` | Present |

### Extracted/Generated Data

**None.** The `generated-files/extracted/`, `merged/`, `merged-deduped/`, `final/`, and `deductions/` directories contain only `.gitkeep` placeholder files. No extraction or processing has been done for 2023.

---

## 4. What Needs to Be Collected/Done for 2023

### Priority 1: Extract Existing Source Documents

These documents exist but need extraction into standardized CSV format:

1. **Wells Fargo statements (12 months)** - Extract all transactions to CSV
   - Files: `2023-01-31-wells-fargo.pdf` through `2023-12-31-wells-fargo.pdf`
   - Output: `generated-files/extracted/wells-fargo/2023-01_wells-fargo_checking.csv` through `2023-12_wells-fargo_checking.csv`
   - This is the PRIMARY source for expense tracking (utilities, meals, personal expenses, transfers)

2. **Privacy.com statement** - Extract/normalize the raw CSV
   - Source: `privacy-com-statement-2023.csv` (raw CSV already exists)
   - Output: `generated-files/extracted/privacy-com/2023_privacy-com_transactions.csv`
   - Key for: Business software/SaaS subscriptions (Heroku, GoDaddy, QuickNode, etc.)
   - Preliminary scan shows: Heroku, QuickNode, GoDaddy, GitHub, Google Domains, Amazon, Netflix, Blink continue in 2023

3. **Popstand Chase statements (12 months)** - Extract wire transfers/business income
   - Already being handled by popstand-researcher (Task #2)

4. **NFT Genius W-2** - Extract income and withholding data
   - Already being handled by nft-genius-researcher (Task #1)

5. **Popstand tax return** - Extract K-1 and business income data
   - Already being handled by popstand-researcher (Task #2)

### Priority 2: Collect Missing Source Documents

These documents are needed but NOT yet in the repo:

| Document | Why Needed | 2022 Equivalent |
|----------|-----------|-----------------|
| **Form 1098 (Mortgage Interest)** | Schedule A, Line 8a - likely $19-20k deduction | Had PHH Mortgage 1098 |
| **IRS Transcripts (Wage & Income)** | Verify all income reported to IRS | Had 2022 W&I transcript |
| **Coinbase statements/tax reports** | Capital gains/losses | Had full 2022 Coinbase data |
| **Tesla charging history 2023** | Vehicle expense deduction (if applicable) | Had 2022 charging CSV |
| **Amazon order history 2023** | Business equipment deduction | Had order PDFs for 2022 |
| **Utility bills (if using actual home office)** | Home office deduction calculation | Edison, Gas, Water from WF statements |
| **AT&T phone bills** | Cell phone business use deduction | ~$1,483 in 2022 |
| **Spectrum internet bills** | Home office utility (missing in 2022 too) | ~$2,460/yr estimated |
| **EJ Harrison trash bills** | Home office utility (missing in 2022 too) | ~$574/yr estimated |
| **DMV vehicle registration** | Personal property tax deduction | Noted as TODO in 2022 |
| **Popstand K-1** | S-Corp income on personal return | Had 2022 K-1 |
| **Any 1099 forms** | Freelance/contract income | N/A |

### Priority 3: Deduction Analysis (After Extraction)

Once data is extracted, the following analyses should be performed:

1. **Software/SaaS services** - Categorize Privacy.com transactions by business service
2. **Home office deduction** - Calculate using same methodology as 2022
3. **Business meals** - Identify restaurant transactions (now 50% deductible, not 100%)
4. **Vehicle expenses** - Check if Pasadena office continued into 2023
5. **Property taxes** - Extract from 2023 tax bill (shared/property-taxes/)
6. **SALT cap analysis** - Calculate state income tax + property tax vs. $10k cap
7. **Mortgage interest** - Need Form 1098 for 2023
8. **Business equipment** - Identify Amazon/other equipment purchases
9. **Utilities** - Extract from Wells Fargo for Edison, Gas, Water
10. **Itemized vs. standard deduction** - Compare at $13,850 threshold

---

## 5. Wells Fargo Statements Status

All 12 monthly statements for 2023 are present in `personal/2023/source-documents/wells-fargo/`:

| Month | File | Extraction Status |
|-------|------|-------------------|
| January | `2023-01-31-wells-fargo.pdf` | Not extracted |
| February | `2023-02-28-wells-fargo.pdf` | Not extracted |
| March | `2023-03-31-wells-fargo.pdf` | Not extracted |
| April | `2023-04-30-wells-fargo.pdf` | Not extracted |
| May | `2023-05-31-wells-fargo.pdf` | Not extracted |
| June | `2023-06-30-wells-fargo.pdf` | Not extracted |
| July | `2023-07-31-wells-fargo.pdf` | Not extracted |
| August | `2023-08-31-wells-fargo.pdf` | Not extracted |
| September | `2023-09-30-wells-fargo.pdf` | Not extracted |
| October | `2023-10-31-wells-fargo.pdf` | Not extracted |
| November | `2023-11-30-wells-fargo.pdf` | Not extracted |
| December | `2023-12-31-wells-fargo.pdf` | Not extracted |

**Action:** Extract all 12 months following the same format as 2022 extraction (Date, Description, Amount, Source, Notes, Balance).

---

## 6. Privacy.com 2023 Preliminary Analysis

A quick scan of the raw `privacy-com-statement-2023.csv` shows the following recurring business services continuing from 2022:

| Service | Description | Estimated 2023 Spend |
|---------|-------------|---------------------|
| **Heroku** | Cloud hosting (multiple apps) | $100-350/mo (continuing) |
| **QuickNode API** | Blockchain node access | $49/mo |
| **GoDaddy** | Domain registration/DNS | Various (large charges visible) |
| **Google Domains** | Domain registration | Various |
| **GitHub** | Code repository | $10/mo |
| **Netflix** | Streaming (likely personal) | $15.49/mo |
| **Blink** | Video communication | $10/mo |
| **Amazon** | Various purchases | High volume |

**Full extraction and categorization needed** to get accurate 2023 totals.

---

## 7. Automatique Inc Consideration for 2023

Automatique Inc (new S-Corp) was incorporated via Stripe Atlas. Mercury bank statements begin in August 2023:
- `automatique-inc/archive/mercury/archive/automatique-inc-2599-monthly-statement-2023-08.pdf` through `2023-12.pdf`
- `automatique-inc/archive/mercury/archive/automatique-inc-7968-monthly-statement-2023-08.pdf` through `2023-12.pdf`

**Impact on personal 2023 taxes:** Some business expenses may shift from personal to Automatique Inc starting Aug 2023. This needs coordination with the automatique-researcher (Task #5).

---

## 8. Key Differences Expected Between 2022 and 2023

### Income Changes to Investigate
- Did NFT Genius W-2 income change significantly?
- Did Popstand distributions continue at similar levels?
- Was there any Automatique Inc income (Aug-Dec 2023)?
- Any Coinbase crypto gains/losses?

### Expense Changes to Investigate
- Did the Pasadena office continue into 2023? (Affects vehicle mileage deduction)
- Did Heroku costs decrease? (Some downscaling visible in late 2022)
- Were there any large equipment purchases?
- Did mortgage terms change? (Same 3.25% rate expected)
- Any new business ventures or income sources?

### Structural Changes
- Automatique Inc established mid-2023 - may affect where business expenses are reported
- Business meals revert to 50% deductible (from 100% in 2022)
- Standard mileage rate increased to $0.655/mile (from $0.585/$0.625)

---

## 9. Recommended Next Steps

### Immediate (Extraction Phase)
1. Extract all 12 Wells Fargo 2023 statements to CSV
2. Normalize/extract Privacy.com 2023 CSV
3. Merge and deduplicate all 2023 transactions

### Short-term (Collection Phase)
4. Locate and obtain 2023 Form 1098 (mortgage interest)
5. Locate and obtain 2023 IRS Wage & Income transcript
6. Download 2023 Tesla charging history
7. Collect 2023 Amazon order history for business equipment
8. Obtain 2023 Coinbase tax reports (if any crypto activity)

### Medium-term (Analysis Phase)
9. Categorize all 2023 transactions (business vs. personal)
10. Calculate home office deduction (simplified vs. actual)
11. Identify and document business meals (with 50% rule)
12. Calculate vehicle mileage deduction (if applicable)
13. Prepare Schedule A comparison (itemized vs. $13,850 standard)
14. Coordinate with Automatique Inc for expense allocation (Aug-Dec)

---

## 10. File Locations Reference

### 2022 Deduction Breakdowns (for reference)
- Summary: `personal/2022/generated-files/deductions/2022-deductions-summary-for-accountant.md`
- Tax analysis: `personal/2022/generated-files/deductions/2022-tax-deduction-analysis.md`
- Schedule A: `personal/2022/generated-files/deductions/schedule-a-2022-final.md`
- Software/SaaS: `personal/2022/generated-files/deductions/breakdowns/breakdown-2022-software-services.md`
- Home office: `personal/2022/generated-files/deductions/breakdowns/breakdown-2022-home-office-summary.md`
- Mortgage: `personal/2022/generated-files/deductions/breakdowns/breakdown-2022-mortgage-interest.md`
- Property tax: `personal/2022/generated-files/deductions/breakdowns/breakdown-2022-property-taxes.md`
- Utilities: `personal/2022/generated-files/deductions/breakdowns/breakdown-2022-utilities.md`
- Tesla charging: `personal/2022/generated-files/deductions/breakdowns/breakdown-2022-tesla-charging-costs.md`
- Vehicle mileage: `personal/2022/generated-files/deductions/2022-tax-deduction-analysis.md` (Directive 1)
- Personal assistants: `personal/2022/generated-files/deductions/breakdowns/breakdown-2022-personal-assistants.md`
- SALT cap: `personal/2022/generated-files/deductions/breakdowns/breakdown-2022-salt-cap-analysis.md`

### 2023 Source Documents
- Wells Fargo: `personal/2023/source-documents/wells-fargo/`
- Privacy.com: `personal/2023/source-documents/privacy-com/`
- NFT Genius W-2: `personal/2023/source-documents/nft-genius/2023-w2-nft-genius.pdf`
- Popstand tax return: `personal/2023/source-documents/popstand/2023-popstand-tax-return.pdf`
- Popstand Chase: `personal/2023/source-documents/popstand-chase/`
- Property tax bill: `personal/shared/property-taxes/2023-annual-tax-bill.pdf`

### 2023 Output Directories (created, awaiting data)
- Extracted: `personal/2023/generated-files/extracted/wells-fargo/`, `extracted/privacy-com/`
- Merged: `personal/2023/generated-files/merged/`
- Deduped: `personal/2023/generated-files/merged-deduped/`
- Final: `personal/2023/generated-files/final/`
- Deductions: `personal/2023/generated-files/deductions/`

---

*This research report identifies all expense/deduction categories from 2022, inventories what 2023 data exists, and outlines what needs to be collected and processed for the 2023 tax year.*
