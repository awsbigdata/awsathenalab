import boto3
import time
import sys

from botocore.errorfactory import *

client = boto3.client('athena')
dbname = "athenalabdb"

def submitQuery(query,stage,boto3client=None):
    print(query)
    if boto3client is not None:
        return execute(client, query, stage)
    return execute(client, query, stage)



def execute(client, query, stage):
    try:
        res = client.start_query_execution(QueryString=query, QueryExecutionContext={'Database': dbname},
                                           ResultConfiguration={'OutputLocation': 's3://{}/output'.format(stage)})
    except ClientError as e:
        print("Unexpected error:", e.response['Error'])
        res = {"status": "FAILED", "message": e.response['Error']}
    except:
        print("Unexpected error:", sys.exc_info())
        res = {"status": "FAILED", "message": "unknow error"}
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
        print(response)
        status = response['QueryExecution']['Status']['State']

    print("Execution completed")

    return response


def executeQuery(query,stage,boto3client=None):
    """Execute the Athena query and return the result"""
    res=submitQuery(query,stage,boto3client)
    print("resr",res)
    if('status' in res.keys() and res['status'] =='FAILED'):
        result=res
    else:
        result = waitForQueryToComplete(res['QueryExecutionId'])
    return result

def processresultset(queryid):
    res=client.get_query_results(QueryExecutionId=queryid,MaxResults=100)
    rows=[]
    for row in res['ResultSet']['Rows']:
        rows.append(processRows(row['Data'],res['ResultSet']['ResultSetMetadata']['ColumnInfo']))
    return rows;


def processRows(row,columninfo):
    return ','.join(str(v['VarCharValue'])  if 'VarCharValue' in v else str('') for v in row)


#print(processresultset('a02336c8-5f26-4709-90ab-fee4155a6d53'))
