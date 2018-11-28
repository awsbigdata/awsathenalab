
import sys
from sqlalchemy.orm import sessionmaker
from tabledef import *
from com.awssupport.athenalab.dao import exerciseinput
import json

import time


def user_data(session):
    print(sys.argv[1])
    user = User("admin", sys.argv[1])
    session.add(user)
    # commit the record the database
    session.commit()





#ex1

def exerciseData(session):
    for q in ('q1','q2','q3'):
        for i in exerciseinput.getQuery(q):
            print(i)
            exer = Exercise(i)
            session.add(exer)

        dbname = "athenalabdb"
        s3bucket = "athenalab-{}".format(str(int(time.time())))
        extopic = ExerciseTopic(q, json.dumps({"dbname": dbname, "s3bucket": s3bucket, "crawlername": "Athena_labq1"}))
        session.add(extopic)
        session.commit()




if __name__ == '__main__':
    engine = create_engine('sqlite:///dbathena.db', echo=True)
    Base = declarative_base()
    # create a Session
    Session = sessionmaker(bind=engine)
    session = Session()
    user_data(session)
    exerciseData(session)

