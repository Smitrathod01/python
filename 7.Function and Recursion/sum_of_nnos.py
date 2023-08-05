def nat(a):
    if(a==1):
        return 1
    else:
         return a+nat(a-1)

a=int(input("Enter youur no : \n"))

b=nat(a)
print(b)