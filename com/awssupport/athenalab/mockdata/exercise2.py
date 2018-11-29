import boto3
import json
from datetime import date, datetime
import time

class Exer2():


    glue= boto3.client('glue')
    s3 = boto3.client('s3')
    athena = boto3.client('athena')
    dbname="athenalabdb"
    s3bucket="athenalab-{}".format(str(int(time.time())))
    prefix='athenalab/exer2/'


    def __init__(self,prop):
        self.dbname=prop['dbname']
        self.s3bucket=prop['s3bucket']




    def json_serial(obj):
        """JSON serializer for objects not serializable by default json code"""

        if isinstance(obj, (datetime, date)):
            return obj.isoformat()




    def createEx41(self):
        content = '{"records":[{"a":"data1","b":"data2"},{"a":"data4","b":"data5"},{"a":"data7","b":"data8"}]}'
        self.s3.put_object(Bucket=self.s3bucket, Key='{}{}'.format(self.prefix, 'ex21/input.json'), Body=content)
        self.s3.put_object(Bucket=self.s3bucket, Key='{}{}'.format(self.prefix, 'ex22/input.json'), Body=content)
        self.s3.put_object(Bucket=self.s3bucket, Key='{}{}'.format(self.prefix, 'ex23/input.json'), Body=content)



    def exerciseMockData(self):
        self.createEx41()

        out={}
        out['S3bucket']=self.s3bucket
        out['database']=self.dbname
        return out
