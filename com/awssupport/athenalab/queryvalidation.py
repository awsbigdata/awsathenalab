from com.awssupport.athenalab import athenaQueryExecutor,exerciesQuery

import boto3
import datetime

def ex11(stage,ex_query):
    out = athenaQueryExecutor.executeQuery(ex_query,stage)
    return responseformat(out=out)

def ex12(stage,ex_query):
    out = athenaQueryExecutor.executeQuery(ex_query,stage)
    return responseformat(out=out)

def ex13(stage,ex_query):
    out = athenaQueryExecutor.executeQuery(ex_query,stage)
    rs= responseformat(out=out)
    if(rs['status']=='SUCCEEDED'):
        out=athenaQueryExecutor.processresultset(rs['queryid'])
        if out[1]=='':
            rs['status']='FAILED'
            rs['message']='TimeStamp Column is Empty'
        return rs
    else:
        return rs

def ex14(stage,ex_query):
    out = athenaQueryExecutor.executeQuery(ex_query,stage)
    return responseformat(out=out)

def ex15(stage,ex_query):
    out = athenaQueryExecutor.executeQuery(ex_query,stage)
    rs = responseformat(out=out)
    if (rs['status'] == 'SUCCEEDED'):
        out = athenaQueryExecutor.processresultset(rs['queryid'])
        print(out)
        if len(out) <2:
            rs['status'] = 'FAILED'
            rs['message'] = 'Zero Rows returned'
        else:
            rs['message']=out[1]
        return rs
    else:
        return rs

def ex2X(stage,ex_query):
    out = athenaQueryExecutor.executeQuery(ex_query,stage)
    if('status' in out.keys()):
       return out
    return responseformat(out=out)



def ex31(stage,ex_query):
    accountid=boto3.client('sts').get_caller_identity().get('Account')
    arn='arn:aws:iam::{}:role/Athena_Exercise_lab31_Role'.format(accountid)
    print(arn)
    session = role_arn_to_session(
        RoleArn=arn, RoleSessionName='lab_31'
    )
    client = session.client('athena')
    out = athenaQueryExecutor.executeQuery(ex_query,stage,client)
    return responseformat(out=out)

def ex32(stage,ex_query):
    accountid = boto3.client('sts').get_caller_identity().get('Account')
    arn='arn:aws:iam::{}:role/Athena_Exercise_lab32_Role'.format(accountid)

    session=role_arn_to_session(
        RoleArn=arn,RoleSessionName='lab_32'
    )
    client = session.client('athena')
    out = athenaQueryExecutor.executeQuery(ex_query,stage,client)
    return responseformat(out=out)


def ex41(stage,ex_query):
    out = athenaQueryExecutor.executeQuery(ex_query,stage)

    rs = responseformat(out=out)
    if (rs['status'] == 'SUCCEEDED'):
        out = athenaQueryExecutor.processresultset(rs['queryid'])
        print(out)
        if len(out) <1:
            rs['status'] = 'FAILED'
            rs['message'] = 'Zero Rows returned,perhaps, relauch the cf to fix the issue'
        else:
            if(len(out[1].split(','))==2):
                rs['message']=athenaQueryExecutor.tableConstruct(out)
            else:
                rs['status'] = 'FAILED'
                rs['message'] =out
        return rs
    else:
        return rs


def ex42(stage,ex_query):
    out = athenaQueryExecutor.executeQuery(ex_query,stage)
    rs = responseformat(out=out)
    if (rs['status'] == 'SUCCEEDED'):
        out = athenaQueryExecutor.processresultset(rs['queryid'])
        print(out)
        if len(out) <1:
            rs['status'] = 'FAILED'
            rs['message'] = 'Zero Rows returned,perhaps, relauch the cf to fix the issue'
        else:
            if(len(out)>=2):
                try:
                    validate(out[1],'%Y-%m-%d %H:%M:%S.%f')
                except:
                    rs['status'] = 'FAILED'
                    rs['message'] = out
                    return rs
                rs['message']=out[1]

            else:
                rs['status'] = 'FAILED'
                rs['message'] =out
        return rs
    else:
        return rs


def ex43(stage, ex_query):
    out = athenaQueryExecutor.executeQuery(ex_query, stage)
    rs = responseformat(out=out)
    if (rs['status'] == 'SUCCEEDED'):
        out = athenaQueryExecutor.processresultset(rs['queryid'])
        print(out)
        if len(out) < 1:
            rs['status'] = 'FAILED'
            rs['message'] = 'Zero Rows returned,perhaps, relauch the cf to fix the issue'
        else:
            if (len(out) >= 2):
                try:
                    validate(out[1], '%m/%d/%Y')
                except ValueError as e:
                    rs['status'] = 'FAILED'
                    rs['message'] = e.message+out
                    return rs
                rs['message'] = out[1]

            else:
                rs['status'] = 'FAILED'
                rs['message'] = out
        return rs
    else:
        return rs


def role_arn_to_session(**args):
    """
    Usage :
        session = role_arn_to_session(
            RoleArn='arn:aws:iam::012345678901:role/example-role',
            RoleSessionName='ExampleSessionName')
        client = session.client('sqs')
    """
    client = boto3.client('sts')
    response = client.assume_role(**args)
    return boto3.Session(
        aws_access_key_id=response['Credentials']['AccessKeyId'],
        aws_secret_access_key=response['Credentials']['SecretAccessKey'],
        aws_session_token=response['Credentials']['SessionToken'])

def responseformat(out):
    if out['QueryExecution']['Status']['State'] == 'SUCCEEDED':
       return {"status": out['QueryExecution']['Status']['State'],
         "message": 'ok',
         "queryid": out['QueryExecution']['QueryExecutionId']}
    else:
       return {"status": out['QueryExecution']['Status']['State'],
         "message": out['QueryExecution']['Status']['StateChangeReason'],
         "queryid": out['QueryExecution']['QueryExecutionId']}



def validate(date_text,format):
    try:
        datetime.datetime.strptime(date_text, format)
    except ValueError:
        raise ValueError("Incorrect data format, should be {}".format(format))


def query_validation(argument,stage,query):
    switcher = {
        'q11': ex11,
        'q12': ex12,
        'q13': ex13,
        'q14': ex14,
        'q15': ex15,
        'q21': ex2X,
        'q22': ex2X,
        'q23': ex2X,
        'q31': ex31,
        'q32': ex32,
        'q41': ex41,
        'q42': ex42,
        'q43': ex43


    }
    # Get the function from switcher dictionary
    func = switcher.get(argument, lambda: "Invalid month")
    # Execute the function
    return func(stage,query)





    #print(query_validation('q11'))