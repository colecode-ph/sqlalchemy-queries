# This file will use SQLAlchemy to run queries on a sqlite database and print them

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from puppydb_setup import Base, Shelter, Puppy

engine = create_engine('sqlite:///puppies.db')
# lets the program know which database we want to query
Base.metadata.bind = engine
# binds the engine to the Base class -
# this makes the connections between our class definitions
# and the corresponding tables in the database
DBSession = sessionmaker(bind = engine)
# creates a sessionmaker object, which establishes a link of
# communication between our code executions and the engine we created
session = DBSession()
# create an instance of the DBSession  object - to make a changeses
# to the database, we can call a method within the session

puppyNames = session.query(Puppy.name).order_by(Puppy.name)
for puppyName in puppyNames:
    print puppyName.name,