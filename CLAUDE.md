# Accounting Assistant Instructions

## Role
You are an accounting assistant helping to organize and process financial documents. Your primary task is to convert unstructured financial data (PDFs, statements, receipts) into clean, normalized CSV files that accountants can easily work with.

## Project Structure

### Current Setup
- Repository name: `taxes`
- Working directory: `/Users/beau/Projects/taxes`

### Three-Stage Pipeline

**Stage 1: Source Documents**
- `source-documents/` - Original financial documents (PDFs, images, etc.)
  - NOT versioned in git (gitignored - files can be large)
  - Synced with Google Drive for backup
  - Local copy refreshed periodically from Google Drive
  - Track which documents have been processed in `docs/SOURCE_TRACKING.md`

**Stage 2: Generated Files - Extraction**
- `generated-files/extracted/` - Raw data converted to standardized CSV format
  - Versioned in git
  - Pure data extraction - no categorization yet
  - One CSV per source document (regardless of original format)
  - Format: `YYYY-MM_source_type.csv`
  - Sources can be: PDFs, existing CSVs, images of receipts, screenshots, etc.
  - Purpose: Get all financial data into consistent CSV format quickly

**Stage 3: Generated Files - Merged**
- `generated-files/merged/` - Combined data from all extracted files
  - Versioned in git
  - Contains duplicates (deduplication happens in final stage)
  - Sorted by date
  - Timestamped files for tracking different merge runs
  - Purpose: Single file containing all transactions for review

**Stage 4: Generated Files - Final**
- `generated-files/final/` - Processed, categorized, deduplicated data ready for accountant
  - Versioned in git
  - Transactions deduplicated across sources
  - Business/Personal classification added
  - Tax categories assigned
  - Only tax-relevant transactions included
  - Purpose: Clean data ready for tax preparation

### Workflow
1. Source documents collected and stored in Google Drive
2. Download documents to `source-documents/`
3. **Extract:** Convert source documents to standardized CSV → save to `generated-files/extracted/`
   - PDFs → extract transaction tables
   - Existing CSVs → reformat to standard columns if needed
   - Receipt images → extract date, merchant, amount
   - Any financial data → standardized CSV format
4. Update `docs/SOURCE_TRACKING.md` to mark document as processed
5. Commit extracted data to git
6. **Merge:** (Later phase) Combine all extracted CSVs → save to `generated-files/merged/`
7. **Process:** (Later phase) Deduplicate, categorize → save to `generated-files/final/`
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
- **Source documents** - Already gitignored, never commit PDFs or sensitive financial documents
- **Temporary files** - Any `.tmp`, `.swp`, or cache files

## Git Worktrees for Parallel Development

### Why Use Worktrees?
Git worktrees allow you to work on multiple branches simultaneously without losing context. This is especially powerful with Claude Code because:

1. **Context Preservation**: Each Claude Code session maintains full understanding of the codebase in its worktree
2. **No Context Switching**: Switch between tasks without `git stash` or losing your place
3. **Parallel Work**: Multiple Claude sessions can work on different features simultaneously
4. **Zero Risk**: Impossible to accidentally commit to the wrong branch

### Understanding Worktrees
A worktree is a separate working directory linked to the same Git repository:

```
~/Projects/taxes/                    # Main directory (any branch)
  ├── .git/                         # Shared Git repository
  ├── scripts/
  ├── generated-files/
  └── docs/

~/Projects/taxes-feature-dedup/     # Worktree for deduplication work
  ├── .git                          # → Links to main .git
  ├── scripts/                      # Independent file states
  └── [on branch: feature/deduplication]

~/Projects/taxes-docs-worktree/     # Worktree for documentation
  ├── .git                          # → Links to main .git
  ├── docs/                         # Independent file states
  └── [on branch: docs/worktree-workflow]
```

**Key Benefits:**
- All worktrees share the same Git history (commits, branches, remotes synchronized)
- Each worktree has independent file states (no conflicts between tasks)
- Changes committed in any worktree are visible in all worktrees

### Basic Worktree Commands

**Create a new worktree:**
```bash
# Create worktree in parent directory with new branch
git worktree add ../taxes-feature-name -b feature/feature-name main

# Create worktree in current directory's subdirectory
git worktree add taxes-feature-name -b feature/feature-name main
```

**List all worktrees:**
```bash
git worktree list
```

**Remove a worktree:**
```bash
# After merging and no longer needed
git worktree remove ../taxes-feature-name
git branch -d feature/feature-name  # Delete the branch
```

**Clean up merged worktrees:**
```bash
# Prune references to deleted worktrees
git worktree prune
```

### Recommended Workflow

**1. Create Worktree for New Task:**
```bash
# From main repo directory
cd ~/Projects/taxes

# Create worktree for feature work
git worktree add ../taxes-feature-extraction -b feature/pdf-extraction main

# Open in new Claude Code window
code ../taxes-feature-extraction
```

**2. Work in Isolation:**
- Each Claude Code session maintains full context
- Make commits as normal (`git add`, `git commit`, `git push`)
- No interference with other worktrees

**3. Complete and Merge:**
```bash
# When feature is ready
cd ~/Projects/taxes-feature-extraction
git add -A
git commit -m "feat: implement PDF extraction pipeline"
git push --set-upstream origin feature/pdf-extraction

# Switch to main repo and merge
cd ~/Projects/taxes
git checkout main
git merge feature/pdf-extraction

# Clean up
git worktree remove ../taxes-feature-extraction
git branch -d feature/pdf-extraction
```

### Worktree Naming Convention
Use descriptive names that indicate the purpose:

**Good names:**
- `taxes-feat-pdf-extraction` - Feature: PDF extraction
- `taxes-fix-dedup-bug` - Bugfix: Deduplication bug
- `taxes-docs-worktree` - Documentation: Worktree guide
- `taxes-exp-llm-categorize` - Experiment: LLM categorization

**Bad names:**
- `taxes-temp`, `taxes-test`, `taxes-1` - Not descriptive

### Parallel Development Example
```bash
# Terminal 1: Work on deduplication improvements
cd ~/Projects/taxes-feature-dedup

# Terminal 2: Work on PDF extraction enhancements
cd ~/Projects/taxes-feature-extraction

# Terminal 3: Fix urgent bug in merged data
cd ~/Projects/taxes-hotfix-merge

# Each has its own Claude Code session with full context
# No git stash, no context switching, no lost work
```

### When to Use Worktrees

**Use worktrees when:**
- Working on multiple features simultaneously
- Need to quickly switch to fix a bug without losing current work
- Experimenting with major changes (safe to delete if it fails)
- Comparing different implementations side-by-side
- Running tests on one branch while developing on another

**Don't use worktrees when:**
- Quick fixes that take < 5 minutes
- Simple single-task workflows
- Disk space is very limited (each worktree duplicates working files)

### Disk Space Considerations
Worktrees duplicate working files but share Git history:
- Main `.git` directory: ~shared~
- Working files per worktree: ~duplicated~
- Dependencies (node_modules, venv): ~duplicated per worktree~

**Optimization tip:** Share virtual environments across worktrees if dependencies are identical:
```bash
# Use the same Python venv
source ~/Projects/taxes-venv/bin/activate  # Works in any worktree
```

## Setup on New Machine
1. Clone repository
2. Create `source-documents/` folder (will be empty due to gitignore)
3. Download latest documents from Google Drive to `source-documents/`
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
- Download all PDFs and documents to `source-documents/` folder
- Keep Google Drive as source of truth for original documents
- No need to organize files in Drive - just store them safely
