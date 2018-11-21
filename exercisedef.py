from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy.pool import SingletonThreadPool


engine = create_engine('sqlite:///dbathena.db', echo=True,poolclass=SingletonThreadPool)
Base = declarative_base()


########################################################################
class Exercise(Base):
    """"""
    __tablename__ = "exercises"

    id = Column(String, primary_key=True)
    groupid=Column(String)
    desc = Column(String)
    run = Column(String)
    comments= Column(String)
    result= Column(String)


    # ----------------------------------------------------------------------
    def __init__(self, dict):
        """"""
        self.id = dict['id']
        self.desc = dict['desc']
        self.comments=dict['comments']
        self.groupid=dict['groupid']
        self.result=dict['result']



# create tables
Base.metadata.create_all(engine)