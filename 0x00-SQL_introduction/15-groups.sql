-- 15-groups.sql
-- lists the number of records with the same score in the table
SELECT DISTINCT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY score DESC;
