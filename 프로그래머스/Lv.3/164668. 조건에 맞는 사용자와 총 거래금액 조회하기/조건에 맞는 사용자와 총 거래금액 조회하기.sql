-- 코드를 입력하세요
SELECT A.USER_ID, A.NICKNAME, B.TOTAL_PRICE
FROM USED_GOODS_USER AS A
INNER JOIN (
    SELECT WRITER_ID, SUM(PRICE) AS TOTAL_PRICE
    FROM USED_GOODS_BOARD
    WHERE USED_GOODS_BOARD.STATUS = 'DONE'
    GROUP BY WRITER_ID
) AS B
ON A.USER_ID = B.WRITER_ID
WHERE B.TOTAL_PRICE >= 700000
ORDER BY B.TOTAL_PRICE ASC;