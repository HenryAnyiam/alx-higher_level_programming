-- lists all comedy show in the hbtn_0d_tvshows database
SELECT s.title FROM tv_shows AS s
INNER JOIN tv_show_genres AS t ON s.id = t.show_id
INNER JOIN tv_genres AS g ON g.id = t.show_id
WHERE g.name = 'Comedy' ORDER BY s.title;
