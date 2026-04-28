-- ✅ Step 1: Database உருவாக்கு
CREATE DATABASE IF NOT EXISTS auth_db;
USE auth_db;

-- ✅ Step 2: Users table உருவாக்கு
CREATE TABLE IF NOT EXISTS users (
    id       INT AUTO_INCREMENT PRIMARY KEY,
    name     VARCHAR(100)  NOT NULL,
    userid   VARCHAR(50)   NOT NULL UNIQUE,
    password VARCHAR(256)  NOT NULL,
    mobile   VARCHAR(15)   NOT NULL,
    email    VARCHAR(150)  NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ✅ Confirm
SELECT "Database மற்றும் Table ready!" AS status;
