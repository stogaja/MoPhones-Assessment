# MoPhones Data Analytics Case Study
## Product Analytics Report

**Date:** January 2026  

---

## Executive Summary

This report analyzes MoPhones' credit portfolio performance, customer segmentation, and the relationship between credit outcomes and customer satisfaction (NPS). The analysis covers 71,456 credit records across 5 quarterly snapshots from January to December 2025, with demographic and NPS data for customer insights.

**Key Findings:**
- Portfolio grew from 9,082 accounts (Jan) to 24,828 accounts (Dec), a 173% increase
- Average arrears increased from 99.7M to 323.9M, indicating growing risk exposure
- Older customers (46-55, Above 55) show significantly lower arrears than younger segments
- Higher income customers demonstrate better repayment behavior
- NPS scores are negatively correlated with arrears - customers with arrears score 6.29 vs 7.10 for those without

---

## 1. Portfolio Performance Over Time

### 1.1 Overall Portfolio Growth

| Date | Account Count | Total Paid | Total Arrears | Avg Days Past Due |
|------|--------------|------------|---------------|-------------------|
| 2025-01-01 | 9,082 | 288.9M | 99.7M | 71.6 |
| 2025-03-31 | 11,405 | 393.8M | 151.4M | 88.7 |
| 2025-06-30 | 14,863 | 526.3M | 209.2M | 99.6 |
| 2025-09-30 | 18,337 | 677.4M | 264.9M | 112.8 |
| 2025-12-30 | 24,828 | 892.3M | 323.9M | 111.6 |

**Observations:**
- Portfolio size increased 173% over the year
- Total payments grew proportionally with portfolio size
- Arrears grew faster (225%) than portfolio size, indicating deteriorating quality
- Days past due peaked in Q3 (112.8 days) before slight improvement in Q4

### 1.2 Performance by Customer Segments

#### Age Group Analysis (Latest Snapshot - Dec 2025)

**Average Arrears by Age Group:**
- 46-55: 4,809 (Lowest risk)
- Above 55: 5,666
- 36-45: 6,744
- 26-35: 8,277
- 18-25: 8,414 (Higher risk)
- Unknown: 19,404 (Highest risk - data quality issue)

**Key Insights:**
- Clear inverse relationship between age and credit risk
- Older customers (46+) have ~40% lower arrears than younger customers (18-35)
- Unknown age group shows 2.3x higher arrears, highlighting data quality importance

#### Income Group Analysis (Latest Snapshot - Dec 2025)

**Average Arrears by Income Group:**
- 5,000–9,999: 5,793 (Lowest risk)
- 100,000–149,999: 7,149
- 150,000 and above: 7,413
- 50,000–99,999: 7,687
- 10,000–19,999: 7,815
- 30,000–49,999: 8,299
- 20,000–29,999: 8,465
- Below 5,000: 20,485 (Highest risk)

**Key Insights:**
- Lower income customers (<5,000) show 2.6x higher arrears than mid-tier income groups
- Surprisingly, the 5,000-9,999 group performs best, possibly due to conservative credit limits
- Very high income (150,000+) shows moderate arrears, suggesting affordability isn't the only factor

### 1.3 Account Status Distribution

The portfolio shows diverse account statuses including:
- **Active accounts** (New Active, Existing Active): Core performing portfolio
- **Inactive tiers** (01-07, 08-14, 15-30 days): Early warning indicators
- **Default categories**: Various stages of non-performance
- **Closed accounts**: Paid Off (Cash/Loan), Returns, Write-offs

---

## 2. Portfolio Health & Risk Metrics

### 2.1 Recommended Key Performance Indicators (KPIs)

#### Primary Health Metrics:
1. **Portfolio at Risk (PAR) Ratio**
   - Formula: Total Arrears / Total Outstanding Balance
   - Tracks overall portfolio quality
   - Current trend: Increasing (concern)

2. **Delinquency Rate by Bucket**
   - % of accounts in 1-30, 31-60, 61-90, 90+ days past due
   - Enables early intervention strategies

3. **Vintage Analysis**
   - Track cohort performance over time
   - Identify seasonality and underwriting quality changes

4. **Roll Rate Analysis**
   - Probability of accounts moving between delinquency buckets
   - Predicts future defaults

#### Secondary Metrics:
5. **Net Default Rate**: Accounts moving to write-off status
6. **Recovery Rate**: Collections on defaulted accounts
7. **Average Days to First Payment**: Early performance indicator
8. **Payment Consistency Score**: Regularity of payments

### 2.2 Risk Indicators

**Best Predictors of Portfolio Risk:**
1. **Days Past Due**: Strong leading indicator (peaked at 112.8 days in Q3)
2. **Account Status Transitions**: Movement from Active → Inactive → Blocked
3. **Customer Age**: Inverse correlation with risk
4. **Income Level**: Below 5,000 shows 3-4x higher risk
5. **First Payment Behavior**: "First Payment Default" status is critical

**Recommended Risk Segmentation:**
- **Low Risk**: Age 46+, Income 5,000-150,000, <30 days past due
- **Medium Risk**: Age 26-45, Income 10,000-50,000, 30-60 days past due
- **High Risk**: Age 18-25, Income <5,000 or Unknown, 60+ days past due

---

## 3. Credit Outcomes vs Customer Satisfaction (NPS)

### 3.1 NPS Analysis by Account Status

**Average NPS Score by Account Status:**
- New Active: 8.17 (Highest - honeymoon period)
- Lost Write Off: 8.16 (Surprisingly high - possibly relief from debt)
- Inactive 15-30: 7.48
- Paid Off Cash: 7.54
- Inactive 08-14: 7.28
- First Payment Default: 7.31
- Existing Active: 7.06
- Blocked 31-60: 7.10
- Blocked 61-90: 7.00
- Paid Off Loan: 6.94
- Inactive 01-07: 6.62
- Write Off: 6.22
- First Month Default with inventory: 4.94
- Cancelled Returned past 3 mths: 4.00
- First 2 days Return: 3.53
- Cancelled Returned in 3 mths: 3.15

### 3.2 NPS by Arrears Status

- **No Arrears**: 7.10
- **Has Arrears**: 6.29

**Difference**: -0.81 points (11% lower satisfaction)

### 3.3 Trade-offs Between Recovery and Experience

**Key Findings:**
1. **Collections Pressure Impact**: Customers with arrears show measurably lower NPS
2. **Status Paradox**: Some defaulted statuses (Write Off) show moderate NPS, possibly due to:
   - Reduced collection pressure
   - Account closure providing psychological relief
   - Selection bias (only engaged customers respond)

3. **Early Returns**: Lowest NPS (3.15-3.53) for early returns, indicating:
   - Product quality issues
   - Mismatched expectations
   - Poor onboarding experience

**Recommended Balance:**
- Implement **graduated collections approach**: Gentle reminders for first 30 days, escalating thereafter
- **Proactive communication**: Reach out before customers fall into arrears
- **Flexible payment plans**: Offer restructuring before accounts become severely delinquent
- **Product quality focus**: Address early return issues to prevent low NPS

---

## 4. Data Assumptions & Limitations

### 4.1 Point-in-Time Data Assumptions

**Assumptions Made:**
1. **Snapshot Representation**: Each quarterly snapshot represents the account state at that specific date, not cumulative behavior
2. **Age Calculation**: Customer age calculated as of each snapshot date using DOB
3. **Income Stability**: Average income (total receipts / duration) assumes consistent income over loan period
4. **NPS Timing**: NPS surveys linked to LOAN_ID without specific date matching - assumed to reflect recent experience
5. **Account Status**: Current status may not reflect full payment history between snapshots

**Impact on Analysis:**
- **Trend Analysis**: Limited to 5 data points; may miss intra-quarter volatility
- **Behavioral Patterns**: Cannot track individual account transitions between snapshots
- **Causality**: Difficult to establish cause-effect between actions and outcomes
- **Seasonality**: Insufficient data points to identify seasonal patterns

### 4.2 Data Quality Issues

**Missing Data:**
1. **Unknown Age Group**: 19,404 average arrears suggests significant missing DOB data
2. **Income Data**: Some LOAN_IDs lack income information (NaN values)
3. **NPS Coverage**: Not all customers have NPS responses (inner join reduced dataset)

**Inconsistent Fields:**
1. **Column Naming**: Whitespace in column names (e.g., "Loan Id " with trailing space)
2. **Date Formats**: Mixed formats required careful parsing
3. **Income Sources**: Three separate columns (Received, Banks Received, Paybills) required aggregation logic

**Unclear Definitions:**
1. **Account Status Categories**: Multiple similar statuses (e.g., various "Inactive" and "Default" types)
2. **ARREARS vs BALANCE**: Relationship between these fields not explicitly defined
3. **Duration Field**: Units not specified (assumed months based on loan terms)

### 4.3 Impact on Confidence

**High Confidence:**
- Overall portfolio growth trends
- Age and income group risk patterns
- NPS correlation with arrears

**Medium Confidence:**
- Specific account status transitions
- Exact default rates (need full payment history)
- Income group analysis (due to missing data)

**Low Confidence:**
- Causality between specific actions and NPS
- Seasonal patterns (insufficient time series)
- Recovery rates (need post-default tracking)

---

## 5. Data & Reporting Recommendations

### 5.1 Critical Data Improvements

**Immediate Priority:**
1. **Complete Customer Demographics**
   - Mandatory DOB collection at onboarding
   - Backfill missing DOB data through verification
   - Target: <5% unknown age group

2. **Enhanced Payment Tracking**
   - Daily/weekly snapshots instead of quarterly
   - Payment transaction log with timestamps
   - Track payment method and amount per transaction

3. **Account Status Standardization**
   - Consolidate similar status categories
   - Clear definitions for each status
   - Document status transition rules

**Secondary Priority:**
4. **Income Verification**
   - Standardize income data collection
   - Validate against actual mobile money flows
   - Update income data periodically (every 6 months)

5. **NPS Survey Metadata**
   - Capture survey date/time
   - Link to specific account status at survey time
   - Add survey trigger reason (e.g., post-payment, post-contact)

### 5.2 Reporting Infrastructure

**Recommended Dashboards:**

1. **Executive Dashboard** (Weekly)
   - Portfolio size and growth rate
   - PAR ratio trend
   - Collections efficiency
   - NPS score

2. **Risk Management Dashboard** (Daily)
   - Delinquency buckets (1-30, 31-60, 61-90, 90+)
   - Roll rates between buckets
   - High-risk account alerts
   - Vintage performance

3. **Collections Dashboard** (Daily)
   - Accounts by days past due
   - Collection activity and outcomes
   - Promise-to-pay tracking
   - Recovery rate by collector

4. **Customer Experience Dashboard** (Monthly)
   - NPS by segment
   - NPS trend over time
   - Complaint/issue tracking
   - Product return rates

### 5.3 Data Architecture

**Recommended Structure:**
```
Raw Layer:
- Credit transactions (daily)
- Customer demographics (SCD Type 2)
- Income verification (versioned)
- NPS surveys (timestamped)
- Collection activities (event log)

Staging Layer:
- Standardized schemas
- Data quality checks
- Deduplication
- Type conversions

Analytics Layer:
- Customer dimension (SCD Type 2)
- Credit fact table (daily snapshots)
- Payment fact table (transactions)
- NPS fact table (surveys)
- Collections fact table (activities)

Reporting Layer:
- Pre-aggregated metrics
- Dashboard-specific views
- Historical trends
```

### 5.4 Data Quality Framework

**Implement Automated Checks:**
1. **Completeness**: % of required fields populated
2. **Validity**: Data type and range checks
3. **Consistency**: Cross-field validation (e.g., paid amount ≤ balance)
4. **Timeliness**: Data freshness monitoring
5. **Uniqueness**: Duplicate detection

**Quality Metrics:**
- Target: 95% completeness for critical fields
- Target: <1% invalid records
- Target: Data available within 24 hours of transaction

---

## 6. Strategic Recommendations

### 6.1 Credit Policy

1. **Age-Based Pricing**: Consider lower rates for 46+ age group given lower risk
2. **Income Verification**: Mandatory for <5,000 income group or higher deposit requirements
3. **First Payment Focus**: Intensive support for first payment to prevent early defaults
4. **Graduated Limits**: Start with lower limits for high-risk segments, increase based on performance

### 6.2 Collections Strategy

1. **Proactive Outreach**: Contact customers at 15 days past due (before 30-day mark)
2. **Segmented Approach**: Different strategies for age/income segments
3. **Payment Plans**: Offer restructuring at 30 days to prevent 60+ day delinquency
4. **Customer-Centric**: Balance recovery with NPS impact - avoid aggressive tactics that damage satisfaction

### 6.3 Product & Experience

1. **Address Early Returns**: Investigate and fix issues causing 3-day returns (NPS 3.15)
2. **Onboarding**: Enhanced education for first-time customers
3. **Payment Reminders**: Automated, friendly reminders before due dates
4. **Success Stories**: Share positive outcomes to improve NPS

---

## Appendices

### A. Methodology

**Age Group Calculation:**
```python
Age = (Snapshot Date - Date of Birth) / 365.25
Groups: 18-25, 26-35, 36-45, 46-55, Above 55
```

**Income Group Calculation:**
```python
Total Income = Received + Banks Received + Paybills Received Others
Average Income = Total Income / Duration
Groups: Below 5,000 | 5,000–9,999 | 10,000–19,999 | 20,000–29,999 | 
        30,000–49,999 | 50,000–99,999 | 100,000–149,999 | 150,000+
```

**NPS Scoring:**
- Scale: 0-10 (based on "How likely are you to recommend MoPhones?")
- Analysis: Mean score by segment

### B. Data Sources

1. **Credit Data**: 5 CSV files (quarterly snapshots)
   - 71,456 total records
   - 24,828 unique accounts (latest snapshot)

2. **Customer Data**: Excel workbook with 4 sheets
   - Sales Details
   - Gender
   - DOB
   - Income Level

3. **NPS Data**: Excel workbook
   - Survey responses with scores
   - Linked by LOAN_ID

### C. Tools & Technologies

- **Analysis**: Python (pandas, numpy)
- **Data Transformation**: dbt (see separate dbt project)
- **Reporting**: Markdown documentation

---

