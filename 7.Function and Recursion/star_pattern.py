def pattern(a):
    i=0
    for i in range(a):
        print("*"*(a-i))

a=int(input("Enter no : \n"))
pattern(a)