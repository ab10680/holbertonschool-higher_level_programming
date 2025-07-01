-- Task 4: Create first_table if it doesn't exist
-- This script creates a table named first_table with id and name columns

CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
