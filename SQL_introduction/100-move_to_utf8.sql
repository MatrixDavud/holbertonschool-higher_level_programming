-- Convert the database, table, and the field into utf8
-- Select the database first
USE hbtn_0c_0;

-- Convert the database default charset and collation
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Convert the table charset and collation, including all text columns
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Specifically modify the 'name' field to set the collation only (no charset needed explicitly)
ALTER TABLE first_table MODIFY name VARCHAR(256) COLLATE utf8mb4_unicode_ci DEFAULT NULL;

