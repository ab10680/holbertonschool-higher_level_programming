-- Task 12: Update Bob's score to 10 without using id
-- This script updates the score to 10 for the row where name is 'Bob'

UPDATE second_table
SET score = 10
WHERE name = 'Bob';
