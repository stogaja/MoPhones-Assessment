with source as (
    select * from {{ source('heavy_raw', 'income_details') }}
),

calculated as (
    select
        loan_id,
        duration,
        -- Assuming raw columns exist
        coalesce(received, 0) + coalesce(banks_received, 0) + coalesce(paybills_received, 0) as total_income_raw
    from source
)

select * from calculated
