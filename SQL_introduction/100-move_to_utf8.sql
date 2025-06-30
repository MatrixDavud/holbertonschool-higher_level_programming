-- Convert the database, table, and the field into utf8
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

USE hbtn_0c_0;

ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

DROP TABLE IF EXISTS first_table;

CREATE TABLE first_table (
    id INT DEFAULT NULL,
    name VARCHAR(256) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
    score INT DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
