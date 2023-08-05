class Calculator:

    def __init__(self,num):
        self.num=num

    def square(self):
        print(f"{self.num**2}")
        
    def cube(self):
        print(f"{self.num**3}")

    @staticmethod
    def greet():
        print("thanks for using")

a=int(input("Enter a no : \n"))
b=Calculator(a)
b.square()
b.cube()
b.greet()