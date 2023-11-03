-- From the table named 'metal_bands',
-- list all bands with "Glam rock" as their main style, ranked by their longevity.
-- Requirements:
--  Use the 'metal_bands.sql' table dump
--  Column names must be: band_name and lifespan (in years)
--  You should use attributes formed and split for computing the lifespan
--  Your script can be executed on any database
SELECT band_name
        FROM metal_bands
        WHERE style LIKE "%Glam rock%"
;
