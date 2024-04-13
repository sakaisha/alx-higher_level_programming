-- lists all cities contained in the database hbtn_0d_usa.
SELECT A.id, state_id AS name, A.name FROM cities A LEFT OUTER JOIN states B ON A.state_id = B.id ORDER BY A.id;
