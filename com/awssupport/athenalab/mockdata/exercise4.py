import boto3
import json
from datetime import date, datetime
import time

class Exer4():


    glue= boto3.client('glue')
    s3 = boto3.client('s3')
    athena = boto3.client('athena')
    dbname="athenalabdb"
    s3bucket="athenalab-{}".format(str(int(time.time())))
    prefix='athenalab/exer4/'


    def __init__(self,prop):
        self.dbname=prop['dbname']
        self.s3bucket=prop['s3bucket']




    def json_serial(obj):
        """JSON serializer for objects not serializable by default json code"""

        if isinstance(obj, (datetime, date)):
            return obj.isoformat()




    def createEx41(self):
        content = '{"records":[{"a":"data1","b":"data2"},{"a":"data4","b":"data5"},{"a":"data7","b":"data8"}]}'
        self.s3.put_object(Bucket=self.s3bucket, Key='{}{}'.format(self.prefix, 'ex41/input.json'), Body=content)
        tablequery="CREATE external TABLE lab_ex41 (  records array<struct<a:string,b:string>>  ) ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe' LOCATION"+"'s3://{}/{}ex41/'".format(self.s3bucket,self.prefix)
        res = self.athena.start_query_execution(QueryString=tablequery, QueryExecutionContext={'Database': self.dbname},
                                           ResultConfiguration={'OutputLocation': 's3://{}/stage/'.format(self.s3bucket)})
        print(res)



    def createEx42(self):
        content = '20180721T025005'
        self.s3.put_object(Bucket=self.s3bucket, Key='{}{}'.format(self.prefix, 'ex42/server.log'),
                           Body=content)

        tablequery="CREATE EXTERNAL TABLE `lab_ex42`(logtime string ) LOCATION"+"'s3://{}/{}ex42/'".format(self.s3bucket,self.prefix)
        res = self.athena.start_query_execution(QueryString=tablequery, QueryExecutionContext={'Database': self.dbname},
                                           ResultConfiguration={'OutputLocation': 's3://{}/stage/'.format(self.s3bucket)})
    def createEx43(self):
        content = '1544518667000'
        self.s3.put_object(Bucket=self.s3bucket, Key='{}{}'.format(self.prefix, 'ex43/test2.json'),
                           Body=content,ServerSideEncryption='aws:kms')

        tablequery="CREATE EXTERNAL TABLE `lab_ex43`(logtime string) LOCATION"+"'s3://{}/{}ex43/'".format(self.s3bucket,self.prefix)
        res = self.athena.start_query_execution(QueryString=tablequery, QueryExecutionContext={'Database': self.dbname},
                                           ResultConfiguration={'OutputLocation': 's3://{}/stage/'.format(self.s3bucket)})




    def exerciseMockData(self):
        self.createEx41()
        self.createEx42()
        self.createEx43()
        out={}
        out['S3bucket']=self.s3bucket
        out['database']=self.dbname
        return out
