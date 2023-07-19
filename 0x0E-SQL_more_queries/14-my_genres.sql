-- uses the hbtn_0d_tvshows database to list all genres of the Dexter show
SELECT g.name FROM tv_genres AS g
INNER JOIN tv_show_genres AS t ON g.id = t.genre_id
INNER JOIN tv_shows AS s ON s.id = t.show_id
WHERE s.title = 'Dexter' ORDER BY g.name;
