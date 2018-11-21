
def ex11():
    return "SELECT * FROM lab_ex11 limit 2"

def ex12():
    return "SELECT * FROM lab_ex12 limit 2"

def ex13():
    return "SELECT * FROM lab_ex13 limit 2"

def ex14():
    return "SELECT * FROM lab_ex14 limit 2"

def ex15():
    return "SELECT * FROM lab_ex15 limit 2"

def getQuery(argument):
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
    return func()

print(getQuery('q11'))