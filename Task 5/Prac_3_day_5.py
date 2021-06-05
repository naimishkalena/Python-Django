class cal3:
    def __init__(self,P,R,T):
        self.n1=P
        self.n2=R
        self.n3=T

    def callInterest(self):
        self.Interest = ((self.n1*self.n2*self.n3)/100)

    def display(self):
        print("Interest of given value is ",self.Interest)

c=cal3(1000,1,2)
c.callInterest()
c.display()