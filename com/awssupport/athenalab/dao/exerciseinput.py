def ex11():
    ex11table=[]
    ex11table.append({"id":"q11","groupid":"q1","desc":"Hive Schema mismatch error","run":"","result":"","comments":""})
    ex11table.append({"id":"q12","groupid":"q1","desc":"How do I resolve the RegexSerDe error \"Number of matching groups doesn't match the number of columns\" in Amazon Athena?","run":"","result":"","comments":""})
    ex11table.append({"id":"q13","groupid":"q1","desc":"When I query a table in Amazon Athena, the TIMESTAMP result is empty","run":"","result":"","comments":""})
    ex11table.append({"id":"q14","groupid":"q1","desc":"When I try to read JSON data in Amazon Athena, I receive NULL or incorrect data errors. How can I resolve this?","run":"","result":"","comments":""})
    ex11table.append({"id":"q15","groupid":"q1","desc":"I created a table in Amazon Athena with defined partitions, but when I query the table, zero records are returned","run":"","result":"","comments":""})
    return ex11table

def ex12():
    return "SELECT * FROM lab_ex12 limit 10"

def ex13():
    return "SELECT * FROM lab_ex13 limit 10"

def ex14():
    return "SELECT * FROM lab_ex14 limit 10"

def ex15():
    return "SELECT * FROM lab_ex15 limit 10"

def getQuery(argument):
    switcher = {
        'q1': ex11,
        'q2': ex12,
        'q3': ex13,
        'q4': ex14,
        'q5': ex15,

    }
    # Get the function from switcher dictionary
    func = switcher.get(argument, lambda: "Invalid month")
    # Execute the function
    return func()

#print(getQuery('q11'))