a = int(input("Enter your no : \n"))

prime=True
for i in range(2,a):
    if(a%i==0):
        prime=False
        break

if prime:
    print("Prime no")

else:
    print("Not a prime")
    