
def ex11():
    return "SELECT * FROM lab_ex11 limit 10"

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

print(getQuery('q1'))