import sys
from sqlalchemy.orm import sessionmaker
from tabledef import *
import json

import time
from com.awssupport.athenalab.mockdata.exercise1 import exercise1



def sample_data(s):
    options = []
    query = s.query(ExerciseTopic).filter(ExerciseTopic.id.__eq__('q1'))
    row = query.first()
    ex = exercise1(json.loads(row.property))
    ex.createdatabase()
    ex.createBucket()
    print(ex.exerciseMockData())




if __name__ == '__main__':
    engine = create_engine('sqlite:///dbathena.db', echo=True)
    Session = sessionmaker(bind=engine)
    s = Session()
    sample_data(s)