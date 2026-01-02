with credit as (
    select * from {{ ref('fct_credit_performance') }}
),

nps as (
    select * from {{ ref('stg_nps') }}
),

final as (
    select
        c.loan_id,
        c.snapshot_date,
        c.account_status,
        c.arrears,
        n.score as nps_score,
        n.survey_date
        
    from credit c
    inner join nps n on c.loan_id = n.loan_id
    -- Logic to match NPS date to relevant Credit Snapshot
    -- e.g., NPS date close to Snapshot date
)

select * from final
