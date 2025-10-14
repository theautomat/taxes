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

## Complete Workflow Example

### Scenario: You're working on PDF extraction when a bug report arrives

**Step 1: Create main feature worktree**
```bash
cd ~/Projects/taxes
git worktree add ../taxes-feat-extraction -b feature/pdf-extraction main
code ../taxes-feat-extraction
```

**Step 2: Work on feature with Claude**
```
Terminal 1 (Claude Code in taxes-feat-extraction):
- Implementing PDF extraction pipeline
- Full context maintained
- Making progress
```

**Step 3: Bug report arrives!**
```bash
# In Terminal 2
cd ~/Projects/taxes
git worktree add ../taxes-hotfix-amounts -b hotfix/amount-parsing main
code ../taxes-hotfix-amounts
```

**Step 4: Fix bug in parallel**
```
Terminal 2 (Claude Code in taxes-hotfix-amounts):
- Fix amount parsing bug
- Full context for the bug fix
- Independent of Terminal 1

Terminal 1 (Still running!):
- PDF extraction work continues
- No context lost
- No git stash needed
```

**Step 5: Complete and merge bug fix**
```bash
cd ~/Projects/taxes-hotfix-amounts
git add -A
git commit -m "fix: correct amount parsing in merge script"
git push --set-upstream origin hotfix/amount-parsing

cd ~/Projects/taxes
git merge hotfix/amount-parsing
git push

# Clean up
git worktree remove ../taxes-hotfix-amounts
git branch -d hotfix/amount-parsing
```

**Step 6: Continue feature work**
```bash
# Terminal 1 never stopped working!
# Just keep going with full context
```

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
