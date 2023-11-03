-- Using the table named 'metal_bands' from 'metal_bands.sql',
-- Write a SQL script that ranks country origins of bands, ordered by the number of (non-unique) fans
-- Requirements:
--  Column names must be: origin and nb_fans
--  Your script can be executed on any database
SELECT
    origin    AS origin,
    SUM(fans) AS nb_fans
    FROM metal_bands
    GROUP BY origin
;
