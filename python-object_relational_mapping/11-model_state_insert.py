#!/usr/bin/python3
""" This script adds the State object 'Louisiana' to the database """
if __name__ == '__main__':
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()
    print(new_state.id)

    session.close()
