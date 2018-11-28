from com.awssupport.athenalab import athenaQueryExecutor,exerciesQuery


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

def ex21(stage,ex_query):
    out = athenaQueryExecutor.executeQuery(ex_query,stage)
    if('status' in out.keys()):
       return out
    return responseformat(out=out)

def ex22(stage,ex_query):
    out = athenaQueryExecutor.executeQuery(ex_query,stage)
    if('status' in out.keys()):
       return out
    return responseformat(out=out)



def responseformat(out):
    if out['QueryExecution']['Status']['State'] == 'SUCCEEDED':
       return {"status": out['QueryExecution']['Status']['State'],
         "message": 'ok',
         "queryid": out['QueryExecution']['QueryExecutionId']}
    else:
       return {"status": out['QueryExecution']['Status']['State'],
         "message": out['QueryExecution']['Status']['StateChangeReason'],
         "queryid": out['QueryExecution']['QueryExecutionId']}

def query_validation(argument,stage,query):
    switcher = {
        'q11': ex11,
        'q12': ex12,
        'q13': ex13,
        'q14': ex14,
        'q15': ex15,
        'q21': ex21,
        'q22': ex22,


    }
    # Get the function from switcher dictionary
    func = switcher.get(argument, lambda: "Invalid month")
    # Execute the function
    return func(stage,query)





    #print(query_validation('q11'))