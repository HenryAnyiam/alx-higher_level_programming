-- list all data in second_table with a name column
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
