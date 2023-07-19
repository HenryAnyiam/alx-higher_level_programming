-- lists all shows and genres linked to the show
-- in the hbtn_0d_tvshows database
SELECT s.title, g.name FROM tv_shows AS s
LEFT JOIN tv_show_genres AS t ON s.id = t.show_id
LEFT JOIN tv_genres AS g ON t.genre_id = g.id
ORDER BY s.title, g.name;
