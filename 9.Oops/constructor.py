class Employee:
    
    def __init__(self,name,salary,unit): #it will run when object is created automatically
        self.name=name
        self.salary=salary
        self.unit=unit
        print("Employee is created!\n")

    def getdetails(self):
        print("Details are \n",end="")
        print(f"{self.name},{self.salary},{self.unit}\n ")

#smit = Employee() it is for check in self while init is created or not at object time when formed

smit=Employee("smit",13400,"human resource") #direct assigning.
venom=Employee("venom",12222,"marketing")

smit.getdetails()
venom.getdetails()
