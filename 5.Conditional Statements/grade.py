a=input("Enter your marks : \n")
a=int(a)

if(a>90):
    print("A grade")
elif(a>80 and a<90):
    print("B grade")
elif(a>70 and a<80):
    print("c grade")
elif(a>60 and a<70):
    print("d grade")
else:
    print("Fail")