class Number:

    def __init__(self,num1) -> None:
        self.num=num1

    def __add__(self,num2): #this are also known as dunder method
        print("lets add")
        return self.num + num2.num
    
    def __mul__(self,num2):
        print("lets mul")
        return self.num*num2.num

a=Number(5)
b=Number(6)
sum=a+b
mul=a*b
print(sum)
print(mul)

#__truediv__ for division
#likewise,sub for substraction floordiv for //
        