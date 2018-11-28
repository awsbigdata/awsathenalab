import boto3
import json
from datetime import date, datetime
import time

class Exer3():


    glue= boto3.client('glue')
    s3 = boto3.client('s3')
    athena = boto3.client('athena')
    dbname="athenalabdb"
    s3bucket="athenalab-{}".format(str(int(time.time())))
    prefix='athenalab/exer3/'


    def __init__(self,prop):
        self.dbname=prop['dbname']
        self.s3bucket=prop['s3bucket']




    def json_serial(obj):
        """JSON serializer for objects not serializable by default json code"""

        if isinstance(obj, (datetime, date)):
            return obj.isoformat()




    def createEx31(self):
        content = '64.242.88.10 - - [07/Mar/2004:16:06:51 -0800] "GET /twiki/bin/rdiff/TWiki/NewUserTemplate?rev1=1.3&rev2=1.2 HTTP/1.1" 200 4523'
        self.s3.put_object(Bucket=self.s3bucket, Key='{}{}'.format(self.prefix, 'ex31/input.log'), Body=content)
        tablequery="CREATE external table lab_ex31(col1 string, col2 string, col3 string, col4 string, col5 string, col6 string, col7 string ) ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.RegexSerDe' WITH SERDEPROPERTIES ( 'input.regex' = '^([0-9.]+) ([\\\w.-]) ([\\\w.-]) \\\[([A-Za-z0-9:/]+ [+-][0-9]{4})\\\] \\\"(.+?)\\\" ([0-9]{3}) ([0-9]+)$') LOCATION"+"'s3://{}/{}ex31/'".format(self.s3bucket,self.prefix)
        res = self.athena.start_query_execution(QueryString=tablequery, QueryExecutionContext={'Database': self.dbname},
                                           ResultConfiguration={'OutputLocation': 's3://{}/stage/'.format(self.s3bucket)})
        print(res)



    def createEx32(self):
        content = '{"name":"john","numbertest":10, "address":{ "location":"sydney","phone":{"test":"java"}}}'
        self.s3.put_object(Bucket=self.s3bucket, Key='{}{}'.format(self.prefix, 'ex32/test2.json'),
                           Body=content,ServerSideEncryption='aws:kms')

        tablequery="CREATE EXTERNAL TABLE `lab_ex32`(`name` string , `numbertest` bigint , `address` struct<location:string,phone:struct<test:string>> ) ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe' LOCATION"+"'s3://{}/{}ex32/'".format(self.s3bucket,self.prefix)
        res = self.athena.start_query_execution(QueryString=tablequery, QueryExecutionContext={'Database': self.dbname},
                                           ResultConfiguration={'OutputLocation': 's3://{}/stage/'.format(self.s3bucket)})




    def exerciseMockData(self):
        self.createEx31()
        self.createEx32()
        out={}
        out['S3bucket']=self.s3bucket
        out['database']=self.dbname
        return out
