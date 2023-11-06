-- Create an index `idx_name_first`
-- on the table named `names`, and the first letter of `name`.
-- Requirements:
    -- Only the first letter of name must be indexed

-- (We were given a massive file with a table, named `names`,
-- that has a `name` VARCHAR(255) DEFAULT NULL
-- and a `score` INT(11) DEFAULT NULL

CREATE INDEX idx_name_first
    ON names (name(1))
;
