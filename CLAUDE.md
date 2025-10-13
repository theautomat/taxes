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

### CSV Format Standards - Extraction Phase
Focus on getting data out of PDFs first. Categorization comes later.

**Required columns for initial extraction:**
- **Date** (YYYY-MM-DD format)
- **Description** (original transaction description - keep it exactly as shown)
- **Amount** (negative for expenses/debits, positive for income/credits)
- **Source** (original source document filename, e.g., "022822 WellsFargo.pdf")
- **Notes** (optional - only for clarifications or questions)

**Optional columns (useful for verification):**
- **Balance** (ending daily balance - helps verify extraction accuracy)

**Note:** Business/Personal classification, detailed categorization, and deductibility will be added in a later phase after all documents are extracted.

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
- **Always include Source field** with original document filename for audit trail
- **Keep duplicates initially** - deduplication happens in a later phase (see DEDUPLICATION.md)

## Bookkeeping & Tax Preparation

### Goal
Convert unstructured financial data into organized transactions that can be:
1. Reconciled across multiple sources
2. Deduplicated to avoid double-counting
3. Categorized for tax purposes
4. Filtered to tax-relevant transactions only
5. Delivered to accountant in easy-to-digest format

### What Your Accountant Needs

**Business Income:**
- Wire transfers from clients/companies
- Payroll deposits
- 1099 income
- Business revenue from any source

**Business Deductions (Common Categories):**
- Office expenses: Software subscriptions, SaaS services
- Professional services: Hosting, domains, cloud services
- Home office: Utilities (business portion), internet
- Vehicle expenses: Auto payments, gas (business use percentage)
- Business meals: 50% deductible
- Equipment: Computer hardware, office furniture
- Storage: Business-related storage fees
- Professional development: Courses, training, subscriptions
- Banking fees: Wire transfer fees, business account fees

**NOT Needed for Tax Filing:**
- Personal groceries, personal shopping
- Personal entertainment (unless documented business purpose)
- Credit card payments (the underlying expenses are what matter)
- Internal transfers between your own accounts
- Ending balances (useful for reconciliation only)

### Business vs Personal Classification

**Business:** Expenses directly related to business operations
**Personal:** Personal living expenses, non-business purchases
**Mixed:** Items used for both (document business use percentage in Notes)

### Deductibility Guidelines

**Yes:** Clearly business expense, fully deductible
**No:** Personal expense, not deductible
**Partial:** Mixed use, or limited deductibility (e.g., meals at 50%)
**Unknown:** Needs clarification or research

Document reasoning in Notes field when unclear.

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
