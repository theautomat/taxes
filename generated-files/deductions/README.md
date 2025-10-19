# Expenses Workflow & Tax Deduction Analysis

## Purpose
This directory serves two primary functions:
1. **Transaction-based expense research** - Identifying business expenses from transaction data
2. **Tax deduction analysis** - Breaking down major deduction categories with detailed calculations

## Directory Structure

```
expenses/
├── README.md                                    # This file
├── 2022_POTENTIAL_DEDUCTIONS_CHECKLIST.md      # Master brainstorming list of potential deductions
├── breakdowns/                                  # Detailed analysis for each deduction category
│   ├── BREAKDOWN_2022_Home_Office_Summary.md
│   ├── BREAKDOWN_2022_Home_Office_Calculation.md
│   ├── BREAKDOWN_2022_Depreciation_Recapture.md
│   ├── BREAKDOWN_2022_Mortgage_Interest_Federal_State.md
│   ├── BREAKDOWN_2022_Office_Expenses.md
│   └── [more breakdowns as created]
├── expense_patterns_whitelist.json    # High-confidence business expense patterns
├── expenses_template.csv               # Template for expense tracking
└── flagged_expenses_*.csv             # Auto-flagged expenses from scripts

scripts/
└── flag_expenses.py                    # Automated expense flagging script
```

---

## Part 1: Transaction-Based Expense Research

### Workflow Overview

```
Deduped/Merged Data → Research & Flagging → Expenses CSV → Review → Integrate
```

### Stage 1: Source Data
- Start with deduplicated merged transactions from `generated-files/merged/`
- Contains all transactions from all sources (Wells Fargo, Privacy.com, etc.)

### Stage 2: Research & Flagging
Multiple approaches to identify potential expenses:

1. **Automated Flagging** - `scripts/flag_expenses.py` using whitelist patterns
2. **Manual Review** - Human review in spreadsheet software
3. **Pattern Matching** - Known software developer expense patterns (GoDaddy, Heroku, GitHub, etc.)
4. **Tax Code Research** - Documented potential deductions (see `2022_TAX_DEDUCTIONS.md`)

### Stage 3: Expenses CSV
- Isolated transactions flagged as potential business expenses
- Uses same CSV schema as merged data plus expense-specific columns
- Includes confidence/source of flagging
- Awaits human review and validation

### Stage 4: Integration
Once validated:
- Option A: Merge expenses CSV back into main merged data with expense flags
- Option B: Edit merged CSV directly to add expense flags
- Goal: Have expense classification in the main dataset for final reporting

### CSV Schema
Follows main schema with additions:

**Required columns:**
- Date (YYYY-MM-DD)
- Description
- Amount (negative for expenses)
- Source (original document)

**Additional expense columns:**
- **ExpenseCategory** - Type of business expense (cloud_infrastructure, domain_dns, etc.)
- **Deductibility** - Yes/Partial/Unknown
- **FlaggedBy** - How this was identified (whitelist/manual/pattern)
- **Confidence** - High/Medium/Low
- **Notes** - Reasoning, questions, business purpose

---

## Part 2: Tax Deduction Analysis & Breakdowns

### Philosophy: "Show Your Work"

Each major deduction category gets its own detailed breakdown document (like showing work in math class). These breakdowns:
- Show all calculations step-by-step
- Explain the logic and tax rules
- Compare different approaches
- Document sources and assumptions
- Provide actionable recommendations

### Breakdown Document Naming Convention

**Format:** `BREAKDOWN_YYYY_Category_Description.md`

**Examples:**
- `BREAKDOWN_2022_Home_Office_Summary.md` - Final home office deduction recommendation
- `BREAKDOWN_2022_Mortgage_Interest_Federal_State.md` - Federal + CA mortgage deduction analysis
- `BREAKDOWN_2022_Office_Expenses.md` - Pasadena office + home office combined analysis

### Current Breakdown Documents

#### Home Office Deduction
1. **BREAKDOWN_2022_Home_Office_Summary.md** ⭐ START HERE
   - Final recommendation: Actual expenses WITHOUT depreciation
   - Three methods compared (simplified, actual, actual+depreciation)
   - Tax savings: ~$1,583/year
   - Business use: 15.2% (225 sq ft office / 1,480 sq ft home)

2. **BREAKDOWN_2022_Home_Office_Calculation.md**
   - Detailed scenarios based on different home sizes
   - Method comparison matrix
   - IRS qualification requirements

3. **BREAKDOWN_2022_Depreciation_Recapture.md**
   - Long-term analysis of depreciation vs. no depreciation
   - 5, 10, 15, 20-year scenarios
   - Recapture tax calculations
   - Why we recommend skipping depreciation

#### Mortgage Interest
4. **BREAKDOWN_2022_Mortgage_Interest_Federal_State.md** ⭐ COMPREHENSIVE
   - Federal vs. California treatment
   - Split method: 15.2% business, 84.8% personal
   - Total tax savings: ~$7,271 (federal + CA)
   - Itemized vs. standard deduction analysis
   - SALT cap considerations
   - Loan limitation check ($750k limit)

5. **BREAKDOWN_2022_Mortgage_Interest_Initial.md**
   - Initial analysis (simpler version)
   - Basic scenarios and options

#### Office Expenses
6. **BREAKDOWN_2022_Office_Expenses.md**
   - Pasadena office rent reimbursement cycle ($9,600)
   - **CRITICAL:** Verify reimbursements not counted as income
   - Parking expenses: $336.50 (NOT reimbursed, deductible)
   - Internet payments: TBD (need to locate)
   - Combined with home office expenses

### How Breakdowns Feed Into Final Deductions

**Flow:**
```
Individual Breakdowns → 2022_TAX_DEDUCTIONS.md → Tax Return
        ↓                          ↓
    Show logic              Consolidated list        Final Schedule C/A
    Calculate totals        Action items             Form 8829
    Compare options         Documentation needed      Actual tax forms
```

**Example:**
1. `BREAKDOWN_2022_Home_Office_Summary.md` calculates → **$3,572.86 deduction**
2. `BREAKDOWN_2022_Mortgage_Interest_Federal_State.md` calculates → **$3,102.39 business portion**
3. These feed into `2022_POTENTIAL_DEDUCTIONS_CHECKLIST.md` → **Home office total: $3,572.86**
4. Tax preparer uses this → **Form 8829 Line 10 (mortgage interest business portion)**

### Master Checklist: 2022_POTENTIAL_DEDUCTIONS_CHECKLIST.md

This is the comprehensive brainstorming list of ALL potential deductions:
- Add any deduction idea freely (even if uncertain)
- Check off items with inline notes about outcomes
- Track both qualifying and non-qualifying items (with reasons)
- References to detailed breakdowns for major categories
- Running tally of known amounts

**Purpose:** Braindump hundreds of ideas, then research and document outcomes inline

**Status Tracking:**
- Unchecked - Not yet researched
- Checked + **$amount** - Qualifies and amount known
- Checked + **N/A** or **NOT DEDUCTIBLE** - Doesn't qualify (with reason)
- Checked + **Needs...** - More information required

---

## Current Phase & Next Steps

### Completed:
- ✅ Home office deduction analysis (3 methods compared)
- ✅ Mortgage interest federal + state analysis
- ✅ Office expenses (Pasadena + home combined)
- ✅ Depreciation recapture long-term analysis
- ✅ Automated expense flagging (whitelist approach)
- ✅ Parking expense identification ($336.50)

### In Progress:
- ⚠️ Locating Pasadena office internet payments (check credit card statements)
- ⚠️ Gathering home utility bills for 2022 (electric, gas, water)
- ⚠️ Gathering homeowners insurance 2022 bill

### Next Deduction Categories to Break Down:
1. **Utilities** (home office portion)
2. **Insurance** (homeowners insurance, business portion)
3. **Business Supplies & Equipment** (flagged expenses from whitelist)
4. **Professional Development** (courses, subscriptions)
5. **Vehicle Expenses** (if applicable)
6. **Health Insurance** (self-employed deduction)
7. **Retirement Contributions** (SEP-IRA, Solo 401k)

---

## Creating New Breakdown Documents

### Template Structure:

```markdown
# BREAKDOWN_YYYY_Category_Name
**Purpose:** [What this breakdown analyzes]
**Tax Year:** YYYY
**Analysis Date:** YYYY-MM-DD

---

## Executive Summary
[Key findings, recommended approach, total deduction amount]

## [Category] Details
[Specific data, calculations, scenarios]

## Tax Treatment
[Federal rules, state rules, special considerations]

## Calculations
[Step-by-step math, show all work]

## Comparison of Methods/Options
[If multiple approaches exist, compare them]

## Recommendations
[What to do, why, expected savings]

## Action Items
[Documentation needed, questions for tax pro]

## Related Documents
[Links to other relevant breakdowns]

---

*Source Documents:*
[List actual files/forms used]
```

### Best Practices:
1. **Show your work** - Like math class, document every step
2. **Compare options** - If multiple methods exist, analyze all
3. **Cite sources** - Reference IRS publications, forms, actual documents
4. **Calculate savings** - Always show tax impact in dollars
5. **Document assumptions** - Tax bracket, filing status, business %
6. **Cross-reference** - Link related breakdowns together

---

## Iteration Strategy

This is designed for constant refinement:

### Transaction-Based Expenses:
1. Run `flag_expenses.py` to identify candidates
2. Review flagged transactions manually
3. Update whitelist patterns based on learnings
4. Add to expenses CSV
5. Repeat

### Deduction Analysis:
1. Identify deduction category
2. Gather source documents (forms, receipts, statements)
3. Research IRS rules and CA rules
4. Create breakdown document showing all work
5. Calculate tax savings
6. Add to master checklist
7. Provide to tax preparer

Nothing is fixed - adjust the process as needed.

---

## Key Files Reference

### Must-Read Documents:
1. **2022_POTENTIAL_DEDUCTIONS_CHECKLIST.md** - Master brainstorming list (start here)
2. **breakdowns/BREAKDOWN_2022_Home_Office_Summary.md** - Home office recommendation
3. **breakdowns/BREAKDOWN_2022_Mortgage_Interest_Federal_State.md** - Mortgage analysis
4. **breakdowns/BREAKDOWN_2022_Office_Expenses.md** - Office expenses + reimbursements

### Supporting Documents:
- **expense_patterns_whitelist.json** - Patterns for automated flagging
- **expenses_template.csv** - CSV template with proper columns
- **flagged_expenses_*.csv** - Auto-flagged transactions

### Scripts:
- **../scripts/flag_expenses.py** - Automated expense flagging

---

## Summary of Tax Savings (2022)

| Category | Deduction Amount | Tax Savings (est.) | Status |
|----------|------------------|-------------------|---------|
| **Home Office** | $3,572.86 | $1,404 | ✅ Calculated |
| **Mortgage Interest (business)** | $3,102.39 | $1,219 | ✅ Calculated |
| **Mortgage Interest (personal)** | $17,308.04 | $5,764 | ✅ Calculated |
| **Pasadena Office Parking** | $336.50 | $132 | ✅ Calculated |
| **Pasadena Office Internet** | TBD | TBD | ⚠️ Need to locate |
| **Business Supplies (whitelist)** | $13,684.49 | $5,378 | ⚠️ Need review |
| **Utilities (home office)** | ~$456 | ~$179 | ⚠️ Need bills |
| **Insurance (home office)** | TBD | TBD | ⚠️ Need bill |
| **TOTAL (known)** | **$38,460+** | **~$14,076+** | In progress |

---

*Last Updated: 2025-10-16*
