-- Script that creates a table called 'first_table'
-- first_table Description:
-- 	id: INT
-- 	name: VARCHAR(256)
-- If it already exists, script should not fail
-- Not allowed to use SELECT or SHOW statements
CREATE TABLE IF NOT EXISTS first_table(id INT, name VARCHAR(256));
