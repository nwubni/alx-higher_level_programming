#!/usr/bin/python3
"""
Create a database table from a SQLAlchemy model.
"""

import sys
from model_state import Base
from sqlalchemy import create_engine

if __name__ == "__main__":
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    connection_string = 'mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, password, database)

    engine = create_engine(connection_string, pool_pre_ping=True)
    Base.metadata.create_all(engine)
