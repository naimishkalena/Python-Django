class cal2:
    def setData(self,r):
        self._rad = r

    def area(self):
        self._Total_Area = 3.14*self._rad*self._rad

    def Display(self):
        print("Area of circle is ",self._Total_Area)



c = cal2()
c.setData(12)
c.area()
c.Display()