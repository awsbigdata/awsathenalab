import boto3
import time

client = boto3.client('athena',region_name='us-east-1')
dbname = "athenalabdb"

def submitQuery(query):
    #query="""SELECT * FROM lab_exe1"""
    print(query)
    res = client.start_query_execution(QueryString=query, QueryExecutionContext={'Database': dbname},
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


def executeQuery(query):
    res=submitQuery(query)
    result=waitForQueryToComplete(res['QueryExecutionId'])
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
