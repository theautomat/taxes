# Source Document Tracking

This file tracks which source documents have been extracted and which still need processing.

## Wells Fargo Statements - 2022

Location: `source-documents/Tax - Finance Documents/2022 Tax Info/Well Fargo Statements/`

| File | Status | Extracted To | Notes |
|------|--------|--------------|-------|
| 013122 WellsFargo.pdf | ✅ Done | generated-files/extracted/2022-01_wells-fargo_checking.csv | 154 transactions |
| 022822 WellsFargo.pdf | ✅ Done | generated-files/extracted/2022-02_wells-fargo_checking.csv | 181 transactions |
| 033122 WellsFargo.pdf | ✅ Done | generated-files/extracted/2022-03_wells-fargo_checking.csv | 153 transactions |
| 043022 WellsFargo.pdf | ✅ Done | generated-files/extracted/2022-04_wells-fargo_checking.csv | 175 transactions |
| 053122 WellsFargo.pdf | ✅ Done | generated-files/extracted/2022-05_wells-fargo_checking.csv | 176 transactions |
| 063022 WellsFargo.pdf | ✅ Done | generated-files/extracted/2022-06_wells-fargo_checking.csv | 177 transactions |
| 073122 WellsFargo.pdf | ✅ Done | generated-files/extracted/2022-07_wells-fargo_checking.csv | 134 transactions |
| 083122 WellsFargo.pdf | ✅ Done | generated-files/extracted/2022-08_wells-fargo_checking.csv | 191 transactions |
| 093122 WellsFargo.pdf | ✅ Done | generated-files/extracted/2022-09_wells-fargo_checking.csv | 201 transactions |
| 103122 WellsFargo.pdf | ✅ Done | generated-files/extracted/2022-10_wells-fargo_checking.csv | 219 transactions |
| 113022 WellsFargo.pdf | ✅ Done | generated-files/extracted/2022-11_wells-fargo_checking.csv | 199 transactions |
| 123122 WellsFargo.pdf | ✅ Done | generated-files/extracted/2022-12_wells-fargo_checking.csv | 218 transactions |

**Total:** 12 statements | **Done:** 12 | **Pending:** 0

## Privacy.com Transactions

Location: `source-documents/Privacy.com Transactions/`

**Note:** Privacy.com provides both PDF and CSV files. We only process the CSV files since they contain identical data and are faster to process. PDF files are ignored.

| File | Status | Extracted To | Notes |
|------|--------|--------------|-------|
| Privacy.com Statement 2022-01-01 - 2022-12-31.csv | ✅ Done | generated-files/extracted/2022_privacy-com_transactions.csv | 650 transactions (644 sales, 6 refunds) |
| Privacy.com Statement 2022-01-01 - 2022-12-31.pdf | ⏭️ Skip | N/A | Skipped - CSV contains same data |

**Total:** 1 CSV processed | **Done:** 1 | **Pending:** 0

## Other Source Documents

### Automatique
Location: `source-documents/Automatique/`
- Status: ⏳ Not cataloged

### NFT Genius - 2022 Tax Info
Location: `source-documents/Tax - Finance Documents/2022 Tax Info/NFT Genius/`

| File | Status | Extracted To | Notes |
|------|--------|--------------|-------|
| 2022 nft-genius-inc-paystubs-kurt-braget.pdf | ✅ Done | generated-files/extracted/2022_nft-genius_gusto-paystubs.csv | 24 paystubs (bi-monthly) |

**Total:** 1 file | **Done:** 1 | **Pending:** 0

### Popstand Wire Transfers - 2022
Location: `source-documents/Archive (Organizations)/Popstand/Chase Bank Statements/2022/`

| File | Status | Extracted To | Notes |
|------|--------|--------------|-------|
| Chase Bank Statements (12 PDFs) | ✅ Done | generated-files/extracted/popstand/2022_popstand_wire-transfers.csv | 62 wire transfers consolidated from Chase statements |

**Total:** 1 consolidated file | **Done:** 1 | **Pending:** 0

### Popstand Income - 2022
Location: `source-documents/Tax - Finance Documents/2022 Tax Info/Popstand/`

| File | Status | Extracted To | Notes |
|------|--------|--------------|-------|
| 2022W2 Copy B, C & 2 Kurt Braget.pdf | ⏳ Pending | TBD | Popstand W-2 for 2022 (wages, withholding) |
| 2022-tax-return-documents-popstand-inc-client-copy-no-pass.pdf | ⏳ Pending | TBD | Popstand 2022 tax return package (likely contains K-1 Schedule K-1) |
| popstand-wages-summary.md | ℹ️ Info | N/A | Summary document (reference only) |

**Total:** 2 files to extract | **Done:** 0 | **Pending:** 2

### IRS Transcripts - 2022
Location: `source-documents/Tax - Finance Documents/2022 Tax Info/IRS Transcripts/`

| File | Status | Extracted To | Notes |
|------|--------|--------------|-------|
| 202212_Wage and Income_BRAG_104717730538.pdf | ℹ️ Info | N/A | IRS transcript showing what was reported to IRS (W-2s, 1099s, etc.) - reference for verification |

**Total:** 1 file (reference only) | **Done:** N/A | **Pending:** 0

### Real Estate - 662 Mountain View
Location: `source-documents/Tax - Finance Documents/2022 Tax Info/662 Mountain View/`

**Lender:** PHH Mortgage Corporation

| File | Status | Extracted To | Notes |
|------|--------|--------------|-------|
| 1098 Morgage Interest 01_11_23.pdf | ✅ Done | generated-files/deductions/breakdowns/BREAKDOWN_2022_Mortgage_Interest.md | Form 1098: $20,410.43 interest paid, $887.50 PMI. See comprehensive analysis document. |
| 1099-INT 01_11_23.pdf | ✅ Done | generated-files/deductions/breakdowns/BREAKDOWN_2022_Interest_Income.md | Form 1099-INT: $203.45 interest income from escrow account (taxable income - report on Schedule B) |
| Screen Shot 2023-03-14 at 4.02.47 PM.png | ℹ️ Info | N/A | 2022 tax return payment reference ($24,420) |

**Total:** 2 files to extract | **Done:** 2 | **Pending:** 0

---

## Status Legend
- ✅ Done - Extracted and verified
- ⏳ Pending - Not yet extracted
- ⚠️ Issue - Problem noted, see Notes column
- 🔄 In Progress - Currently being worked on
- ℹ️ Info - Reference/informational only, no extraction needed
- ⏭️ Skip - Intentionally skipped (duplicate data or not needed)

## Notes
Add any issues or special considerations here as you process documents.
