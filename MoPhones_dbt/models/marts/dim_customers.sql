with demographics as (
    select * from {{ ref('stg_demographics') }}
),

income as (
    select * from {{ ref('stg_income') }}
),

final as (
    select
        d.loan_id,
        d.date_of_birth,
        d.gender,
        
        -- Income Calculation
        i.total_income_raw / nullif(i.duration, 0) as average_income,
        
        -- Use macro for income grouping
        {{ calculate_income_group('i.total_income_raw / nullif(i.duration, 0)') }} as income_group
        
    from demographics d
    left join income i on d.loan_id = i.loan_id
)

select * from final
