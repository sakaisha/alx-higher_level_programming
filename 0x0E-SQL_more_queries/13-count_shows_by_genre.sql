-- lists all genres in the database hbtn_0d_tvshows_rate by their rating.
SELECT name AS genre, COUNT(genre_id) AS number_of_shows FROM tv_genres RIGHT JOIN tv_show_genres ON id = genre_id GROUP BY genre_id ORDER BY number_of_shows DESC;
