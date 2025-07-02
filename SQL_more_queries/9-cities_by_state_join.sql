-- Task 9: List all cities with their state name using a single SELECT

SELECT cities.id, cities.name, states.name
FROM cities, states
WHERE cities.state_id = states.id
ORDER BY cities.id ASC;
