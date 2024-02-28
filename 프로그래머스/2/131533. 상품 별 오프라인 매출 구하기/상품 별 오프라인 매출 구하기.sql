-- 코드를 입력하세요
SELECT A.PRODUCT_CODE, B.SALES_SUM * A.PRICE AS SALES
FROM PRODUCT AS A 
JOIN
(SELECT PRODUCT_ID, SUM(SALES_AMOUNT) AS SALES_SUM
 FROM OFFLINE_SALE
 GROUP BY PRODUCT_ID
) AS B
ON A.PRODUCT_ID = B.PRODUCT_ID
ORDER BY SALES DESC, PRODUCT_CODE ASC
