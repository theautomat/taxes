# Coinbase / Crypto Research for 2023 Tax Year

## What Was Done for 2022

### Documents Collected
The 2022 Coinbase folder (`personal/2022/source-documents/coinbase/`) contains:

1. **Monthly Statements (12 PDFs):** `coinbase-1-jan-2022.pdf` through `coinbase-12-dec-2022.pdf`
2. **Transaction Source CSV:** `coinbase_2022_transactions_source.csv` - Raw Coinbase transaction export (50 transactions)
3. **Marked-Up Transactions:** `coinbase_2022_transactions_marked_up.csv` - Annotated with tax treatment, cost basis, gain/loss
4. **Income CSV:** `coinbase_2022_income.csv` - Staking rewards + FLOW bonuses
5. **Capital Gains/Losses CSV:** `coinbase_2022_capital_gains_losses.csv` - Form 8949 data with LIFO methodology
6. **BTC Transaction History:** `btc_transaction_history.csv` - Full BTC transaction history 2018-2022
7. **BTC Cost Basis Proof:** `btc_cost_basis_proof.csv` - Detailed cost basis verification
8. **BTC LIFO Analysis:** `btc_lifo_analysis.csv` - Step-by-step LIFO calculation

### Accountant Deliverables
- `for-accountant/summary.txt` - Concise tax summary
- `for-accountant/capital_gains_losses.csv` - 7 capital gain/loss entries for Form 8949
- `for-accountant/income.csv` - 3 ordinary income entries (staking + 2 FLOW bonuses)
- `for-accountant.zip` - Packaged for delivery
- `for-accountant-with-extras/coinbase_2022_tax_summary.csv` - Detailed tax summary with full methodology notes

### 2022 Tax Summary
- **Ordinary Income:** $166,765.16
  - USDC Staking Rewards: $427.67
  - FLOW Bonus (July): $124,425.00 (75,000 FLOW from NFT Genius)
  - FLOW Bonus (December): $41,912.49 (37,912.7 FLOW from NFT Genius)
- **Capital Losses:** -$14,316.17 (all short-term)
  - BTC conversions: -$3,237.45
  - FLOW disposals: -$11,078.72

### Crypto Holdings at End of 2022

**BTC remaining:** ~1.305 BTC (from btc_transaction_history.csv - last balance entry shows balance after March 2022 sell, but Jan/Feb 2022 sends also occurred)
- Pre-2022 BTC balance: ~1.894 BTC
- 2022 sends (Jan-Feb): -0.140 BTC
- 2022 same-day conversions (March): net zero (acquired and disposed same lots)
- 2022 old BTC sold (March 29): -0.448 BTC
- **Estimated end-of-2022 BTC balance: ~1.306 BTC**

**USDC remaining:** Significant balance likely held. In 2022:
- Received ~$175k in USDC from FLOW conversions and other converts
- Sent some out to external wallets ($5,014 to external address)
- Converted some to ETH ($21,094.59 total)
- Received $427.67 in staking rewards
- **Substantial USDC balance likely carried into 2023** (exact amount needs verification from Dec 2022 statement)

**FLOW remaining:** ~1,313 FLOW
- Received 75,000 FLOW (July) + 37,912.7 FLOW (December) = 112,912.7 FLOW
- Converted 73,884.69 FLOW (July) + 38,714.19 FLOW (December) = 112,598.88 FLOW
- **Remaining: ~313.82 FLOW** (negligible value)

**ETH:** All sent to external wallet (0x96C3D5...AFA606). Holdings exist off-Coinbase.

**APE:** Sent to external wallet. Holdings exist off-Coinbase.

## What Exists for 2023

### Currently in Repository
**Nothing.** There are no Coinbase or crypto-related files in `personal/2023/`.

### Crypto-Related Expenses Found in 2023 Privacy.com Data
- **2023-06-25:** ZenLedger purchase - $149.00 (crypto tax software)
- **2023-06-25:** CoinLedger purchase - $99.99 (crypto tax software)
- **2023-06-28:** ZenLedger refund - $149.00
- Net crypto tax software cost: $99.99 (CoinLedger only - ZenLedger was refunded)
- **Note:** These are deductible business expenses (tax preparation software)

### Other Crypto Platforms
- **Kraken:** Small recurring $9/month charges seen in 2021-2022 Privacy.com data (subscription). No charges in 2023.
- **External wallets:** ETH and APE were sent to external wallets in 2022. Any activity in those wallets (DeFi, NFT sales, etc.) would need separate tracking.

## What's Missing / Needed for 2023

### Priority 1: Required Documents
1. **Coinbase Tax Documents**
   - Coinbase 1099-MISC (if issued - typically for >$600 in staking/rewards)
   - Coinbase tax center report (capital gains/losses for 2023)
   - These are the most important documents - they tell us if any crypto was sold/traded

2. **Coinbase Transaction History Export**
   - Full 2023 transaction CSV from Coinbase
   - Shows all buys, sells, converts, sends, receives, rewards
   - This is the raw data needed to calculate taxes

3. **Monthly Statements (Jan-Dec 2023)**
   - 12 PDFs from Coinbase showing monthly activity
   - Useful for verification but transaction history CSV is more important

### Priority 2: Important for Completeness
4. **End-of-Year Balance / Portfolio Report**
   - Shows exactly what assets were held on Dec 31, 2023
   - Important for tracking carryover into 2024

5. **Staking Rewards Report**
   - Were USDC staking rewards still being earned in 2023?
   - These are taxable ordinary income

### Priority 3: If Applicable
6. **External Wallet Activity**
   - ETH wallet (0x96C3D5A76170e53F8aBeC088b71DF46493AFA606) - any DeFi/NFT activity?
   - APE wallet activity?
   - Any NFT sales or DeFi yields?

7. **Other Crypto Platforms**
   - Kraken: Any 2023 activity? (subscription stopped)
   - CoinLedger report: The $99.99 purchase suggests tax reporting was attempted. Any generated reports?

## How to Download from Coinbase

### Transaction History
1. Log in to Coinbase at coinbase.com
2. Click profile icon (top right) > **Taxes**
3. Under "Documents", look for any 1099 forms for 2023
4. Under "Transaction history", click **Generate report**
5. Select date range: Jan 1, 2023 - Dec 31, 2023
6. Download as CSV
7. Save to `personal/2023/source-documents/coinbase/coinbase_2023_transactions.csv`

### Tax Reports
1. In the Taxes section, look for **Tax reports** or **Tax documents**
2. Download the Coinbase-generated tax summary for 2023
3. If a 1099-MISC was issued, download it
4. Save to `personal/2023/source-documents/coinbase/`

### Monthly Statements
1. Go to Settings > Statements or Reports
2. Select each month of 2023
3. Download as PDF
4. Name them: `coinbase-1-jan-2023.pdf` through `coinbase-12-dec-2023.pdf`

### Alternative: Use CoinLedger
Since CoinLedger was purchased in June 2023 ($99.99), the user may already have a crypto tax report generated there. Check for any exports from CoinLedger that could serve as the transaction/tax data.

## Key Questions for the Taxpayer

1. **Was there any crypto trading activity in 2023?** (buys, sells, converts)
   - If the USDC and BTC were just held, the tax impact is minimal (only staking rewards)
2. **Was NFT Genius still paying FLOW bonuses in 2023?** (NFT Genius may have shut down)
3. **Any activity in external wallets?** (ETH wallet, NFT sales, DeFi)
4. **Did you use CoinLedger to generate a 2023 tax report?** If so, where is it?
5. **Kraken account - any 2023 activity?**

## Folder Structure Created

```
personal/2023/
  source-documents/
    coinbase/              (empty - needs documents)
      for-accountant/      (empty - to be populated after analysis)
  generated-files/
    extracted/
      coinbase/            (empty - for extracted CSVs)
```
