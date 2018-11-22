import sys
from sqlalchemy.orm import sessionmaker
from tabledef import *
import json

import time
from com.awssupport.athenalab.mockdata.exercise1 import exercise1

engine = create_engine('sqlite:///dbathena.db', echo=True)
Session = sessionmaker(bind=engine)
s = Session()
options = []
query = s.query(ExerciseTopic).filter(ExerciseTopic.id.__eq__('q1'))
row=query.first()
ex=exercise1(json.loads(row.property))
ex.cleanup()
ex.createdatabase()
ex.createBucket()
print(ex.exerciseMockData())