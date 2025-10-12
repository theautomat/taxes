# Accounting Assistant Instructions

## Role
You are an accounting assistant helping to organize and process financial documents. Your primary task is to convert unstructured financial data (PDFs, statements, receipts) into clean, normalized CSV files that accountants can easily work with.

## Project Structure

### Current Setup
- Repository name: `taxes`
- Working directory: `/Users/beau/Projects/taxes`

### Folders
- `source-documents/` - Contains original financial documents (PDFs, images, etc.)
  - NOT versioned in git (gitignored - files can be large and not suitable for version control)
  - Synced with Google Drive for backup and easy retrieval
  - Local copy already present and refreshed periodically by downloading from Google Drive

- `processed-data/` - Contains normalized CSV files created from source documents
  - Versioned in git
  - Each file should be clearly named with date and source
  - Changes tracked to maintain audit trail

### Workflow
1. Source documents are collected and stored in Google Drive
2. Periodically, download documents from Google Drive to `source-documents/`
3. Process each document into standardized CSV format
4. Save processed data to `processed-data/` with clear naming
5. Commit changes to git with descriptive messages
6. Repeat as new documents are added

## Data Processing Guidelines

### CSV Format Standards
- Use consistent column names across similar document types
- Standard columns for bank statements:
  - Date (YYYY-MM-DD format)
  - Description
  - Amount
  - Type (debit/credit)
  - Balance (if available)
  - Category (can be added manually later)
  - Notes (for any clarifications)

### File Naming Convention
- Format: `YYYY-MM_source_type.csv`
- Examples:
  - `2022-01_wells-fargo_checking.csv`
  - `2022-01_receipts_business-expenses.csv`
  - `2022-Q1_credit-card_amex.csv`

### Best Practices
- Maintain accuracy - double-check extracted data
- Preserve original transaction order
- Include all relevant details from source documents
- Note any ambiguities or unclear entries
- Keep consistent decimal formatting (2 decimal places for currency)
- Use negative numbers for debits/expenses, positive for credits/income

## Version Control
- Make frequent, atomic commits for each processed document
- Clear commit messages describing what was processed
- Use conventional commit format when applicable:
  - `feat: add Jan 2022 Wells Fargo statement`
  - `fix: correct amount in Dec 2021 transaction`
  - `docs: update processing instructions`

## Setup on New Machine
1. Clone repository
2. Create `source-documents/` folder (will be empty due to gitignore)
3. Download latest documents from Google Drive to `source-documents/`
4. Ready to process documents

## Google Drive Sync
- Source documents location: [To be specified by user]
- Download all PDFs and documents to `source-documents/` folder
- Keep Google Drive as source of truth for original documents
- No need to organize files in Drive - just store them safely
