# Taxes - Financial Document Processing

A system for converting unstructured financial documents (PDFs, receipts, statements) into clean, normalized CSV files for accounting purposes.

## Structure

```
taxes/
├── source-documents/     # Stage 1: Original PDFs/documents (NOT versioned, synced with Google Drive)
├── extracted-data/       # Stage 2: Raw CSV extractions (versioned in git)
├── final-data/           # Stage 3: Processed, deduplicated, categorized data for accountant (versioned in git)
├── SOURCE_TRACKING.md   # Tracks which source documents have been processed
├── CLAUDE.md            # Instructions for accounting assistant
├── DEDUPLICATION.md     # Strategy for handling duplicate transactions
├── CATEGORIES.md        # Reference guide for categorization
└── README.md            # This file
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
- Track documents in `SOURCE_TRACKING.md`

### Stage 2: Extraction (Current Phase)
- Convert all source documents to standardized CSV → save to `extracted-data/`
- Sources: PDFs, existing CSVs, receipt images, screenshots, etc.
- Focus: Get data into consistent format quickly, no categorization
- One CSV per source document (regardless of original format)
- Update `SOURCE_TRACKING.md` when complete

### Stage 3: Processing (Future Phase)
- Combine all extracted CSVs
- Deduplicate transactions across sources (see `DEDUPLICATION.md`)
- Categorize for tax purposes (see `CATEGORIES.md`)
- Filter to tax-relevant transactions only
- Save final clean data to `final-data/` for accountant

## File Naming Convention

Processed CSV files follow this format: `YYYY-MM_source_type.csv`

Examples:
- `2022-01_wells-fargo_checking.csv`
- `2022-01_receipts_business-expenses.csv`
- `2022-Q1_credit-card_amex.csv`

## CSV Format

Standard columns for bank statements:
- Date (YYYY-MM-DD format)
- Description
- Amount
- Type (debit/credit)
- Balance (if available)
- Category (optional, can be added later)
- Notes (for clarifications)

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
