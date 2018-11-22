import boto3
import time

glue = boto3.client('glue')
s3 = boto3.client('s3')
athena = boto3.client('athena')

def deleteDB(name):
    response = glue.get_databases()
    for dbname in response['DatabaseList']:
        if dbname['Name'] == name:
                response = glue.delete_database(Name=name)
    return response

def deleteS3bucket(name):
    print("bucket name")
    s3 = boto3.resource('s3')
    for eachbuk in s3.buckets.all():
        if 'athenalab' in eachbuk.name:
            if s3.Bucket(eachbuk.name) in s3.buckets.all():
                bucket = s3.Bucket(eachbuk.name)
                for key in bucket.objects.all():
                    key.delete()
                bucket.delete()


def deleteCrawler(name):
    response = glue.get_crawlers()
    res='none'
    for cname in response['Crawlers']:
        if cname['Name'] == name:
            print(cname['State'])
            while cname['State']!='READY':
                if(cname['State']=='RUNNING'):
                    response = glue.stop_crawler(Name=cname['Name'])
                time.sleep(5)
                cres=glue.get_crawler(Name=cname['Name'])
                cname=cres['Crawler']
            res = glue.delete_crawler(Name=name)
            print(res)
    return res

def ex14():
    return "SELECT * FROM lab_ex14 limit 2"

def ex15():
    return "SELECT * FROM lab_ex15 limit 2"

def cleanup(argument,name):
    switcher = {
        'dbname': deleteDB,
        's3bucket': deleteS3bucket,
        'crawlername': deleteCrawler,
        'q14': ex14,
        'q15': ex15,

    }
    # Get the function from switcher dictionary
    func = switcher.get(argument, lambda: "Invalid month")
    # Execute the function
    return func(name)
