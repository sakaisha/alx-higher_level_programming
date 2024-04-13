-- lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
SELECT A.title, B.genre_id FROM tv_shows A LEFT JOIN tv_show_genres B ON A.id = B.show_id ORDER BY A.title, B.genre_id;
