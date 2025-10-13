# Transaction Categorization Reference

This document provides guidelines for categorizing transactions consistently across all financial documents.

## Category List

### Income Categories

| Category | Business/Personal | Deductible | Examples |
|----------|------------------|------------|----------|
| Payroll | Business | N/A | Gusto Pay, Popstand Inc Payroll |
| Wire Transfer In | Business | N/A | Client payments, contractor payments |
| Interest Income | Mixed | N/A | Bank interest |
| Refund/Return | Varies | Varies | Purchase returns, refunds |

### Expense Categories - Business

| Category | Business/Personal | Deductible | Examples | Notes |
|----------|------------------|------------|----------|-------|
| **Software & Services** | Business | Yes | GitHub, Slack, Heroku, AWS, Quicknode | SaaS subscriptions, development tools |
| **Hosting & Infrastructure** | Business | Yes | Hivelocity, Pinata Cloud, Amazon Web Services | Cloud hosting, servers, infrastructure |
| **Domain & DNS** | Business | Yes | GoDaddy, Google Domains | Domain registration and management |
| **Professional Services** | Business | Yes | Gitbook, Medium, Twitter Blue | Business-related subscriptions |
| **Banking Fees** | Business | Yes | Wire transfer fees, service charges | Only business account fees |
| **Office Supplies** | Business | Yes | Amazon (office items), Staples | Clearly office-related purchases |
| **Equipment** | Business | Yes | Computer hardware, monitors, office furniture | Capital expenses, may need depreciation |
| **Storage** | Business | Yes | Porta-Stor | Business storage only |
| **Utilities** | Mixed | Partial | So Cal Edison, So Cal Gas, AT&T | Requires business use percentage |
| **Internet/Phone** | Mixed | Partial | AT&T, Verizon | Requires business use percentage |
| **Auto/Vehicle** | Mixed | Partial | Wells Fargo Auto, gas | Requires business mileage tracking |
| **Business Meals** | Business | Partial | Restaurant purchases (with business purpose) | 50% deductible, document business purpose |

### Expense Categories - Personal

| Category | Business/Personal | Deductible | Examples |
|----------|------------------|------------|----------|
| **Groceries** | Personal | No | Whole Foods, Instacart, Erewhon |
| **Food Delivery** | Personal | No | Uber Eats, DoorDash (unless business meal) |
| **Personal Shopping** | Personal | No | Target, IKEA, Amazon (personal items) |
| **Entertainment** | Personal | No | Netflix, Hulu, Prime Video, Audible |
| **Transportation** | Personal | No | Uber, Lyft (unless business travel) |
| **Home Improvement** | Personal | No | Home Depot, Lowe's (unless home office) |
| **Personal Services** | Personal | No | Gym, personal subscriptions |
| **Cryptocurrency** | Personal | No | Kraken, Coinbase (separate crypto tax tracking) |
| **Credit Card Payments** | Personal | No | Chase Credit Card payments |
| **Investments** | Personal | No | Stash Capital, investment accounts |

### Special Categories

| Category | Business/Personal | Deductible | Examples | Notes |
|----------|------------------|------------|----------|-------|
| **Tips** | Varies | Varies | Amazon Tips, delivery tips | Deductible if business meal |
| **Mixed Purchases** | Mixed | Partial | Amazon (mixed items) | Needs itemization |
| **Unclear/Review** | Unknown | Unknown | Unfamiliar merchants | Flag for review |

## Merchant Pattern Matching

### Automatic Business Classification

These merchants are typically business expenses:
- `Pwp` prefix (Privacy.com business transactions)
- `GitHub`, `Slack`, `Heroku`, `AWS`, `Google Cloud`
- `GoDaddy`, `Domain.com`, `Cloudflare`
- `Quicknode`, `Pinata`, `Hivelocity`
- `Gitbook`, `Hootsuite`, `Terminal`
- Wire transfers from known business entities

### Automatic Personal Classification

These merchants are typically personal:
- `Uber Eats`, `Instacart`, `Whole Foods`, `Erewhon`
- `Netflix`, `Hulu`, `Prime Video`, `Audible`, `Spotify`
- `Target`, `IKEA`, `Home Depot`, `Lowe's` (unless clearly business)
- `Uber`, `Lyft` (unless business travel)

### Requires Manual Review

These need context to classify:
- `Amazon` - Could be business or personal, needs item details
- `Apple.com` - Could be iCloud business storage or personal
- Restaurants - Personal unless documented business meal
- Home improvement - Personal unless home office related

## Amount Formatting

- **Expenses/Debits:** Use negative numbers (e.g., `-50.00`)
- **Income/Credits:** Use positive numbers (e.g., `2000.00`)
- **Always 2 decimal places** for consistency

## Notes Field Guidelines

Use Notes field to document:
- **Business purpose** for borderline expenses
- **Business use percentage** for mixed-use items
- **Questions** about categorization
- **Item details** for Amazon/mixed purchases
- **Meeting/client names** for business meals
- **Project names** for project-specific expenses

### Examples:
```
"Business dinner with client John Smith"
"80% business use - home office internet"
"Office supplies: printer paper, pens"
"Personal items - not deductible"
"Review: unclear if business or personal"
```

## Workflow for Categorization

1. **First pass:** Automatic categorization based on merchant patterns
2. **Second pass:** Review uncategorized and flagged transactions
3. **Third pass:** Add business/personal classification
4. **Fourth pass:** Confirm deductibility
5. **Final pass:** Add detailed notes where needed

## When in Doubt

- **Flag it for review** - Use Category "Unclear/Review"
- **Add detailed notes** about why it's unclear
- **Research later** with more context
- **Ask accountant** during final review

Better to flag something than miscategorize it!
