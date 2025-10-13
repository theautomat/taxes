# Taxes - Financial Document Processing

A system for converting unstructured financial documents (PDFs, receipts, statements) into clean, normalized CSV files for accounting purposes.

## Structure

```
taxes/
├── source-documents/           # Original unorganized source files (NOT versioned, synced with Google Drive)
├── generated-files/            # All generated/processed files (versioned in git)
│   ├── extracted/              # Stage 1: Raw CSV extractions from source documents
│   ├── merged/                 # Stage 2: Combined data with duplicates
│   └── final/                  # Stage 3: Clean, categorized, deduplicated data for accountant
├── scripts/                    # Processing and conversion scripts
├── docs/                       # Documentation files
│   ├── SOURCE_TRACKING.md      # Tracks which source documents have been processed
│   ├── DEDUPLICATION.md        # Strategy for handling duplicate transactions
│   └── CATEGORIES.md           # Reference guide for categorization
├── CLAUDE.md                   # Instructions for AI assistant
└── README.md                   # This file (project overview)
```

## Setup on New Machine

1. Clone this repository:
   ```bash
   git clone https://github.com/theautomat/taxes.git
   cd taxes
   ```

2. Create the `source-documents` folder:
   ```bash
   mkdir source-documents
   ```

3. Download source documents from Google Drive:
   - Location: [To be specified - update this with your Google Drive folder path]
   - Download all PDFs and documents to `source-documents/` folder

4. Ready to process documents!

## Three-Stage Workflow

### Stage 1: Collection (Source Documents)
- Collect financial documents in Google Drive
- Download to `source-documents/` folder locally
- Track documents in `docs/SOURCE_TRACKING.md`

### Stage 2: Extraction (Current Phase)
- Convert all source documents to standardized CSV → save to `generated-files/extracted/`
- Sources: PDFs, existing CSVs, receipt images, screenshots, etc.
- Focus: Get data into consistent format quickly, no categorization
- One CSV per source document (regardless of original format)
- **Check `scripts/` folder first** - conversion scripts may already exist
- Update `docs/SOURCE_TRACKING.md` when complete

### Stage 3: Processing (Future Phase)
- Combine all extracted CSVs → `generated-files/merged/`
- Deduplicate transactions across sources (see `docs/DEDUPLICATION.md`)
- Categorize for tax purposes (see `docs/CATEGORIES.md`)
- Filter to tax-relevant transactions only
- Save final clean data to `generated-files/final/` for accountant

## File Naming Convention

Processed CSV files follow this format: `YYYY-MM_source_type.csv`

Examples:
- `2022-01_wells-fargo_checking.csv`
- `2022-01_receipts_business-expenses.csv`
- `2022-Q1_credit-card_amex.csv`

## Standard CSV Format

All extracted data must conform to this structure:

```csv
Date,Description,Deposits,Withdrawals,Balance,Type,Category,Notes
```

**Column Definitions:**
- **Date**: Transaction date (YYYY-MM-DD format)
- **Description**: Transaction description
- **Deposits**: Money in (positive number, or empty)
- **Withdrawals**: Money out (positive number, or empty)
- **Balance**: Running balance (when available, otherwise empty)
- **Type**: Credit/Debit/Balance/Payroll
- **Category**: Transaction category (can be empty initially)
- **Notes**: Additional details, source file references, etc.

## Scripts

The `scripts/` directory contains automation tools for converting various source formats to the standard CSV format. Always check for existing scripts before manually extracting data - they save time and ensure consistency.

See `scripts/README.md` for available scripts and usage instructions.

## Source Documents

Source documents are **NOT** versioned in git because:
- They can be large PDF files
- Not practical to version binary files
- Original source of truth is Google Drive
- Local copy is refreshed as needed

## Version Control

This repository tracks:
- Processed CSV files
- Documentation and instructions
- Configuration files

Commits should be frequent and descriptive, documenting what was processed.
