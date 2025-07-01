-- Task 16: List all records with non-empty name
-- This script lists score and name where name is not null and not empty

SELECT score, name FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
