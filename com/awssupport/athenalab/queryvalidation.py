from com.awssupport.athenalab import athenaQueryExecutor,exerciesQuery


def ex11(number):
    query = exerciesQuery.getQuery(number)
    out = athenaQueryExecutor.executeQuery(query)
    return responseformat(out=out)

def ex12(number):
    query = exerciesQuery.getQuery(number)
    out = athenaQueryExecutor.executeQuery(query)
    return responseformat(out=out)

def ex13(number):
    query = exerciesQuery.getQuery(number)
    out = athenaQueryExecutor.executeQuery(query)
    rs= responseformat(out=out)
    if(rs['status']=='SUCCEEDED'):
        out=athenaQueryExecutor.processresultset(rs['queryid'])
        if out[1]=='':
            rs['status']='FAILED'
            rs['message']='TimeStamp Column is Empty'
        return rs
    else:
        return rs

def ex14(number):
    query = exerciesQuery.getQuery(number)
    out = athenaQueryExecutor.executeQuery(query)
    return responseformat(out=out)

def ex15(number):
    query = exerciesQuery.getQuery(number)
    out = athenaQueryExecutor.executeQuery(query)
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


def responseformat(out):
    if out['QueryExecution']['Status']['State'] == 'SUCCEEDED':
       return {"status": out['QueryExecution']['Status']['State'],
         "message": 'ok',
         "queryid": out['QueryExecution']['QueryExecutionId']}
    else:
       return {"status": out['QueryExecution']['Status']['State'],
         "message": out['QueryExecution']['Status']['StateChangeReason'],
         "queryid": out['QueryExecution']['QueryExecutionId']}

def query_validation(argument):
    switcher = {
        'q11': ex11,
        'q12': ex12,
        'q13': ex13,
        'q14': ex14,
        'q15': ex15,

    }
    # Get the function from switcher dictionary
    func = switcher.get(argument, lambda: "Invalid month")
    # Execute the function
    return func(argument)





    #print(query_validation('q11'))