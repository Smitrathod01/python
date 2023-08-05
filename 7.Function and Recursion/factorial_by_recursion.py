def factorial(num):
    if(num==0 or num==1):
         return 1
    else:
            return num*factorial(num-1)

a=int(input("Enter your no : \n"))

b=factorial(a)
print(b)