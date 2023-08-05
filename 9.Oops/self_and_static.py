class Employee:
    company="Google"
    def getsalary(self): #self is used to assign object name in field u can use more args in this clause like sign
        print(f"salary is {self.salary}")    #and then write that sign in smit.getsalary clause

    @staticmethod #used to execute without self
    def greet():
        print("Good morning")

smit=Employee()
smit.salary=346456
smit.getsalary()
# Employee.getsalary(smit) both are same it is used without self in def....
smit.greet()