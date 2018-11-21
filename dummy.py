import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabledef import *
from com.awssupport.athenalab.dao import exerciseinput

from exercisedef import *

engine = create_engine('sqlite:///dbathena.db', echo=True)

# create a Session
Session = sessionmaker(bind=engine)
session = Session()

user = User("admin", "password")
session.add(user)



# commit the record the database
session.commit()



for i in exerciseinput.getQuery('q1'):
    print(i)
    exer=Exercise(i)
    session.add(exer)

session.commit()

