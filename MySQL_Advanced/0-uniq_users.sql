-- Create a table 'users' that follows these following requirements:
-- id, integer, never null, auto increment and primary key
-- email, string (255 characters), never null and unique
-- name, string (255 characters)
CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT,
    email VARCHAR(255),
    name VARCHAR(255),
    PRIMARY KEY (id)
);
