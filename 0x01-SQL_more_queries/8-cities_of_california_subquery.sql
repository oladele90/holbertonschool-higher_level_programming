-- 8-cities_of_california_subquery.sql
-- lists all the cities of California that can be found 
SELECT id, name FROM cities WHERE state_id = (select id FROM states WHERE name = 'CALIFORNIA') ORDER BY (id) ASC;
