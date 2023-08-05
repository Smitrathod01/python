class Employee:
    company="Google"
    def take(self):
        print("a")

class Emp(Employee): #derived class
    company="microsoft"

    def ok(self):
        print("b")

a=Employee()
b=Emp()

b.take()
print(b)
b.ok()
print(b)
#when derived class has no cooresponding values or attributes then it will take from parent class
#or base class and if both have that same class then owned value or attribute carried out

