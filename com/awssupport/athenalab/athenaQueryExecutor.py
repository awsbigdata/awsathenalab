import boto3
import time

client = boto3.client('athena',region_name='us-east-1')

def submitQuery(query):
    #query="""SELECT * FROM lab_exe1"""
    print(query)
    res = client.start_query_execution(QueryString=query, QueryExecutionContext={'Database': 'hive_glue'},
                                      ResultConfiguration={'OutputLocation':'s3://testeastreg/output'})
    return res

def waitForQueryToComplete(queryid):
    time.sleep(1)
    response = client.get_query_execution(
        QueryExecutionId=queryid
    )
    status = response['QueryExecution']['Status']['State']
    print(status)

    while (status == "RUNNING"):
        time.sleep(3)
        response = client.get_query_execution(
            QueryExecutionId=queryid
        )
        status = response['QueryExecution']['Status']['State']

    print("Execution completed")

    return response


def executeQuery():
    res=submitQuery("SELECT * FROM lab_exe1")
    result=waitForQueryToComplete(res['QueryExecutionId'])
    return result
