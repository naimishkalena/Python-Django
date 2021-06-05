class cal1:
    def setData(self, n1, n2, n3):
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3

    def Display(self):
        sum = self.n1 + self.n2 + self.n3
        print("Sum of three number  : ", sum)


c = cal1()
c.setData(10, 20, 30)
c.Display()