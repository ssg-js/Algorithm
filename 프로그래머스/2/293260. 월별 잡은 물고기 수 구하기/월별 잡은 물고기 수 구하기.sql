-- 코드를 작성해주세요
select count(*) as FISH_COUNT, cast(DATE_FORMAT(time, '%c') as UNSIGNED) as MONTH
from fish_info
group by MONTH
order by MONTH asc