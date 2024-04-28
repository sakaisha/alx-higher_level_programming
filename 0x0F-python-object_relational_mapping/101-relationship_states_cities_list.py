#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, relationship, backref

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine, checkfirst=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    flag = 0
    st_id_remember = 0
    for st in (session.query(State).order_by(State.id).all()):
        print("{}: {}".format(st.id, st.name))
        for ct in st.cities:
            print("\t{}: {}".format(ct.id, ct.name))
    session.commit()
    session.close()
