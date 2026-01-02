# MoPhones Data Analytics Case Study - Submission Summary

## Submission Contents

This repository contains the complete analysis and dbt implementation for the MoPhones Product Analytics case study.

### Repository Structure

```
MoPhones/
├── data/
│   ├── raw/                        # Original data files
│   │   ├── Credit Data/            # quarterly snapshots
│   │   ├── NPS Data.xlsx           # customer satisfaction data
│   │   └── Sales and Customer Data.xlsx # demographics and income
│   └── processed/                  # Intermediate outputs
├── docs/
│   ├── MoPhones Data Case Study.pdf # original prompt
│   └── CASE_STUDY_ANALYSIS.md      # Main analysis report
├── scripts/
│   └── mo_phones_analysis.py       # Python analysis script
├── MoPhones_dbt/                    # dbt project
├── README.md                        # This file
└── .gitignore
```

---

## Analysis Summary

### Key Findings

1. **Portfolio Growth**: 173% increase in accounts (9,082 to 24,828) over 2025
2. **Risk Trends**: Arrears grew 225%, outpacing portfolio growth
3. **Age Segmentation**: Customers 46+ show 40% lower arrears than 18-35 age group
4. **Income Patterns**: Below 5,000 income group has 2.6x higher arrears
5. **NPS Correlation**: Customers with arrears score 11% lower (6.29 vs 7.10)

### Questions Answered

The [CASE_STUDY_ANALYSIS.md](docs/CASE_STUDY_ANALYSIS.md) file provides detailed answers to all 6 case study questions:

1. [x] **Portfolio Performance Over Time** - Analyzed growth, arrears trends, and segmentation
2. [x] **Risk Indicators & Metrics** - Recommended KPIs and tracking methodology
3. [x] **Credit vs NPS Relationship** - Identified trade-offs and correlations
4. [x] **Data Assumptions** - Documented point-in-time limitations and impacts
5. [x] **Data Limitations** - Identified missing fields and quality issues
6. [x] **Improvement Recommendations** - Proposed data architecture and reporting enhancements

---

## dbt Implementation

### What's Included

The [MoPhones_dbt](MoPhones_dbt/) directory contains a production-ready dbt project with:

- [x] **Staging models**: Clean and standardize raw data
- [x] **Dimension tables**: Customer demographics with calculated fields
- [x] **Fact tables**: Credit performance time-series
- [x] **Analysis tables**: NPS-Credit linkage for experience monitoring
- [x] **Reusable macros**: Age and income group calculations
- [x] **Data quality tests**: Uniqueness, not-null, and referential integrity
- [x] **Sample raw data**: Demonstrates assumed upstream source structure
- [x] **Comprehensive documentation**: Schema definitions and usage examples

### Key Design Decisions

1. **Assumed Raw Sources**:
   - `credit_snapshots`: Point-in-time credit data
   - `customer_info`: Demographics (DOB, gender)
   - `income_details`: Multi-source income verification
   - `nps_surveys`: Customer satisfaction responses

2. **Transformation Logic**:
   - Age groups calculated dynamically per snapshot date
   - Income averaged across loan duration
   - Macros ensure consistency across models

3. **Data Quality**:
   - Tests on critical fields (loan_id uniqueness, not-null constraints)
   - Handles missing data with 'Unknown' categories
   - Validates NPS scores (0-10 range)

---

## How to Use This Submission

### 1. Review the Analysis

Read [docs/CASE_STUDY_ANALYSIS.md](docs/CASE_STUDY_ANALYSIS.md) for:
- Detailed answers to all case study questions
- Data insights and visualizations
- Strategic recommendations
- Methodology and assumptions

### 2. Explore the dbt Project

```bash
cd MoPhones_dbt

# Install dbt (if not already installed)
pip install dbt-core dbt-postgres  # or your database adapter

# Load sample data
dbt seed

# Run all models
dbt run

# Test data quality
dbt test

# Generate and view documentation
dbt docs generate
dbt docs serve
```

### 3. Run the Python Analysis

```bash
# Install dependencies
pip install pandas numpy openpyxl

# Run the main analysis
python [scripts/mo_phones_analysis.py](scripts/mo_phones_analysis.py)
```

---

## Analytical Approach

### Data Preparation

1. **Loaded 5 quarterly snapshots** (71,456 total records)
2. **Merged customer demographics** from Excel sheets
3. **Calculated derived fields**:
   - Age from DOB and snapshot date
   - Average income from multiple sources
   - Age and income group classifications

### Analysis Methodology

1. **Time-Series Analysis**: Tracked portfolio metrics across 5 quarters
2. **Segmentation**: Analyzed performance by age and income groups
3. **Correlation Analysis**: Linked credit outcomes to NPS scores
4. **Risk Profiling**: Identified high-risk customer segments

### Tools Used

- **Python (pandas)**: Data manipulation and analysis
- **dbt**: Production-ready data transformations
- **SQL**: Analytical queries and data modeling
- **Markdown**: Documentation and reporting

---

## Key Insights & Recommendations

### Immediate Actions
1. **Improve data quality**: Target <5% unknown age/income
2. **Implement daily snapshots**: Enable better trend analysis
3. **Proactive collections**: Contact customers at 15 days past due
4. **Address early returns**: Investigate 3-day return issues

### Strategic Initiatives
1. **Age-based pricing**: Lower rates for 46+ segment (lower risk)
2. **Income verification**: Mandatory for <5,000 income group
3. **NPS monitoring**: Track by account status to balance recovery and experience
4. **Data architecture**: Implement recommended staging to marts structure

### Metrics to Track
1. **Portfolio at Risk (PAR)**: Total arrears / outstanding balance
2. **Delinquency buckets**: % in 1-30, 31-60, 61-90, 90+ days
3. **Roll rates**: Probability of moving between buckets
4. **NPS by segment**: Monitor experience across customer groups

---

## Assumptions & Limitations

### Assumptions Made
- Income columns represent monthly flows
- Duration is in months
- NPS reflects recent customer experience
- Snapshot data represents end-of-period state

### Data Limitations
- Only 5 quarterly snapshots (limited time-series)
- Missing demographic data for some customers
- No payment transaction history between snapshots
- NPS survey timing not explicitly linked to credit events

### Impact on Analysis
- **High confidence**: Overall trends and segment patterns
- **Medium confidence**: Specific account transitions
- **Low confidence**: Causality and seasonal patterns

All limitations are documented in detail in [docs/CASE_STUDY_ANALYSIS.md](docs/CASE_STUDY_ANALYSIS.md) Section 4.

---

## Contact

For questions about this submission, review the comprehensive analysis in [docs/CASE_STUDY_ANALYSIS.md](docs/CASE_STUDY_ANALYSIS.md) or examine the [scripts/mo_phones_analysis.py](scripts/mo_phones_analysis.py) for implementation details.

---