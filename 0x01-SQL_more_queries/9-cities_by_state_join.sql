-- 9-cities_by_state_join.sql
--  lists all cities contained in the database
SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states WHERE state_id = states.id ORDER BY (cities.id);
