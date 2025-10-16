# Expenses Workflow

## Purpose
This directory is for isolating and researching potential business expenses from deduplicated transaction data. This is an iterative, ongoing process - not a one-time engineering task.

## Workflow Overview

```
Deduped/Merged Data → Research & Flagging → Expenses CSV → Review → Merge Back
```

### Stage 1: Source Data
- Start with deduplicated merged transactions
- Contains all transactions from all sources

### Stage 2: Research & Flagging
Multiple approaches to identify potential expenses:

1. **Manual Review** - Human eyeballing in spreadsheet
2. **AI-Assisted Flagging** - Scripts to flag probable expenses for review
3. **Pattern Matching** - Known software developer expense patterns
4. **Tax Code Research** - Documented potential deductions (see `2022_TAX_DEDUCTIONS.md`)

### Stage 3: Expenses CSV
- Isolated transactions flagged as potential business expenses
- Uses same CSV schema as merged data
- Includes confidence/source of flagging
- Awaits human review and validation

### Stage 4: Integration
Once validated:
- Option A: Merge expenses CSV back into main merged data with expense flags
- Option B: Edit merged CSV directly to add expense flags
- Goal: Have expense classification in the main dataset

## Current Phase
**Focus:** Building up the expenses CSV through various research methods
**Not worrying about:** Perfect automation or final integration yet

## Files in This Directory

### Research Inputs
- Deduped/merged transaction data (from `generated-files/merged/`)
- Manual expense research spreadsheets (added as needed)
- AI-flagged potential expenses

### Outputs
- `expenses_YYYY-MM-DD.csv` - Current working expense candidates
- Flags, notes, and confidence levels for review

### Documentation
- `2022_TAX_DEDUCTIONS.md` - Running list of potential tax breaks for 2022
- `EXPENSE_PATTERNS.md` - Common software developer expense patterns

## CSV Schema
Follows main schema with additions:

**Required columns:**
- Date (YYYY-MM-DD)
- Description
- Amount (negative for expenses)
- Source (original document)

**Additional expense columns:**
- **ExpenseCategory** - Type of business expense
- **Deductibility** - Yes/Partial/Unknown
- **FlaggedBy** - How this was identified (manual/ai/pattern/other)
- **Confidence** - High/Medium/Low
- **Notes** - Reasoning, questions, business purpose

## Iteration Strategy
This is designed for constant refinement:
1. Run scripts to flag new candidates
2. Add manual research findings
3. Review and validate batches
4. Update patterns and scripts based on learnings
5. Repeat

Nothing is fixed - adjust the process as needed.
