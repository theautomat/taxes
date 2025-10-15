# Git Worktrees Workflow for Parallel Development

## Quick Start

**Create a worktree for a new task:**
```bash
cd ~/Projects/taxes
git worktree add ../taxes-feat-your-feature -b feature/your-feature main
code ../taxes-feat-your-feature
```

**List all worktrees:**
```bash
git worktree list
```

**Clean up when done:**
```bash
git worktree remove ../taxes-feat-your-feature
git branch -d feature/your-feature
```

## What Are Git Worktrees?

Git worktrees let you have multiple branches checked out simultaneously in separate directories. Each worktree is a complete working copy of your repository, but they all share the same Git history.

## The Manager Pattern (Key Concept!)

**Understanding roles is critical to using worktrees correctly:**

```
┌─────────────────────────────────────────────────────────────────┐
│ MAIN DIRECTORY = "Manager" / Coordination Hub                   │
├─────────────────────────────────────────────────────────────────┤
│ ~/Projects/taxes/                                               │
│                                                                 │
│ Purpose:                                                        │
│ • Create new worktrees (spawn workers)                          │
│ • Merge completed work                                          │
│ • Coordinate between branches                                   │
│ • NO active development happens here                            │
│                                                                 │
│ The "manager" can run git checkout safely because               │
│ nobody is actively working in this directory!                   │
└─────────────────────────────────────────────────────────────────┘
                            │
                            │ Creates worktrees
                            ↓
┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐
│ WORKTREE 1       │  │ WORKTREE 2       │  │ WORKTREE 3       │
├──────────────────┤  ├──────────────────┤  ├──────────────────┤
│ taxes-feat-dedup │  │ taxes-docs-wf    │  │ taxes-fix-bug    │
│                  │  │                  │  │                  │
│ Claude Session 1 │  │ Claude Session 2 │  │ Developer        │
│ Active work      │  │ Active work      │  │ Active work      │
│ NEVER leaves dir │  │ NEVER leaves dir │  │ NEVER leaves dir │
│ NEVER git checkout│ │ NEVER git checkout│ │ NEVER git checkout│
└──────────────────┘  └──────────────────┘  └──────────────────┘
```

### The Golden Rules

1. **Main Directory (Manager):**
   - Can run `git checkout` freely ✓
   - No active development work ✓
   - Used only for coordination ✓
   - Creates worktrees ✓
   - Merges completed work ✓

2. **Worktrees (Workers):**
   - NEVER run `git checkout` ✗
   - Each locked to one branch forever ✓
   - All active work happens here ✓
   - Each terminal/session stays in its worktree ✓

### Why This Eliminates Context Switching

```
WRONG (Traditional): Everyone works in ~/Projects/taxes/
───────────────────────────────────────────────────────
Terminal 1: ~/Projects/taxes (feature-a)
Terminal 2: ~/Projects/taxes (feature-a) ← Same directory!

Terminal 1 runs: git checkout main
Terminal 2: OH NO! Now on main too! Context lost!

RIGHT (Manager Pattern): Workers in separate directories
──────────────────────────────────────────────────────
Terminal 1: ~/Projects/taxes-feat-a (feature-a)
Terminal 2: ~/Projects/taxes-feat-b (feature-b)
Terminal 3: ~/Projects/taxes (manager - coordination only)

Terminal 3 runs: git checkout main
Terminal 1: Still on feature-a! ✓
Terminal 2: Still on feature-b! ✓
No context lost!
```

### Traditional vs Worktree Workflow

**Traditional (Context Switching Tax):**
```
1. Working on feature A
2. Bug report comes in
3. git stash (lose context)
4. git checkout main
5. git checkout -b hotfix
6. Fix bug (Claude needs to rebuild context)
7. git checkout feature-a
8. git stash pop
9. Re-explain everything to Claude
```

**With Worktrees (Zero Context Loss):**
```
Terminal 1: Working on feature A → keeps working
Terminal 2: cd ../taxes-hotfix → fix bug immediately
           Claude has full context in both terminals
```

## Directory Structure

```
~/Projects/
├── taxes/                          # Main repository (any branch)
│   ├── .git/                      # Shared Git database
│   ├── scripts/
│   ├── generated-files/
│   └── docs/
│
├── taxes-feat-extraction/         # Worktree 1
│   ├── .git → ../taxes/.git      # Link to shared Git
│   └── [feature/pdf-extraction]
│
├── taxes-fix-dedup-bug/           # Worktree 2
│   ├── .git → ../taxes/.git      # Link to shared Git
│   └── [hotfix/dedup-amounts]
│
└── taxes-docs-worktree/           # Worktree 3
    ├── .git → ../taxes/.git       # Link to shared Git
    └── [docs/worktree-workflow]
```

## Complete Workflow Example (Manager Pattern)

### Scenario: You're working on PDF extraction when a bug report arrives

**Phase 1: Manager creates feature worktree**
```bash
# Terminal 1: Manager (coordination)
cd ~/Projects/taxes
git checkout main
git pull

# Create worktree for feature work
git worktree add ../taxes-feat-extraction -b feature/pdf-extraction main
code ../taxes-feat-extraction
```

**Phase 2: Worker does feature work**
```bash
# Terminal 2: Worker (active development in worktree)
cd ~/Projects/taxes-feat-extraction
# STAYS IN THIS DIRECTORY
# NEVER runs git checkout

# Work on feature
# Edit files, test, iterate
git add -A
git commit -m "feat: add PDF extraction"
git push --set-upstream origin feature/pdf-extraction
```

**Phase 3: Bug report arrives! Manager creates hotfix worktree**
```bash
# Terminal 1: Manager (coordination)
cd ~/Projects/taxes
# Can safely run git checkout - no workers in this directory!
git checkout main

# Create worktree for hotfix
git worktree add ../taxes-hotfix-amounts -b hotfix/amount-parsing main
code ../taxes-hotfix-amounts
```

**Phase 4: Another worker fixes bug (parallel to Terminal 2!)**
```bash
# Terminal 3: Worker (active development in worktree)
cd ~/Projects/taxes-hotfix-amounts
# STAYS IN THIS DIRECTORY
# NEVER runs git checkout

# Fix the bug
git add -A
git commit -m "fix: correct amount parsing"
git push --set-upstream origin hotfix/amount-parsing

# Terminal 2 is STILL working on feature-extraction!
# Zero context lost! No interference!
```

**Phase 5: Manager merges completed work**
```bash
# Terminal 1: Manager (coordination)
cd ~/Projects/taxes
git checkout main  # Safe! No workers in this directory
git merge hotfix/amount-parsing
git push

# Clean up
git worktree remove ../taxes-hotfix-amounts
git branch -d hotfix/amount-parsing
```

**Phase 6: Feature work continues undisturbed**
```bash
# Terminal 2: Worker (still in worktree)
cd ~/Projects/taxes-feat-extraction
# Never stopped working!
# Never lost context!
# Continues development with full Claude Code context
```

**Phase 7: Feature complete, manager merges**
```bash
# Terminal 2: Worker finishes
cd ~/Projects/taxes-feat-extraction
git add -A
git commit -m "feat: PDF extraction complete"
git push

# Terminal 1: Manager merges
cd ~/Projects/taxes
git checkout main
git merge feature/pdf-extraction
git push

# Clean up
git worktree remove ../taxes-feat-extraction
git branch -d feature/pdf-extraction
```

## Manager Pattern: Starting a New Feature

When you want to start a new feature, always begin from the **Manager** (main directory):

```bash
# Step 1: Open terminal in Manager directory
cd ~/Projects/taxes

# Step 2: Get latest code
git checkout main
git pull

# Step 3: Check what worktrees exist
git worktree list

# Step 4: Create new worktree for your feature
git worktree add ../taxes-feat-your-feature -b feature/your-feature main

# Step 5: Open in new Claude Code window
code ../taxes-feat-your-feature

# Step 6: Manager terminal can now:
#  - Create more worktrees
#  - Merge completed work
#  - Check status
#  - Stay on any branch (doesn't matter - nobody's working here)
```

**Key insight:** Nobody works in the main directory, so it's free to coordinate between branches!

## Naming Conventions

Use descriptive prefixes:

| Prefix | Purpose | Example |
|--------|---------|---------|
| `taxes-feat-*` | New feature | `taxes-feat-pdf-extraction` |
| `taxes-fix-*` | Bug fix | `taxes-fix-dedup-bug` |
| `taxes-exp-*` | Experiment | `taxes-exp-llm-categories` |
| `taxes-docs-*` | Documentation | `taxes-docs-worktree` |
| `taxes-test-*` | Testing changes | `taxes-test-new-dedup-algo` |

## Common Commands

### Creating Worktrees

```bash
# New branch from main
git worktree add ../taxes-feat-name -b feature/name main

# New branch from current branch
git worktree add ../taxes-feat-name -b feature/name HEAD

# Existing branch (must not be checked out elsewhere)
git worktree add ../taxes-feat-name existing-branch
```

### Managing Worktrees

```bash
# List all worktrees with branches
git worktree list

# Remove a worktree (directory must be clean)
git worktree remove ../taxes-feat-name

# Force remove (even with uncommitted changes)
git worktree remove --force ../taxes-feat-name

# Clean up deleted worktrees
git worktree prune
```

### Branch Management

```bash
# After merging, delete branch
git branch -d feature/name

# Force delete unmerged branch
git branch -D feature/name

# Check which branches are merged
git branch --merged main
```

## Best Practices

### 1. One Worktree Per Task
Don't create too many worktrees. Each one uses disk space and mental overhead.

**Good:**
- Feature A worktree
- Hotfix B worktree
- Experiment C worktree

**Bad:**
- 10+ worktrees with unclear purposes

### 2. Clean Up Regularly
After merging, immediately remove the worktree:

```bash
# After successful merge
git worktree remove ../taxes-feat-name
git branch -d feature/name
```

### 3. Use Descriptive Names
Future you will thank you:

```bash
# Good
taxes-feat-pdf-extraction
taxes-fix-dedup-amounts

# Bad
taxes-temp
taxes-test
taxes-1
```

### 4. Check Status Before Removal
```bash
cd ~/Projects/taxes-feat-name
git status  # Make sure everything is committed

cd ~/Projects/taxes
git worktree remove ../taxes-feat-name
```

### 5. Share Dependencies When Possible
```bash
# Python virtual environment
source ~/Projects/taxes-venv/bin/activate  # Works in any worktree

# Avoid duplicating large dependencies
```

## Troubleshooting

### Error: "fatal: 'branch' is already checked out"
**Problem:** Trying to create a worktree for a branch that's already checked out.

**Solution:**
```bash
# Find where it's checked out
git worktree list

# Remove the old worktree first
git worktree remove /path/to/old/worktree

# Or force it
git worktree add --force ../new-location existing-branch
```

### Error: "fatal: cannot remove a locked working tree"
**Problem:** Worktree is locked (usually because it's in use).

**Solution:**
```bash
# Unlock it
git worktree unlock /path/to/worktree

# Then remove
git worktree remove /path/to/worktree
```

### Can't find my worktree
**Problem:** Lost track of worktrees.

**Solution:**
```bash
# List all worktrees with full paths
git worktree list

# Clean up deleted worktrees
git worktree prune
```

### Disk space running low
**Problem:** Multiple worktrees using too much space.

**Solution:**
```bash
# Remove unused worktrees
git worktree remove ../taxes-old-feature

# Share dependencies across worktrees
# Use symbolic links for large read-only directories

# Or just work with fewer worktrees at once
```

## Integration with Claude Code

### Why Worktrees Are Powerful with Claude Code

1. **Context Preservation**: Each Claude session maintains full understanding
2. **No Re-explanation**: Claude doesn't need to rebuild context after switching
3. **Parallel Problem Solving**: Multiple Claude sessions work independently
4. **Safe Experimentation**: Create experimental worktree, let Claude try approaches

### Example: Comparing Two Approaches

```bash
# Approach A: Traditional deduplication
git worktree add ../taxes-exp-traditional -b experiment/traditional-dedup main
code ../taxes-exp-traditional

# Approach B: ML-based deduplication
git worktree add ../taxes-exp-ml -b experiment/ml-dedup main
code ../taxes-exp-ml

# Give both Claude sessions the same spec
# See which approach works better
# Merge the winner, delete the loser
```

### Example: Safe Refactoring

```bash
# Keep current working version
cd ~/Projects/taxes  # main branch, working code

# Try major refactoring in worktree
git worktree add ../taxes-refactor -b refactor/script-rewrite main
code ../taxes-refactor

# If refactoring fails, just delete the worktree
# Main code is untouched
```

## Automation Scripts

### Quick Worktree Creation Script

Save as `scripts/create-worktree.sh`:

```bash
#!/bin/bash
# Usage: ./scripts/create-worktree.sh feature-name

if [ $# -eq 0 ]; then
    echo "Usage: $0 <feature-name>"
    exit 1
fi

FEATURE_NAME=$1
WORKTREE_PATH="../taxes-feat-${FEATURE_NAME}"
BRANCH_NAME="feature/${FEATURE_NAME}"

git worktree add "${WORKTREE_PATH}" -b "${BRANCH_NAME}" main
echo "Created worktree: ${WORKTREE_PATH}"
echo "Branch: ${BRANCH_NAME}"
echo "Opening in VS Code..."
code "${WORKTREE_PATH}"
```

### Cleanup Merged Worktrees Script

Save as `scripts/cleanup-worktrees.sh`:

```bash
#!/bin/bash
# Remove worktrees for branches that have been merged to main

echo "Finding merged branches..."

git worktree list | grep -v "$(git rev-parse --show-toplevel)" | while read path branch rest; do
    branch_name=$(echo $branch | tr -d '[]')

    # Check if merged to main
    if git branch --merged main | grep -q "$branch_name"; then
        echo "Removing merged worktree: $path ($branch_name)"
        git worktree remove "$path"
        git branch -d "$branch_name"
    fi
done

echo "Cleanup complete!"
```

## Summary

Git worktrees enable true parallel development with Claude Code:
- **No context switching** - Each session maintains full context
- **Safe experimentation** - Create, test, delete without affecting main work
- **Parallel bug fixes** - Fix urgent issues without losing feature work
- **Improved velocity** - Multiple tasks progress simultaneously

Remember: A worktree is just a checked-out branch in a separate directory. All worktrees share the same Git history. Commits made in any worktree are visible everywhere.
