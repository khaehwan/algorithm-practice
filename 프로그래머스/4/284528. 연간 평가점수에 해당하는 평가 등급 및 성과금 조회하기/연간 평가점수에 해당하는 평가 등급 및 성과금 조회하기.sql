WITH gradetab as(
    SELECT EMP_NO,
        CASE
            WHEN AVG(SCORE) >= 96 THEN "S"
            WHEN AVG(SCORE) >= 90 THEN "A"
            WHEN AVG(SCORE) >= 80 THEN "B"
            ELSE "C"
        END as GRADE
    FROM HR_GRADE
    GROUP BY EMP_NO
)

SELECT g.EMP_NO, e.EMP_NAME, g.GRADE,
    CASE g.GRADE
        WHEN "S" THEN e.SAL*0.20
        WHEN "A" THEN e.SAL*0.15
        WHEN "B" THEN e.SAL*0.10
        ELSE 0
    END as BONUS
FROM gradetab as g
JOIN HR_EMPLOYEES as e
    ON g.EMP_NO = e.EMP_NO
ORDER BY EMP_NO ASC