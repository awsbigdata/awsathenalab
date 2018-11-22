from sqlalchemy import *

from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///dbathena.db', echo=True)
Base = declarative_base()


########################################################################
class User(Base):
    """"""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)


    # ----------------------------------------------------------------------
    def __init__(self, username, password):
        """"""
        self.username = username
        self.password = password


########################################################################
class ExerciseTopic(Base):
    """"""
    __tablename__ = "exercisestopic"

    id = Column(String, primary_key=True)
    property = Column(String)

    # ----------------------------------------------------------------------
    def __init__(self, id, property):
        """"""
        self.id = id
        self.property = property


########################################################################

class Exercise(Base):
    """"""
    __tablename__ = "exercises"

    id = Column(String, primary_key=True)
    groupid = Column(String)
    desc = Column(String)
    run = Column(String)
    comments = Column(String)
    result = Column(String)

    # ----------------------------------------------------------------------
    def __init__(self, dict):
        """"""
        self.id = dict['id']
        self.desc = dict['desc']
        self.comments = dict['comments']
        self.groupid = dict['groupid']
        self.result = dict['result']


# create tables
Base.metadata.create_all(engine)