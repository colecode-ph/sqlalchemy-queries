# This file will use SQLAlchemy to run queries on a sqlite database and print them
from datetime import date
from dateutil.relativedelta import relativedelta

from sqlalchemy import create_engine, func
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
# create an instance of the DBSession  object - to make a changes
# to the database, we can call a method within the session


def alpha_query():
    print "1. Query all of the puppies and print the results in ascending alphabetical order.\n"

    puppyNames = session.query(Puppy.name).order_by(Puppy.name)
    for puppyName in puppyNames:
        print puppyName.name,
    print "\n"


def bday_query():
    print "2. Query all puppies (and birthdates) that are less than 6 months old organized by the youngest first.\n"
    today = date.today()
    sixMonthsAgo = today + relativedelta(months=-6)
    puppyNames = (session.query(Puppy.name, Puppy.dateOfBirth)
                 .filter(Puppy.dateOfBirth > sixMonthsAgo)
                 .order_by(Puppy.dateOfBirth.desc()))
    for puppyName in puppyNames:
        print puppyName.name + " - " + str(puppyName.dateOfBirth)
    print "\n"


def weight_query():
    print "3. Query the name and weight of the ten heaviest puppies in descending order by weight.\n"
    puppyNames = session.query(Puppy.name, Puppy.weight).order_by(Puppy.weight.desc()).limit(10)
    for puppyName in puppyNames:
        print puppyName.name + " - " + str(puppyName.weight) + "lbs"
    print "\n"


def shelter_query():
    print "4. Query all puppies grouped by the shelter in which they are staying.\n"
    shelterCounts = (session.query(Shelter.name, func.count(Puppy.name).label("count"))
                    .join(Puppy, Shelter.id == Puppy.shelter_id)
                    .group_by(Shelter.name))
    for shelterName in shelterCounts:
        print shelterName.name + " - " + str(shelterName.count)

if __name__ == '__main__':
    alpha_query()
    bday_query()
    weight_query()
    shelter_query()
    session.close()
