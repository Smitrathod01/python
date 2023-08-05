class Number:

    def __init__(self,num1) -> None:
        self.num=num1

    def __add__(self,num2): 
        print("lets add")
        return self.num + num2.num
    
    def __mul__(self,num2):
        print("lets mul")
        return self.num*num2.num

    def __str__(self):
        return f"no is {self.num}"

    def __len__(self):
        return 1 #by default will return 1 for values

a=Number(6)
print(a) #wont return 6 to overcome this str is used
print(len(a))