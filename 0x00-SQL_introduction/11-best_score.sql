-- 11-best_score.sql
--  lists all records with a score >= 10
SELECT score, name FROM second_table WHERE score > 9 ORDER BY score DESC;
