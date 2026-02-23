WITH fronttab as(
    SELECT ID, 1 as FRONT_END
    FROM DEVELOPERS as d
    WHERE EXISTS (
        SELECT 1
        FROM SKILLCODES as s
        WHERE s.CATEGORY LIKE "Front End"
            AND (d.SKILL_CODE & s.CODE) > 0
    )
),
pythontab as(
    SELECT ID, 1 as PYTHON
    FROM DEVELOPERS as d
    WHERE EXISTS (
        SELECT 1
        FROM SKILLCODES as s
        WHERE s.NAME LIKE "Python"
            AND (d.SKILL_CODE & s.CODE) > 0
    )
),
cstab as(
    SELECT ID, 1 as CSHARP
    FROM DEVELOPERS as d
    WHERE EXISTS (
        SELECT 1
        FROM SKILLCODES as s
        WHERE s.NAME LIKE "C#"
            AND (d.SKILL_CODE & s.CODE) > 0
    )
)


SELECT CASE
            WHEN FRONT_END=1 AND PYTHON=1 THEN "A"
            WHEN CSHARP=1 THEN "B"
            ELSE "C"
    END as GRADE,
    d.ID, d.EMAIL
From DEVELOPERS as d
LEFT JOIN fronttab as f
    ON d.ID = f.ID
LEFT JOIN pythontab as p
    ON d.ID = p.ID
LEFT JOIN cstab as c
    ON d.ID = c.ID
WHERE FRONT_END=1 OR (FRONT_END=1 AND PYTHON=1) OR CSHARP=1
ORDER BY GRADE ASC, ID ASC