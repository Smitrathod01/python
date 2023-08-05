class Employee:
    company="Google"
    salary=10000
    bonus=500
    #total=10500

    @property  #also known as getter
    def total(self):
        return self.salary+self.bonus

    @total.setter  #it will change bonus according to the total given below
    def total(self,val): #also known as setter
        self.bonus=val-self.salary

a=Employee()
print(a.total)#we will treat it as a attribute like company and salary bcoz it is a property
a.total=10600
print(a.total)
print(a.bonus)