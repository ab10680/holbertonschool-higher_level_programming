-- Task 11: List records with score >= 10 ordered descending
-- This script selects score and name from second_table where score >= 10

SELECT score, name FROM second_table
WHERE score >= 10
ORDER BY score DESC;
