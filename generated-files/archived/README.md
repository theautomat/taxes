# Archived Files

This directory contains previous versions of generated files that have been superseded by improved extractions or processing.

## Purpose

Archives are kept for:
- Performance comparison (comparing vision extraction accuracy)
- Historical reference
- Rollback capability if needed
- Audit trail

## Archive Format

Archives are organized by date and reason:
```
archived/
├── YYYY-MM-DD_reason/
│   ├── README.md              # Description of what was archived and why
│   └── [archived files]
```

## Current Archives

### 2025-10-14_pre-reextraction/
**Reason:** Wells Fargo 2022 statements being re-extracted with improved process

The initial extraction had sign errors (positive/negative amounts) due to manual extraction without formal process. A comprehensive extraction process document was created (`docs/WELLS_FARGO_EXTRACTION_PROCESS.md`) and all 12 months are being re-extracted for accuracy.

**Files archived:**
- All 12 Wells Fargo checking CSV files (Jan-Dec 2022)
- Merged files that included Wells Fargo data
- Deduplicated files that included Wells Fargo data

**Known issues in archived files:**
- Some wire transfers have incorrect signs (e.g., legal fees marked as income)
- Inconsistent handling of deposits vs withdrawals sections

---

## Notes for Scripts

**Scripts should NOT access archived files** - they are kept for reference only. All active processing should use files in:
- `generated-files/extracted/` (current extractions)
- `generated-files/merged/` (current merged data)
- `generated-files/merged-deduped/` (current deduplicated data)
