with credit_data as (
    select * from {{ ref('stg_credit_data') }}
),

customers as (
    select * from {{ ref('dim_customers') }}
),

final as (
    select
        c.loan_id,
        c.snapshot_date,
        c.total_paid,
        c.total_due_today,
        c.balance,
        c.days_past_due,
        c.account_status,
        c.arrears,
        
        cust.date_of_birth,
        cust.income_group,
        cust.average_income,
        
        -- Age Calculation
        datediff(year, cust.date_of_birth, c.snapshot_date) as customer_age,
        
        -- Use macro for age grouping
        {{ calculate_age_group('datediff(year, cust.date_of_birth, c.snapshot_date)') }} as age_group

    from credit_data c
    left join customers cust on c.loan_id = cust.loan_id
)

select * from final
