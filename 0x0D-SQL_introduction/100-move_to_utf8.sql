-- Script that converts hbtn_0c_0 database to UTF* in MySQL server
-- Convert Database hbtn_0c_0, Table first_table, Field name in first_table to UTF8

ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE hbtn_0c_0;
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
