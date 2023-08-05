class Complex:
    def __init__(self,num1,num2) -> None:
        self.num1=num1
        self.num2=num2

    def __add__(self,c):
        return Complex(self.num1+c.num1,self.num2+c.num2)

    def __mul__(self,c):
        mulreal=(self.num1*c.num1) - (self.num2*c.num2)
        mulimg=(self.num1*c.num2) - (self.num2*c.num1)
        return Complex(mulreal,mulimg)

    def __str__(self) -> str:
        return f"{self.num1}+i{self.num2}"

a=Complex(3,5)
b=Complex(3,5)
sum=(a+b)
mul=(a*b)
print(mul)
print(sum)
        