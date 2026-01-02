with source as (
    select * from {{ source('heavy_raw', 'nps_surveys') }}
),

cleaned as (
    select
        loan_id,
        score,
        date as survey_date
    from source
)

select * from cleaned
