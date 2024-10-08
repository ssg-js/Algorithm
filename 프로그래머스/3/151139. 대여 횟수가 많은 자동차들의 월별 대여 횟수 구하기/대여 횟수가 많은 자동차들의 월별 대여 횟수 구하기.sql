-- 코드를 입력하세요
SELECT MONTH(A.START_DATE) AS MONTH, A.CAR_ID, COUNT(*) AS RECORDS
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY AS A
JOIN (
    SELECT CAR_ID
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE START_DATE BETWEEN "2022-08-01" AND "2022-10-31"
    GROUP BY CAR_ID
    HAVING COUNT(*) >= 5
) AS B
ON A.CAR_ID = B.CAR_ID
WHERE START_DATE BETWEEN "2022-08-01" AND "2022-10-31"
GROUP BY MONTH(A.START_DATE), A.CAR_ID
ORDER BY MONTH ASC, A.CAR_ID DESC