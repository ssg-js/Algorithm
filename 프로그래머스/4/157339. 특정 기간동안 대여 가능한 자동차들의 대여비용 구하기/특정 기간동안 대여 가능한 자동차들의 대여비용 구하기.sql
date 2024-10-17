-- 코드를 입력하세요
select a.car_id, a.car_type, floor(a.daily_fee * 30 * (100 - c.discount_rate) / 100) as fee
from (
    select car_id, car_type, daily_fee
    from car_rental_company_car
    where car_type = "세단" or car_type = "SUV"
) as a
left join (
    select car_id
    from car_rental_company_rental_history
    where ("2022-11-30" between start_date and end_date)
    or ("2022-11-01" between start_date and end_date)
    group by car_id
) as b
on a.car_id = b.car_id
join car_rental_company_discount_plan as c
on a.car_type = c.car_type and c.duration_type = "30일 이상"
where b.car_id is null
having fee >= 500000 and fee < 2000000
order by fee desc, a.car_type asc, a.car_id desc;