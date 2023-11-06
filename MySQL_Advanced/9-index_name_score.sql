-- Create an index `idx_name_first_score`
-- on the table named `names`, and the first letter of `name` and the `score`.
-- Requirements:
    -- Only the first letter of name AND score must be indexed

-- (We were given a massive file with a table, named `names`,
-- that has a `name` VARCHAR(255) DEFAULT NULL
-- and a `score` INT(11) DEFAULT NULL

CREATE INDEX idx_name_first_score
    ON names (name(1), score)
;
