-- Task 15: Count number of records per score
-- This script groups by score and counts the number of rows for each score

SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
