# Amazon 2023 Purchases

## Source

These CSVs were generated using AI (Claude browser plugin) to extract data from Amazon order history pages. The extraction was originally done for Automatique Inc expense tracking.

## Dual Role

The CSV serves as both:
- **Source document** -- the original extracted data from Amazon order history
- **Generated file** -- AI-extracted and structured into CSV format

There is no underlying PDF or receipt for these; the Amazon order history web pages are the original source.

## Data Notes

- The CSV contains a `Business` column (Y/N) for filtering business vs personal purchases
- Items marked `Y` are business expenses; items marked `N` are personal
- The `Notes` column provides categorization context
- Prices include the `$` symbol and should be parsed accordingly

## Canonical Source

The single source of truth for this file is:

```
automatique-inc/2023/generated-files/extracted/amazon/2023_amazon_purchases.csv
```

Copies placed here and in `personal/2023/generated-files/extracted/amazon/` are for convenience within the personal tax year workflow.
