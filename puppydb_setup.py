# file to create puppy database with two tables 'puppy' and 'shelter'

from sqlalchemy import Column, ForeignKey, String, Integer, Date, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base() # define a class called 'Base' using the declarative_base function

class Shelter(Base):
    ''' create class Shelter to define parameters of a table in the db '''
    __tablename__ = 'shelter'
    id = Column(Integer, primary_key = True)
    name = Column(String(80), nullable = False)
    address = Column(String(250), nullable = False)
    city = Column(String(80), nullable = False)
    state = Column(String(47), nullable = False)
    zipCode = Column(String(10), nullable = False)
    website = Column(String)


class Puppy(Base):
    ''' create class Puppy to define parameters of a table in the db '''
    __tablename__ = 'puppy'
    id = Column(Integer, primary_key = True)
    name = Column(String(250), nullable = False)
    dateOfBirth = Column(Date)
    gender =  Column(String(6), nullable = False)
    weight = Column(Numeric(10))
    shelter_id = Column(Integer, ForeignKey('shelter.id'))
    shelter = relationship(Shelter)
    picture = Column(String)

engine = create_engine('sqlite:///puppies.db')

Base.metadata.create_all(engine)
