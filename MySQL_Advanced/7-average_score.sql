-- creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student. Note: An average score can be a decimal

-- Requirements:
    -- Procedure ComputeAverageScoreForUser is taking 1 input:
        -- user_id, a users.id value (you can assume user_id is linked to an existing users)

-- (The procedure must output the score average
-- to the `users` table, using the `corrections table`)
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser (
    user_id INT NOT NULL
)
BEGIN
    UPDATE users SET average_score = (
        SELECT AVG(score) FROM corrections
        WHERE user_id=user_id
    ) WHERE id=user_id;
END$$
DELIMITER ;
