#!/usr/bin/python3
"""Write a script that takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa"""
if __name__ == '__main__':
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT A.name FROM cities A LEFT OUTER JOIN states B" +
                " ON A.state_id = B.id WHERE B.name = %s ORDER BY A.id",
                (argv[4],))
    lis = [citi[0] for citi in cur.fetchall()]
    print("{}".format(", ".join(lis)))
    cur.close()
    db.close()
