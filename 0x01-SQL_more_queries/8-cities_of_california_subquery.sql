-- 8-cities_of_california_subquery.sql
-- lists all the cities of California that can be found 
SELECT id, name FROM cities WHERE (select id FROM states WHERE id = state_id) ORDER BY (id);
