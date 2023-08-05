class Person:
    def op(self):
        print("aa")

class Emp(Person):
    def op(self):
        super().op()
        print("bb")

class Prog(Emp):
    def op(self):
        super().op() #it is used to call the same function of its superclass means present in clause
        print("cc")   #it is also used in constructor only u have to write
                    #super().__init()
a=Person()
b=Emp()
c=Prog()
c.op()
