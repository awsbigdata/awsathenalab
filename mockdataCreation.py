import boto3

from com.awssupport.athenalab.mockdata.exercise1 import exercise1

ex=exercise1()
ex.cleanup()
ex.createdatabase()
ex.createBucket()
print(ex.exerciseMockData())