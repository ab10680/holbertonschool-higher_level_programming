-- Task 5: Create table unique_id with UNIQUE constraint on id

CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
