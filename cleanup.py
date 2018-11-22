import boto3

glue = boto3.client('glue')
s3 = boto3.client('s3')
athena = boto3.client('athena')

def deleteDB(name):
    response = glue.get_databases()
    for dbname in response['DatabaseList']:
        if dbname['Name'] == name:
                response = glue.delete_database(name)
    return response

def deleteS3bucket(name):
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(name)
    for key in bucket.objects.all():
        key.delete()
    bucket.delete()
    return "SELECT * FROM lab_ex12 limit 2"

def deleteCrawler(name):
    response = glue.get_crawlers()
    res='none'
    for cname in response['Crawlers']:
        if cname['Name'] == name:
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
