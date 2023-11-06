-- Create an index `idx_name_first`
-- on the table named `names`, and the first letter of `name`.
-- Requirements:
    -- Only the first letter of name must be indexed

-- (We were given a massive file with a table, named `names`,
-- that looks like this:

-- CREATE TABLE `names` (
-- `name` varchar(255) DEFAULT NULL,
-- `score` int(11) DEFAULT NULL
--) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE INDEX idx_name_first
    ON names (name(1))
;
