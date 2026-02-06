# Accounting Assistant Instructions

## ⚠️ Important: Keeping This File Concise

**This file is loaded into every conversation's initial context.** Large files consume tokens and reduce conversation length.

**Guidelines:**
- Keep instructions SHORT and CONCISE
- Link to detailed docs in `docs/` rather than duplicating content
- Use bullet points, not paragraphs
- Remove outdated or redundant information

**Quick Updates:**
- **Use `#` shortcut:** Type `#` followed by your instruction to quickly add memories
- **Use `/memory` command:** Opens this file in your editor for larger edits
- **When editing:** Always remind the user they can use `#` for quick additions instead of manual edits

## Role
You are an accounting assistant helping to organize and process financial documents. Your primary task is to convert unstructured financial data (PDFs, statements, receipts) into clean, normalized CSV files that accountants can easily work with.

### Taxpayer Context (2022 Tax Year)
**Key Facts:**
- Single filer, software developer, age 43, California resident (Fillmore, CA)
- Dual income: W-2 ($275k from NFT Genius) + S-Corp ($165k from Popstand Inc.)
- Total income: ~$440k (35% federal + 9.3% CA + 0.9% Medicare = 45.3% combined marginal rate)
- Home office setup: Primary home office in Fillmore + temporary Pasadena office (Oct-Dec 2022)
- Filing 3 years late (2025) with estimated penalties $50-80k
- **Every $1,000 deduction saves $453 in taxes**

**S-Corp Concern:** Popstand paid no W-2 wages to owner (all distributions) - potential IRS reasonable compensation issue

**Detailed Profile:** See `personal/2022/generated-files/deductions/2022-taxpayer-financial-profile.md` for comprehensive tax research and deduction opportunities

## Project Structure

### Repository Layout
```
taxes/
├── personal/
│   ├── <year>/
│   │   ├── source-documents/   (wells-fargo/, coinbase/, etc.)
│   │   └── generated-files/    (extracted/, merged/, final/, deductions/)
│   └── shared/                 (property-taxes/, estate-probate/)
├── automatique-inc/            (S-Corp tax files)
├── scripts/
├── docs/
└── CLAUDE.md, README.md, TASKS.md
```

- Repository name: `taxes`
- Working directory: `/Users/beau/Projects/taxes`
- Each tax year lives under `personal/<year>/`
- Active years: 2020, 2021, 2022, 2023, 2024 (2022 is most complete)

### Four-Stage Pipeline

All paths below are relative to `personal/<year>/`.

**Stage 1: Source Documents**
- `source-documents/` - Original financial documents (PDFs, images, etc.)
  - Organized by institution (e.g., `wells-fargo/`, `coinbase/`)
  - Track processing status in `docs/SOURCE_TRACKING.md`

**Stage 2: Extraction**
- `generated-files/extracted/` - Raw data converted to standardized CSV
  - One CSV per source document, format: `YYYY-MM_source_type.csv`
  - Pure data extraction - no categorization yet

**Stage 3: Merged**
- `generated-files/merged/` - Combined data from all extracted files
  - Contains duplicates (deduplication happens in final stage)
  - Sorted by date, timestamped files for tracking merge runs

**Stage 4: Final**
- `generated-files/final/` - Deduplicated, categorized data ready for accountant
  - Business/Personal classification, tax categories assigned
  - Only tax-relevant transactions included

### Workflow
1. Source documents collected and stored in Google Drive
2. Download documents to `personal/<year>/source-documents/`
3. **Extract:** Convert source documents to standardized CSV → save to `personal/<year>/generated-files/extracted/`
   - PDFs, CSVs, receipt images → standardized CSV format
4. Update `docs/SOURCE_TRACKING.md` to mark document as processed
5. Commit extracted data to git
6. **Merge:** Combine all extracted CSVs → save to `personal/<year>/generated-files/merged/`
7. **Process:** Deduplicate, categorize → save to `personal/<year>/generated-files/final/`
8. **Deliver:** Final data to accountant

**Current Phase:** Stage 2 (Extraction) - Focus on getting all source documents into standardized CSV format

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
- **Keep duplicates initially** - deduplication happens in a later phase (see docs/DEDUPLICATION.md)

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

## Code Development Principles

### Write Reusable, Maintainable Code
- **Never write disposable code** - Always create scripts that can be reused
- **Add validation and checks** - Scripts should verify their own output and report issues
- **Improve existing scripts** - When a script needs modification, enhance it rather than writing throwaway commands
- **Self-documenting output** - Scripts should print clear status messages and results
- **Save all scripts** - Store utility scripts in `scripts/` directory for future use

Examples:
- Instead of one-off bash commands to check data, add validation to the processing script
- Instead of manual verification, build automated checks into the workflow
- Instead of ad-hoc queries, create reusable analysis scripts

## Version Control

### Git Workflow Requirements
**CRITICAL: A task is not complete until ALL of the following are done:**

1. **Commit everything** - All generated files, scripts, and documentation
2. **Check git status** - Verify working tree is clean (no red untracked files)
3. **Push to remote** - Changes must be on the server, not just local
4. **Verify nothing is gitignored accidentally** - Even gitignored files shouldn't show up as untracked

**Completion Checklist:**
```bash
# Before declaring a task complete:
git status           # Should show "working tree clean"
git push            # Push all commits to remote
git status          # Verify push succeeded
```

**Never say "task complete" if:**
- Files are untracked (showing in red in git status)
- Commits are not pushed to remote
- Working directory has uncommitted changes

### Commit Guidelines
- Make frequent, atomic commits for each processed document
- Clear commit messages describing what was processed
- Use conventional commit format when applicable:
  - `feat: add Jan 2022 Wells Fargo statement`
  - `fix: correct amount in Dec 2021 transaction`
  - `docs: update processing instructions`
- **DO NOT include Claude Code branding in commit messages** - No "Generated with Claude Code" footers or "Co-Authored-By: Claude" tags

### What NOT to Commit
- **Claude Code local settings** - `.claude/settings.local.json` is user-specific and should be gitignored
- **Source documents** - PDFs and financial documents are tracked in git for sync across machines
- **Temporary files** - Any `.tmp`, `.swp`, or cache files

## Git Worktrees for Parallel Development

Git worktrees allow you to work on multiple branches simultaneously without context switching. This is especially powerful with Claude Code because each worktree maintains its own session context.

**Quick Start:**
```bash
# Create worktree for new feature
cd ~/Projects/taxes
git worktree add ../taxes-feat-name -b feature/name main

# List all worktrees
git worktree list

# Remove when done
git worktree remove ../taxes-feat-name
```

**When to use worktrees:**
- Working on multiple features simultaneously
- Quick bug fix without losing current work
- Experimenting with major changes
- Comparing different approaches side-by-side

**For comprehensive worktree documentation, see:** `docs/WORKTREE_WORKFLOW.md`

## Setup on New Machine
1. Clone repository
2. Create `personal/<year>/source-documents/` folders as needed
3. Download documents from Google Drive to appropriate year folders
4. Ready to process documents

## Conversation History Management

### Saving Conversations
Claude Code conversations contain valuable context about decisions made, problems solved, and work completed. Save important conversations for future reference.

**When to save conversations:**
- Before using `/clear` to clear conversation history
- Before using `/compact` to compact the conversation
- After completing significant work or making important decisions
- When the conversation contains troubleshooting steps or solutions
- Any time you want to preserve the context for later reference

**How to save:**
1. Use `/save` command in Claude Code to export the conversation
2. Save the file to `claude-conversations/` directory
3. Use descriptive filenames: `YYYY-MM-DD-brief-description.txt`

**Directory structure:**
```
claude-conversations/
  ├── 2025-10-21-pdf-extraction-troubleshooting.txt
  ├── 2025-10-20-deduplication-implementation.txt
  └── 2025-10-15-initial-project-setup.txt
```

**Best practices:**
- Save conversations BEFORE clearing or compacting (once cleared, history may not be easily accessible via `/resume`)
- Use descriptive names that explain what was discussed/accomplished
- Conversations are versioned in git for backup and sharing across machines
- Review saved conversations when resuming work on related tasks

## Google Drive Sync
- Source documents location: [To be specified by user]
- Download documents to `personal/<year>/source-documents/` (organized by tax year)
- Keep Google Drive as source of truth for original documents
- No need to organize files in Drive - just store them safely
