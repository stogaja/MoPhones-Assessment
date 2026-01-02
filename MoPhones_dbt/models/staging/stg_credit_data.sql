with source as (
    select * from {{ source('heavy_raw', 'credit_snapshots') }}
),

renamed as (
    select
        LOAN_ID as loan_id,
        cast(DATE as date) as snapshot_date,
        TOTAL_PAID as total_paid,
        TOTAL_DUE_TODAY as total_due_today,
        BALANCE as balance,
        DAYS_PAST_DUE as days_past_due,
        ACCOUNT_STATUS_L1 as account_status,
        ARREARS as arrears
    from source
)

select * from renamed
