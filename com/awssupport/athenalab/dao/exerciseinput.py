def ex1():
    ex11table=[]
    ex11table.append({"id":"q11","groupid":"q1","desc":"How to solve Hive Schema mismatch error","run":"","result":"","comments":"","query":"SELECT * FROM lab_ex11 limit 2","editable":"false"})
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
    ex31table = []
    ex31table.append(
        {"id": "q31", "groupid": "q3", "desc": "Getting access denied error while running select query", "run": "", "result": "", "comments": "",
         "query": "SELECT * FROM lab_ex31 limit 2", "editable": "false"})
    ex31table.append({"id": "q32", "groupid": "q3",
                      "desc": "Getting s3 access denied error, although I have s3 full permission",
                      "run": "", "result": "", "comments": "", "query": "SELECT * FROM lab_ex32 limit 2",
                      "editable": "false"})

    return ex31table

def ex4():
    ex4table = []
    ex4table.append(
        {"id": "q41", "groupid": "q4", "desc": """Generate output as column a,b like below <table><tr><th>a</th><th>b</th></tr><tr><td>data1</td><td>data2</td></tr></table>""", "run": "",
         "result": "", "comments": "",
         "query": "select * from lab_ex41", "editable": "true"})
    ex4table.append({"id": "q42", "groupid": "q4",
                      "desc": "Convert below string to timestamp format as yyyy-mm-dd hh:mm:ss:sss",
                      "run": "", "result": "", "comments": "", "query": "select * from lab_ex42",
                      "editable": "true"})
    ex4table.append({"id": "q43", "groupid": "q4",
                      "desc": "Convert below string to timestamp format as mm/dd/yyyy",
                      "run": "", "result": "", "comments": "", "query": "select * from lab_ex43",
                      "editable": "true"})
    return ex4table

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