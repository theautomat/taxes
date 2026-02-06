# Wells Fargo 2022 Re-Extraction Tracking

This document tracks the progress of re-extracting all 12 Wells Fargo 2022 monthly statements using the improved extraction process documented in `WELLS_FARGO_EXTRACTION_PROCESS.md`.

## Overview

**Branch:** `wells-fargo-reextraction-2022`
**Start Date:** 2025-10-14
**Completion Date:** 2025-10-16
**Process Document:** `docs/WELLS_FARGO_EXTRACTION_PROCESS.md`
**Archive Location:** `personal/2022/generated-files/archived/2025-10-14_pre-reextraction/`

## Extraction Status

| Month | PDF Source | Status | Transactions | Completion Date |
|-------|-----------|--------|--------------|-----------------|
| Jan 2022 | `013122 WellsFargo.pdf` | ✅ Done | 170 | 2025-10-16 |
| Feb 2022 | `022822 WellsFargo.pdf` | ✅ Done | 177 | 2025-10-16 |
| Mar 2022 | `033122 WellsFargo.pdf` | ✅ Done | 136 | 2025-10-16 |
| Apr 2022 | `043022 WellsFargo.pdf` | ✅ Done | 171 | 2025-10-16 |
| May 2022 | `053122 WellsFargo.pdf` | ✅ Done | 166 | 2025-10-16 |
| Jun 2022 | `063022 WellsFargo.pdf` | ✅ Done | 151 | 2025-10-16 |
| Jul 2022 | `073122 WellsFargo.pdf` | ✅ Done | 123 | 2025-10-16 |
| Aug 2022 | `083122 WellsFargo.pdf` | ✅ Done | 164 | 2025-10-16 |
| Sep 2022 | `093022 WellsFargo.pdf` | ✅ Done | 158 | 2025-10-16 |
| Oct 2022 | `103122 WellsFargo.pdf` | ✅ Done | 227 | 2025-10-16 |
| Nov 2022 | `113022 WellsFargo.pdf` | ✅ Done | 176 | 2025-10-16 |
| Dec 2022 | `123122 WellsFargo.pdf` | ✅ Done | 205 | 2025-10-16 |

**Total Transactions:** 2,024 (excluding headers)

## Status Legend

- ✅ **Done** - Extraction complete and approved

## Completed Post-Extraction Tasks

- [x] Re-run merge script: `python3 scripts/merge_all_csvs.py`
- [x] Re-run deduplication script: `python3 scripts/deduplicate_transactions.py`
- [x] Merge branch to main

## Quality Metrics

| Metric | Original | Re-extraction | Change |
|--------|----------|---------------|--------|
| Total transactions | 2,178 | 2,024 | -154 (deduplication) |
| Average transaction count per month | 181.5 | 168.7 | Refined |

## Output Files

- **Extracted CSVs:** `personal/2022/generated-files/extracted/wells-fargo/2022-*_wells-fargo_checking.csv`
- **Merged file:** `personal/2022/generated-files/merged/2022_all-transactions_merged_2025-10-15.csv`
- **Deduplicated file:** `personal/2022/generated-files/merged-deduped/2022_deduped_2025-10-16_162510.csv`

---

**Last Updated:** 2025-01-22
**Status:** ✅ COMPLETE
