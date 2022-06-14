import datetime
def date():
    current = datetime.datetime.now()
    return(str(current.date()))
def time():
    current = datetime.datetime.now()
    return(str(current.time()))