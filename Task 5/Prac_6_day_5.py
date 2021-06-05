class cal5:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def calArea(self):
        self.Ans = self.length * self.breadth

    def display(self):
        print("Area of rectangle : ",self.Ans)


c= cal5(8,9)
c.calArea()
c.display()