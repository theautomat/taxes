# Project Tasks

This document tracks ongoing improvements and fixes for the taxes project documentation and structure.

## Current Tasks

### Documentation Consistency Issues

- [ ] **Clarify stage numbering** - Decide on 3 or 4 stages and be consistent across all documentation
- [x] **Create placeholder directories** - `generated-files/final/` exists (empty, ready for final processed data)
- [ ] **Remove hardcoded paths** - Replace `/Users/beau/Projects/taxes` with relative paths or placeholders in CLAUDE.md

### Income Reconciliation

- [ ] **Resolve Popstand K-1 distribution discrepancy** - Reconcile $46,633 difference between K-1 reported distributions ($164,567) and Wells Fargo wire transfers ($211,200)

### Tax Filing - 2022

- [ ] **Complete Schedule B (Interest Income)** - Fill out Schedule B Part I with all interest sources including PHH Mortgage escrow interest ($203.45). See `BREAKDOWN_2022_Interest_Income.md` for details.
- [ ] **Transfer interest total to Form 1040, Line 2b** - After completing Schedule B, transfer total taxable interest amount to Form 1040, Line 2b

### Deduction Research - 2022

- [x] **Research Personal Assistant deductibility** - Analysis COMPLETE in `BREAKDOWN_2022_Personal_Assistants.md`. Remaining actions: verify 1099-NEC was filed, consult tax preparer on deductibility.
- [x] **Research Accountable Plan implementation** - Analysis COMPLETE in `BREAKDOWN_2022_Accountable_Plan.md`. Remaining actions: consult tax preparer on retroactive implementation feasibility.
- [x] **Research First Time Abatement eligibility** - Stub in `BREAKDOWN_2022_First_Time_Abatement.md`. Keep as backup option if penalties assessed.
- [x] **Research Reasonable Cause criteria** - Stub in `BREAKDOWN_2022_Reasonable_Cause.md`. Alternative to FTA if needed.

## Completed Tasks

- [x] **Wells Fargo 2022 extraction** - All 12 months extracted to CSV
  - 2,024 transactions extracted
  - Merged and deduplicated
  - Output: `generated-files/extracted/wells-fargo/`, `generated-files/merged-deduped/2022_deduped_2025-10-16_162510.csv`
- [x] **Standardize CSV format** - Migrated from Deposits/Withdrawals to single Amount column (negative for expenses, positive for income)
  - Converted all 16 existing CSV files (14 extracted + 2 merged)
  - Updated all conversion scripts (fix_wells_fargo_schema.py, convert_privacy_com_to_standard_csv.py, merge_all_csvs.py)
  - Updated documentation (README.md, CLAUDE.md, scripts/README.md)
- [x] **Fix path references** - Updated all path references in SOURCE_TRACKING.md
  - Changed all instances of `extracted-data/` to `generated-files/extracted/`
  - All 14 file path references updated
- [x] **Add Source column** - Added Source field to standard format across all docs and files
  - Source column now included in all CSVs for audit trail and deduplication
  - Updated all conversion scripts to populate Source field
  - Documentation updated to reflect new column

---

## Notes

- Update this file as tasks are completed
- Add new tasks as they are identified
- Check off tasks using `[x]` when complete
