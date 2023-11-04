-- creates a stored procedure AddBonus that adds a new correction for a student.
-- Requirements:
--  Procedure AddBonus is taking 3 inputs (in this order):
--   user_id, a users.id value
--    (you can assume user_id is linked to an existing users)
--   project_name, a name of a project with the same data type as
--    'projects.name'. If it doesn't already exist in the table,
--    you should create it.
--   score, the score value for the correction

-- I'M ASSUMING THAT 'projects' HAS NO REPEATING 'name's,
-- WHEN QUERYING THE ID FROM 'projects' TO ADD TO 'corrections'.
-- IT SELECTS FROM MAX. ONE ROW WHERE `name`=project_name
-- FROM PROJECTS 'projects' TO VERIFY THAT THE PROJECT
-- IS ALREADY PRESENT.
DELIMITER $$
CREATE PROCEDURE AddBonus (
    user_id INT,
    project_name VARCHAR(255),
    score INT
)
BEGIN
    INSERT INTO projects (`name`)
        SELECT project_name
        WHERE NOT EXISTS (
            SELECT `name` FROM projects
            WHERE `name`=project_name
        ) LIMIT 1
    ;
    INSERT INTO corrections (user_id, project_id, score) VALUES (
        user_id,
        (SELECT id FROM projects WHERE `name`=project_name),
        score
    );
END$$
DELIMITER ;
