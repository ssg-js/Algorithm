-- 코드를 작성해주세요
select count(*) as fish_count, max(a.length) as max_length, a.fish_type
from fish_info as a
join (
    select fish_type
    from fish_info
    group by fish_type
    having avg(ifnull(length, 10)) >= 33
) as b
on a.fish_type = b.fish_type
group by a.fish_type
order by a.fish_type asc