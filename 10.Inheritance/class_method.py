class Employee:
    salary=14
    company="google"

   # def changesalary(self,sal): #used to change salary at instance but actual class salary
     #   self.salary=sal     #wont change.

    #def changesalary(self,sal): 
      #  self.__class__.salary=sal  #used to change class salary

    @classmethod #decorator like static method            
    def changesalary(cls,sal):  #class method to change class salary
        cls.salary=sal

a=Employee()
print(Employee.salary)
a.changesalary(67)
print(a.salary)
print(Employee.salary)