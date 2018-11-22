
import sys
from sqlalchemy.orm import sessionmaker
from tabledef import *
from com.awssupport.athenalab.dao import exerciseinput
import json

import time


engine = create_engine('sqlite:///dbathena.db', echo=True)
Base = declarative_base()

# create tables
Base.metadata.create_all(engine)

# create a Session
Session = sessionmaker(bind=engine)
session = Session()
print(sys.argv[1])

user = User("admin", sys.argv[1])
session.add(user)


# commit the record the database
session.commit()


#ex1

for i in exerciseinput.getQuery('q1'):
    print(i)
    exer=Exercise(i)
    session.add(exer)

dbname="athenalabdb"
s3bucket="athenalab-{}".format(str(int(time.time())))

extopic=ExerciseTopic("q1",json.dumps({"dbname":dbname,"s3bucket":s3bucket,"crawlername":"Athena_labq1"}))
session.add(extopic)
session.commit()


