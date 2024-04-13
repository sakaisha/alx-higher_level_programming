-- uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
SELECT title, SUM(rate) AS rating FROM tv_shows LEFT JOIN (tv_show_ratings) ON (tv_shows.id = tv_show_ratings.show_id) GROUP BY title ORDER BY rating DESC;
