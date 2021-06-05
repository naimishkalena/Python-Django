class publisher():

    def __init__(self,title):
        self.title = title
        print("Title : ",title)

class book(publisher):

    def __init__(self,page_no):
        print("Page No:",page_no)

class tape(publisher):

    def __init__(self,tfp):
        print("Time For Playing :",tfp)

pub = publisher("Naimish")
pub2 = book(75)
pub3= tape("2 hours")