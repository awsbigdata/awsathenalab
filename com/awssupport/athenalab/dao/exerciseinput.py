def ex1():
    ex11table=[]
    ex11table.append({"id":"q11","groupid":"q1","desc":"Hive Schema mismatch error","run":"","result":"","comments":"","query":"SELECT * FROM lab_ex11 limit 2","editable":"false"})
    ex11table.append({"id":"q12","groupid":"q1","desc":"How do I resolve the RegexSerDe error \"Number of matching groups doesn't match the number of columns\" in Amazon Athena?","run":"","result":"","comments":"","query":"SELECT * FROM lab_ex12 limit 2","editable":"false"})
    ex11table.append({"id":"q13","groupid":"q1","desc":"When I query a table in Amazon Athena, the TIMESTAMP result is empty","run":"","result":"","comments":"","query":"SELECT * FROM lab_ex13 limit 2","editable":"false"})
    ex11table.append({"id":"q14","groupid":"q1","desc":"When I try to read JSON data in Amazon Athena, I receive NULL or incorrect data errors. How can I resolve this?","run":"","result":"","comments":"","query":"SELECT * FROM lab_ex14 limit 2","editable":"false"})
    ex11table.append({"id":"q15","groupid":"q1","desc":"I created a table in Amazon Athena with defined partitions, but when I query the table, zero records are returned","run":"","result":"","comments":"","query":"SELECT * FROM lab_ex15 limit 2","editable":"false"})
    return ex11table

def ex2():
    ex2table = []
    query= """CREATE EXTERNAL TABLE `lab_ex21`(
                     `col1` string COMMENT '',
                     `col2` string COMMENT '',
                     col3` string COMMENT '',
                     `col4` string COMMENT '',
                     `col5` string COMMENT '',
                     `col6` string COMMENT '',
                     `col7` string COMMENT '')
    ROW
    FORMAT
    SERDE
    'org.apache.hadoop.hive.serde2.RegexSerDe'
    WITH
    SERDEPROPERTIES(
        'input.regex' = '^([0-9.]+) ([w.-]) ([w.-]) [([A-Za-z0-9:/]+ [+-][0-9]{4})] \"(.+?)\" ([0-9]+)$')
    STORED
    AS
    INPUTFORMAT
    'org.apache.hadoop.mapred.TextInputFormat'
    OUTPUTFORMAT
    'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
    LOCATION
    's3://athenalab-1543124020/athenalab/exer2/ex21'"""
    ex2table.append({"id": "q21", "groupid": "q2", "desc": "Table creation is failing, find the create table statement","query":query,"run":"", "result":"", "comments":"","editable":"true"})

    ex2table.append({"id": "q22", "groupid": "q2", "desc": "Table creation is failing, find the create table statement",
                     "query": """CREATE EXTERNAL TABLE lab_ex22(id int,name string )
                     LOCATION
                         'S3://athenalab-1543124020/athenalab/exer2/ex22'""","run":"","result":"","comments":"","editable":"true"})
    ex2table.append({"id": "q23", "groupid": "q2", "desc": "Table creation is failing, find the create table statement",
                     "query": """CREATE EXTERNAL TABLE `lab_ex-2-1`(id int,name string )
                        LOCATION
                            's3://athenalab-1543124020/athenalab/exer2/ex23'""", "run": "", "result": "",
                     "comments": "", "editable": "true"})

    return ex2table

def ex3():
    return "SELECT * FROM lab_ex13 limit 10"

def ex4():
    return "SELECT * FROM lab_ex14 limit 10"

def ex5():
    return "SELECT * FROM lab_ex15 limit 10"

def getQuery(argument):
    switcher = {
        'q1': ex1,
        'q2': ex2,
        'q3': ex3,
        'q4': ex4,
        'q5': ex5,

    }
    # Get the function from switcher dictionary
    func = switcher.get(argument, lambda: "Invalid month")
    # Execute the function
    return func()

#print(getQuery('q11'))