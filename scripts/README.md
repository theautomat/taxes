# Scripts Directory

This folder contains scripts for processing and converting financial documents into standardized CSV format.

## Purpose

Scripts automate the extraction and conversion of financial data from various sources (bank statements, payment processors, payroll systems) into a unified CSV format that can be merged and analyzed.

## Standard CSV Format

All extracted data should conform to this column structure:

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
- **Category**: Transaction category (Food, Shopping, Payroll, etc.)
- **Notes**: Additional details, source file, pay periods, etc.

## Available Scripts

### `convert_privacy_com_to_standard_csv.py`
Converts Privacy.com transaction CSV exports to standardized format.

**Usage:**
```bash
python3 scripts/convert_privacy_com_to_standard_csv.py
```

**Input:** `source-documents/Privacy.com Transactions/Privacy.com Statement 2022-01-01 - 2022-12-31.csv`
**Output:** `generated-files/extracted/2022_privacy-com_transactions.csv`

**Note:** Privacy.com provides both PDF and CSV files. Only process the CSV files - they contain identical data and are much faster to process. PDFs should be skipped.

## Creating New Scripts

When creating new conversion scripts:

1. **Name clearly**: Use format `convert_[source]_to_standard_csv.py`
2. **Add documentation**: Include docstring explaining input/output
3. **Make executable**: `chmod +x scripts/script_name.py`
4. **Add to this README**: Document the script's purpose and usage
5. **Follow standard format**: Output must match the standard CSV structure above
6. **Use relative paths**: Scripts should work from project root

## Script Workflow

1. Read source document (CSV, PDF, etc.)
2. Parse and extract transaction data
3. Convert to standard CSV format
4. Output to `generated-files/extracted/` directory
5. Update `docs/SOURCE_TRACKING.md` to mark source as processed

## Tips for AI Assistants

- **Always check for existing scripts** before creating new extraction code
- **Reuse scripts** when possible - they may work for multiple years
- **Prefer CSV over PDF** when both formats are available
- Scripts in this directory are tested and follow project conventions
- Run scripts from the project root directory: `python3 scripts/script_name.py`
