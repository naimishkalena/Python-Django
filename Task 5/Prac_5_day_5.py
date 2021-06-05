class employee:

    def __init__ (self,name,designation):
        self.name=name
        self.designation=designation

class subclass(employee):

    def __init__ (self,name,designation,salary):
        print("Name :",name,"\nDesignation :",designation,"\nSalary :",salary)

cf=subclass("Naimish","Web Developer","70000")