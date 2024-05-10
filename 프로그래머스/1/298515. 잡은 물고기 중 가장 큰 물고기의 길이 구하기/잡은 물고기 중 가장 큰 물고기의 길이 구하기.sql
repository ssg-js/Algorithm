-- 코드를 작성해주세요
select concat(cast(length AS NCHAR), 'cm') as 'MAX_LENGTH'
from fish_info
order by length desc limit 1;