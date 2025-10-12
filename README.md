# Taxes - Financial Document Processing

A system for converting unstructured financial documents (PDFs, receipts, statements) into clean, normalized CSV files for accounting purposes.

## Structure

```
taxes/
├── source-documents/     # Original PDFs/documents (NOT versioned, synced with Google Drive)
├── processed-data/       # Normalized CSV files (versioned in git)
├── CLAUDE.md            # Instructions for accounting assistant
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

## Workflow

1. **Collect**: Add new financial documents to Google Drive
2. **Sync**: Periodically download documents to `source-documents/`
3. **Process**: Use accounting assistant to convert PDFs to CSV
4. **Save**: Output goes to `processed-data/` with standardized naming
5. **Commit**: Frequent commits to track changes to processed data
6. **Repeat**: Continue as new documents are added

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
