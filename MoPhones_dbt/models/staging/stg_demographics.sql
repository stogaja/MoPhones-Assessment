with source as (
    select * from {{ source('heavy_raw', 'customer_info') }}
),

cleaned as (
    select
        loan_id,
        cast(date_of_birth as date) as date_of_birth,
        gender
    from source
)

select * from cleaned
