import boto3
import json
from datetime import date, datetime
import time

class exercise1():


    glue= boto3.client('glue')
    s3 = boto3.client('s3')
    athena = boto3.client('athena')
    dbname="athenalabdb"
    s3bucket="athenalab-{}".format(str(int(time.time())))
    prefix='athenalab/exer1/'
    crawlername='Athena_lab11'

    def __init__(self,prop):
        self.dbname=prop['dbname']
        self.s3bucket=prop['s3bucket']
        self.crawlername=prop['crawlername']

    def createBucket(self):
        print("bucketname:",self.s3bucket)
        self.s3.create_bucket(Bucket=self.s3bucket,CreateBucketConfiguration={
    'LocationConstraint': boto3.session.Session().region_name})

    def json_serial(obj):
        """JSON serializer for objects not serializable by default json code"""

        if isinstance(obj, (datetime, date)):
            return obj.isoformat()

    def createdatabase(self):
        response = self.glue.get_databases()
        print(self.dbname)
        for db in response['DatabaseList']:
            if db['Name'] == self.dbname:
                self.deleteDatabase()
        self.glue.create_database(DatabaseInput={'Name': self.dbname,'Description': 'it was created as part of Athena lab'})
        return True

    def copyJson(self):
        content = '{"name":"john","numbertest":10, "address":{ "location":"sydney","phone":{"test":"java"}}}'
        self.s3.put_object(Bucket=self.s3bucket, Key='{}{}'.format(self.prefix,'ex11/dt=20181010/test2.json'), Body=content)
        content = '{"name":"john","numbertest":10, "address":{ "location":"sydney"}}'
        self.s3.put_object(Bucket=self.s3bucket, Key='{}{}'.format(self.prefix,'ex11/dt=20181011/test2.json'), Body=content)

    def crawlerCreate(self):
        self.deleteCrawler()
        str = '{"Targets":{"JdbcTargets": [], "S3Targets": [{"Path": "'+"s3://{0}/{1}ex11/".format(self.s3bucket,self.prefix)+'", "Exclusions": []}], "DynamoDBTargets": []},  "Role": "Athena_Exercise_Glue_Role", "DatabaseName": "hive_glue", "SchemaChangePolicy": {"DeleteBehavior": "DEPRECATE_IN_DATABASE","UpdateBehavior": "UPDATE_IN_DATABASE"}, "TablePrefix": "lab_", "Classifiers": []}'
        crawlersetup = json.loads(str)
        response = self.glue.create_crawler(Name=self.crawlername, Role=crawlersetup['Role'],
                                            DatabaseName=self.dbname, Targets=crawlersetup['Targets'],
                                            TablePrefix=crawlersetup['TablePrefix'])

    def startCrawler(self):
        response = self.glue.start_crawler(Name=self.crawlername)

    def deleteDatabase(self):
        response = self.glue.get_databases()
        for dbname in response['DatabaseList']:
            if dbname['Name'] ==self.dbname:
                response = self.glue.delete_database(Name=self.dbname)

    def deletes3(self):
        s3 = boto3.resource('s3')
        if s3.Bucket(self.s3bucket) in s3.buckets.all():
         bucket = s3.Bucket(self.s3bucket)
         bucket.objects.filter(Prefix=self.prefix).delete()


    def deleteCrawler(self):
        response = self.glue.get_crawlers()
        for cname in response['Crawlers']:
            if cname['Name'] == self.crawlername:
                res=self.glue.delete_crawler(Name=self.crawlername)
                print(res)



    def createEx11(self):
        self.copyJson()
        self.crawlerCreate()
        self.startCrawler()

    def cleanup(self):
      #  self.deleteDatabase()
       # self.deletes3()
        self.deleteCrawler()
        print('clean up completed')

    def createEx12(self):
        content = '64.242.88.10 - - [07/Mar/2004:16:06:51 -0800] "GET /twiki/bin/rdiff/TWiki/NewUserTemplate?rev1=1.3&rev2=1.2 HTTP/1.1" 200 4523'
        self.s3.put_object(Bucket=self.s3bucket, Key='{}{}'.format(self.prefix, 'ex12/input.log'), Body=content)
        tablequery="CREATE external table lab_ex12(col1 string, col2 string, col3 string, col4 string, col5 string, col6 string, col7 string ) ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.RegexSerDe' WITH SERDEPROPERTIES ( 'input.regex' = '^([0-9.]+) ([\\w.-]) ([\\w.-]) \\[([A-Za-z0-9:/]+ [+-][0-9]{4})\\] \"(.+?)\" ([0-9]+)$') LOCATION"+"'s3://{}/{}ex12/'".format(self.s3bucket,self.prefix)
        res = self.athena.start_query_execution(QueryString=tablequery, QueryExecutionContext={'Database': self.dbname},
                                           ResultConfiguration={'OutputLocation': 's3://{}/stage/'.format(self.s3bucket)})
        print(res)

    def createEx13(self):
        content = """2018-11-17T09:58:35.374719Z\n2018-11-17T09:58:35.374719Z"""
        self.s3.put_object(Bucket=self.s3bucket, Key='{}{}'.format(self.prefix, 'ex13/input.log'), Body=content)
        tablequery="CREATE external table lab_ex13(`ts` timestamp) ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe' LOCATION"+"'s3://{}/{}ex13/'".format(self.s3bucket,self.prefix)
        res = self.athena.start_query_execution(QueryString=tablequery, QueryExecutionContext={'Database': self.dbname},
                                           ResultConfiguration={'OutputLocation': 's3://{}/stage/'.format(self.s3bucket)})
        print(res)

    def createEx14(self):
        content = '{"name":"john","numbertest":10, "address":{ "location":"sydney","phone":{"test":"java"}}}'
        self.s3.put_object(Bucket=self.s3bucket, Key='{}{}'.format(self.prefix, 'ex14/dt=20181010/test2.json'),
                           Body=content)
        content = '{"name":"john","numbertest":12, "address":{ "location":"sydney","phone":{"test":"java"}}'
        self.s3.put_object(Bucket=self.s3bucket, Key='{}{}'.format(self.prefix, 'ex14/dt=20181010/test4.json'),
                           Body=content)
        content = '{"name":"john","numbertest":10, "address":{ "location":"sydney"}}'
        self.s3.put_object(Bucket=self.s3bucket, Key='{}{}'.format(self.prefix, 'ex14/dt=20181011/test2.json'),
                           Body=content)
        tablequery="CREATE EXTERNAL TABLE `lab_ex14`(`name` string , `numbertest` bigint , `address` struct<location:string,phone:struct<test:string>> ) PARTITIONED BY (`dt` string) ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe' LOCATION"+"'s3://{}/{}ex14/'".format(self.s3bucket,self.prefix)
        res = self.athena.start_query_execution(QueryString=tablequery, QueryExecutionContext={'Database': self.dbname},
                                           ResultConfiguration={'OutputLocation': 's3://{}/stage/'.format(self.s3bucket)})
        time.sleep(5)
        res = self.athena.start_query_execution(QueryString="msck repair table lab_ex14", QueryExecutionContext={'Database': self.dbname},
                                                ResultConfiguration={
                                                    'OutputLocation': 's3://{}/stage/'.format(self.s3bucket)})
        print(res)

    def createEx15(self):
        content = '{"name":"john","numbertest":10, "address":{ "location":"sydney","phone":{"test":"java"}}}'
        self.s3.put_object(Bucket=self.s3bucket, Key='{}{}'.format(self.prefix, 'ex15/dt=20181010/test2.json'),
                           Body=content)

        content = '{"name":"john","numbertest":10, "address":{ "location":"sydney"}}'
        self.s3.put_object(Bucket=self.s3bucket, Key='{}{}'.format(self.prefix, 'ex15/dt=20181011/test2.json'),
                           Body=content)
        tablequery="CREATE EXTERNAL TABLE `lab_ex15`(`name` string , `numbertest` bigint , `address` struct<location:string,phone:struct<test:string>> ) PARTITIONED BY (`dt` string) ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe' LOCATION"+"'s3://{}/{}ex15/'".format(self.s3bucket,self.prefix)
        res = self.athena.start_query_execution(QueryString=tablequery, QueryExecutionContext={'Database': self.dbname},
                                           ResultConfiguration={'OutputLocation': 's3://{}/stage/'.format(self.s3bucket)})

        print(res)



    def cleanupex12(self):
        tablequery="drop table lab_ex12"
        res = self.athena.start_query_execution(QueryString=tablequery, QueryExecutionContext={'Database': self.dbname},
                                                ResultConfiguration={
                                                    'OutputLocation': 's3://{}/stage/'.format(self.s3bucket)})
    def cleanupex13(self):
        tablequery = "drop table lab_ex13"
        res = self.athena.start_query_execution(QueryString=tablequery, QueryExecutionContext={'Database': self.dbname},
                                                ResultConfiguration={
                                                    'OutputLocation': 's3://{}/stage/'.format(self.s3bucket)})

    def exerciseMockData(self):
        self.createEx11()
        self.createEx12()
        self.createEx13()
        self.createEx14()
        self.createEx15()
        out={}
        out['S3bucket']=self.s3bucket
        out['database']=self.dbname
        return out
