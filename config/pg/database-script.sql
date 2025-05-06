
CREATE SCHEMA db1;

ALTER ROLE user1 SET search_path TO db1;

CREATE TABLE db1.user_table (
    USER_NAME VARCHAR(255),
    USER_CATEGORY VARCHAR(255)
);

INSERT INTO db1.user_table (USER_NAME, USER_CATEGORY) VALUES
('Alice', 'A'),
('Bob', 'B'),
('Charlie', 'A'),
('Alice2', 'A'),
('Bob2', 'B'),
('Charlie2', 'A'),
('Alice3', 'A'),
('Bob3', 'B'),
('Charlie3', 'A');






