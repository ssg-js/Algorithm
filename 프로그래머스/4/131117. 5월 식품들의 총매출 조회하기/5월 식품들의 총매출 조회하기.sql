-- 코드를 입력하세요
select a.product_id, a.product_name, (a.price * b.sales) as total_sales
from food_product as a
join (
    select product_id, sum(amount) as sales
    from food_order
    where year(produce_date) = 2022 and month(produce_date) = 5
    group by product_id
) as b
on a.product_id = b.product_id
order by total_sales desc, a.product_id asc;