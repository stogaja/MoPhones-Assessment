{% macro calculate_age_group(age_column) %}
    case
        when {{ age_column }} between 18 and 25 then '18-25'
        when {{ age_column }} between 26 and 35 then '26-35'
        when {{ age_column }} between 36 and 45 then '36-45'
        when {{ age_column }} between 46 and 55 then '46-55'
        when {{ age_column }} > 55 then 'Above 55'
        else 'Unknown'
    end
{% endmacro %}
