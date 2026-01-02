# MoPhones Credit Analytics - dbt Project

## Overview
This dbt project transforms raw credit, customer, and NPS data into analytics-ready models for monitoring portfolio performance and customer experience at MoPhones.

## Project Structure

```
MoPhones_dbt/
├── dbt_project.yml          # Project configuration
├── README.md                 # This file
├── models/
│   ├── staging/              # Raw data cleaning and standardization
│   │   ├── schema.yml        # Source and staging model documentation
│   │   ├── stg_credit_data.sql
│   │   ├── stg_demographics.sql
│   │   ├── stg_income.sql
│   │   └── stg_nps.sql
│   └── marts/                # Business logic and analytics models
│       ├── schema.yml        # Marts model documentation
│       ├── dim_customers.sql # Customer dimension with age/income groups
│       ├── fct_credit_performance.sql  # Credit performance fact table
│       └── credits_nps_linked.sql      # NPS-Credit analysis table
├── macros/
│   ├── calculate_age_group.sql    # Reusable age grouping logic
│   └── calculate_income_group.sql # Reusable income grouping logic
├── seeds/
│   ├── sample_credit_snapshots.csv
│   ├── sample_customer_info.csv
│   ├── sample_income_details.csv
│   └── sample_nps_surveys.csv
└── tests/                    # Custom data quality tests (if any)
```

## Data Model

### Staging Layer
Cleans and standardizes raw data:
- **stg_credit_data**: Credit snapshots with standardized column names
- **stg_demographics**: Customer DOB and gender
- **stg_income**: Aggregated income from multiple sources
- **stg_nps**: Customer satisfaction survey responses

### Marts Layer
Business-ready analytics tables:
- **dim_customers**: Customer dimension with calculated age groups and income groups
- **fct_credit_performance**: Time-series credit performance with customer segmentation
- **credits_nps_linked**: Links credit outcomes to NPS for experience analysis

## Key Transformations

### Age Group Calculation
Customers are grouped by age as of the snapshot date:
- 18-25
- 26-35
- 36-45
- 46-55
- Above 55
- Unknown (missing DOB)

**Formula**: `(snapshot_date - date_of_birth) / 365.25`

### Income Group Calculation
Average monthly income is calculated and grouped:
- Below 5,000
- 5,000–9,999
- 10,000–19,999
- 20,000–29,999
- 30,000–49,999
- 50,000–99,999
- 100,000–149,999
- 150,000 and above

**Formula**: `(Received + Banks Received + Paybills Received) / Duration`

## Assumptions

1. **Income Sources**: All income columns (Received, Banks Received, Paybills Received) represent monthly flows
2. **Duration**: Represents loan duration in months
3. **Snapshot Data**: Each record represents point-in-time state, not cumulative history
4. **NPS Timing**: NPS scores are matched to loans by LOAN_ID without specific date correlation
5. **Data Quality**: Some records may have missing demographic data (handled with 'Unknown' groups)

## Data Quality Tests

The project includes built-in tests:
- **Not null checks**: Critical fields like loan_id, snapshot_date
- **Uniqueness**: Customer dimension has unique loan_ids
- **Referential integrity**: Foreign key relationships between staging and marts
- **Value validation**: NPS scores must be 0-10

## How to Use

### Prerequisites
- dbt Core installed (`pip install dbt-core dbt-<your-database>`)
- Database connection configured in `~/.dbt/profiles.yml`

### Setup
1. Configure your database connection in `profiles.yml`:
```yaml
mo_phones:
  target: dev
  outputs:
    dev:
      type: postgres  # or snowflake, bigquery, etc.
      host: localhost
      user: your_user
      password: your_password
      database: mo_phones
      schema: analytics
      threads: 4
```

2. Load sample data (optional for testing):
```bash
dbt seed
```

3. Run all models:
```bash
dbt run
```

4. Test data quality:
```bash
dbt test
```

5. Generate documentation:
```bash
dbt docs generate
dbt docs serve
```

### Development Workflow

1. **Add new sources**: Update `models/staging/schema.yml`
2. **Create staging models**: Add SQL files to `models/staging/`
3. **Build marts**: Create business logic in `models/marts/`
4. **Add tests**: Define tests in schema.yml files
5. **Document**: Add descriptions to all models and columns

## Sample Queries

### Portfolio Performance by Age Group
```sql
select 
    age_group,
    count(*) as account_count,
    avg(arrears) as avg_arrears,
    avg(days_past_due) as avg_days_past_due
from {{ ref('fct_credit_performance') }}
where snapshot_date = '2025-12-30'
group by age_group
order by avg_arrears;
```

### NPS by Account Status
```sql
select 
    account_status,
    avg(nps_score) as avg_nps,
    count(*) as response_count
from {{ ref('credits_nps_linked') }}
group by account_status
order by avg_nps desc;
```

### Income Group Risk Analysis
```sql
select 
    income_group,
    count(*) as total_accounts,
    sum(case when arrears > 0 then 1 else 0 end) as accounts_with_arrears,
    avg(arrears) as avg_arrears
from {{ ref('fct_credit_performance') }}
where snapshot_date = (select max(snapshot_date) from {{ ref('fct_credit_performance') }})
group by income_group
order by avg_arrears;
```

## Macros

### calculate_age_group(age_column)
Reusable macro for age group classification. Can be used in any model:
```sql
{{ calculate_age_group('customer_age') }} as age_group
```

### calculate_income_group(income_column)
Reusable macro for income group classification:
```sql
{{ calculate_income_group('monthly_income') }} as income_group
```

## Data Lineage

```
Raw Sources
    ├── credit_snapshots ──→ stg_credit_data ──┐
    ├── customer_info ──→ stg_demographics ──┐ │
    ├── income_details ──→ stg_income ────────┼─→ dim_customers ──┐
    └── nps_surveys ──→ stg_nps ──────────────┼──────────────────┼─→ fct_credit_performance
                                               │                  │
                                               └──────────────────┴─→ credits_nps_linked
```

## Production Deployment

### Recommended Schedule
- **Staging models**: Run daily after source data refresh
- **Dimension tables**: Run daily (SCD Type 2 for customer changes)
- **Fact tables**: Run daily for new snapshots
- **Analysis tables**: Run weekly or on-demand

### Monitoring
Set up alerts for:
- Model failures
- Test failures (especially uniqueness and not_null)
- Unexpected data volumes
- Long-running models

## Contributing

When adding new models:
1. Follow naming conventions: `stg_` for staging, `dim_` for dimensions, `fct_` for facts
2. Add comprehensive documentation in schema.yml
3. Include at least one test per model
4. Use macros for repeated logic
5. Add example queries to this README

## Support

For questions or issues:
- Review the main analysis report: [docs/CASE_STUDY_ANALYSIS.md](../docs/CASE_STUDY_ANALYSIS.md)
- Check dbt documentation: https://docs.getdbt.com
- Review model lineage: `dbt docs generate && dbt docs serve`

---

