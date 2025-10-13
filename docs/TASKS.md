# Project Tasks

This document tracks ongoing improvements and fixes for the taxes project documentation and structure.

## Current Tasks

### Documentation Consistency Issues

- [ ] **Task 4: Clarify stage numbering** - Decide on 3 or 4 stages and be consistent across all documentation
- [ ] **Task 5: Create placeholder directories** - Add `generated-files/final/` with explanatory README
- [ ] **Task 6: Remove hardcoded paths** - Replace `/Users/beau/Projects/taxes` with relative paths or placeholders in CLAUDE.md

## Completed Tasks

- [x] **Task 1: Standardize CSV format** - Migrated from Deposits/Withdrawals to single Amount column (negative for expenses, positive for income)
  - Converted all 16 existing CSV files (14 extracted + 2 merged)
  - Updated all conversion scripts (fix_wells_fargo_schema.py, convert_privacy_com_to_standard_csv.py, merge_all_csvs.py)
  - Updated documentation (README.md, CLAUDE.md, scripts/README.md)
- [x] **Task 2: Fix path references** - Updated all path references in SOURCE_TRACKING.md
  - Changed all instances of `extracted-data/` to `generated-files/extracted/`
  - All 14 file path references updated
- [x] **Task 3: Add Source column** - Added Source field to standard format across all docs and files
  - Source column now included in all CSVs for audit trail and deduplication
  - Updated all conversion scripts to populate Source field
  - Documentation updated to reflect new column

---

## Notes

- Update this file as tasks are completed
- Add new tasks as they are identified
- Check off tasks using `[x]` when complete
