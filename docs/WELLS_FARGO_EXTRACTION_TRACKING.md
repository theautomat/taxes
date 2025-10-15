# Wells Fargo 2022 Re-Extraction Tracking

This document tracks the progress of re-extracting all 12 Wells Fargo 2022 monthly statements using the improved extraction process documented in `WELLS_FARGO_EXTRACTION_PROCESS.md`.

## Overview

**Branch:** `wells-fargo-reextraction-2022`
**Start Date:** 2025-10-14
**Process Document:** `docs/WELLS_FARGO_EXTRACTION_PROCESS.md`
**Archive Location:** `generated-files/archived/2025-10-14_pre-reextraction/`

## Extraction Status

| Month | PDF Source | Status | Extracted By | Reviewed By | Completion Date | Notes |
|-------|-----------|--------|--------------|-------------|-----------------|-------|
| Jan 2022 | `013122 WellsFargo.pdf` | ⏳ Pending | | | | |
| Feb 2022 | `022822 WellsFargo.pdf` | ⏳ Pending | | | | |
| Mar 2022 | `033122 WellsFargo.pdf` | ⏳ Pending | | | | |
| Apr 2022 | `043022 WellsFargo.pdf` | ⏳ Pending | | | | Known issue: Zuber Lawler wire transfer sign error |
| May 2022 | `053122 WellsFargo.pdf` | ⏳ Pending | | | | |
| Jun 2022 | `063022 WellsFargo.pdf` | ⏳ Pending | | | | |
| Jul 2022 | `073122 WellsFargo.pdf` | ⏳ Pending | | | | |
| Aug 2022 | `083122 WellsFargo.pdf` | ⏳ Pending | | | | |
| Sep 2022 | `093022 WellsFargo.pdf` | ⏳ Pending | | | | |
| Oct 2022 | `103122 WellsFargo.pdf` | ⏳ Pending | | | | |
| Nov 2022 | `113022 WellsFargo.pdf` | ⏳ Pending | | | | |
| Dec 2022 | `123122 WellsFargo.pdf` | ⏳ Pending | | | | |

## Status Legend

- ⏳ **Pending** - Not yet started
- 🔄 **In Progress** - Currently being extracted
- 👀 **Review** - Extraction complete, waiting for human review
- ✅ **Done** - Extraction complete and approved
- ⚠️ **Issue** - Problem found, needs correction

## Workflow for Each Month

### 1. Pre-Extraction
- [ ] Mark month as "🔄 In Progress" in this tracking file
- [ ] Open source PDF: `source-documents/Tax - Finance Documents/2022 Tax Info/Well Fargo Statements/[PDF filename]`
- [ ] Note beginning and ending balance from PDF for verification

### 2. Extraction
- [ ] Use AI vision to carefully read PDF
- [ ] Follow all rules in `docs/WELLS_FARGO_EXTRACTION_PROCESS.md`
- [ ] Pay special attention to:
  - Deposits section → POSITIVE amounts
  - Withdrawals section → NEGATIVE amounts
  - Wire transfers (check which section they appear in)
  - Large amounts (double-check signs)
- [ ] Generate CSV with standard schema

### 3. Verification
Run through checklist:
- [ ] Balance verification: Does ending balance match PDF?
- [ ] Transaction count: Matches PDF?
- [ ] Date format: All YYYY-MM-DD?
- [ ] Sign check: All deposits positive, all withdrawals negative?
- [ ] Wire service charges: All negative?
- [ ] Description accuracy: Spot-check 5-10 random descriptions
- [ ] Source field: All rows have correct PDF filename?
- [ ] No empty amounts?

### 4. Save Output
- [ ] Save to: `generated-files/extracted/YYYY-MM_wells-fargo_checking.csv`
- [ ] Update this tracking file to mark month as "👀 Review"
- [ ] Commit to git: `git add generated-files/extracted/YYYY-MM_wells-fargo_checking.csv docs/WELLS_FARGO_EXTRACTION_TRACKING.md`
- [ ] Commit message: `feat: Re-extract Wells Fargo YYYY-MM statement`

### 5. Human Review
- [ ] User reviews CSV against PDF
- [ ] User checks wire transfers and large amounts
- [ ] User approves or requests corrections
- [ ] If corrections needed: return to step 2
- [ ] If approved: update tracking file to mark as "✅ Done"

### 6. Completion
- [ ] Mark month as "✅ Done" in tracking table
- [ ] Add completion date
- [ ] Note any special issues in Notes column
- [ ] Move to next month

## Post-Extraction Tasks

After all 12 months are complete and approved:

- [ ] Re-run merge script: `python3 scripts/merge_all_csvs.py`
- [ ] Re-run deduplication script: `python3 scripts/deduplicate_transactions.py`
- [ ] Compare statistics with archived versions
- [ ] Update `docs/SOURCE_TRACKING.md` with re-extraction completion
- [ ] Merge branch to main
- [ ] Delete archived files (optional - keep for comparison if desired)

## Quality Metrics

Track these metrics for comparison with original extraction:

| Metric | Original | Re-extraction | Change |
|--------|----------|---------------|--------|
| Total transactions | 2,178 | TBD | TBD |
| Wire transfers | TBD | TBD | TBD |
| Sign errors corrected | 0 (baseline) | TBD | TBD |
| Average transaction count per month | 181.5 | TBD | TBD |

## Known Issues from Original Extraction

### Confirmed Errors:
1. **April 2022 - Zuber Lawler LLP**: Wire transfer to law firm for $25,000 marked as positive (income) instead of negative (expense)

### To Verify During Re-extraction:
- All wire transfers (especially to vendors, law firms, service providers)
- Large amounts (>$10,000)
- Recurring subscriptions (ensure consistent signs)

## Notes

- Take your time - accuracy is more important than speed
- When in doubt, check the section header in the PDF (Deposits vs Withdrawals)
- Ask questions if anything is ambiguous
- Document any unusual patterns or difficult transactions

---

**Last Updated:** 2025-10-14
**Updated By:** Initial creation
