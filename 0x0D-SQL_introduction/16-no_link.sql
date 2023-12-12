-- list all record in the database table 
SELECT score, name FROM second_table
WHERE name IS NOT NULL ORDER BY score DESC;
