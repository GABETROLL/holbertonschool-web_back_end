-- creates a stored procedure AddBonus that adds a new correction for a student.
-- Requirements:
--  Procedure AddBonus is taking 3 inputs (in this order):
--   user_id, a users.id value (you can assume user_id is linked to an existing users)
--   project_name, a new or already exists projects - if no projects.name found in the table, you should create it
--   score, the score value for the correction

CREATE PROCEDURE AddBonus
    @user_id users.id,
    @project_name projects.name,
    @score INT DEFAULT 0
    AS
        INSERT INTO projects (name) VALUES (@project_name),
        INSERT INTO corrections (user_id, project_id, score) VALUES (
            @user_id,
            SELECT id FROM projects WHERE name = @project_name,
            @score
        )
GO;
