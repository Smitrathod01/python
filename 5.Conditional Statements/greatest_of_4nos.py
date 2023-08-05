a=int(input("Enter number : \n"))
b=int(input("Enter number : \n"))
c=int(input("Enter number : \n"))
d=int(input("Enter number : \n"))

if(a>b and a>c and a>d):
    print("a is greatest")

if(b>a and b>c and b>d):
    print("b is greatest")

if(c>b and c>a and c>d):
    print("c is greatest")
    
if(d>b and d>c and d>a):
    print("d is greatest")