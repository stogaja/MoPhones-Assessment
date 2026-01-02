{% macro calculate_income_group(income_column) %}
    case
        when {{ income_column }} < 5000 then 'Below 5,000'
        when {{ income_column }} between 5000 and 9999 then '5,000–9,999'
        when {{ income_column }} between 10000 and 19999 then '10,000–19,999'
        when {{ income_column }} between 20000 and 29999 then '20,000–29,999'
        when {{ income_column }} between 30000 and 49999 then '30,000–49,999'
        when {{ income_column }} between 50000 and 99999 then '50,000–99,999'
        when {{ income_column }} between 100000 and 149999 then '100,000–149,999'
        when {{ income_column }} >= 150000 then '150,000 and above'
        else 'Unknown'
    end
{% endmacro %}
