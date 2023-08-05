import random

a=random.randint(1,101)
guess=1


for i in range(1,30):
    b=int(input("Enter your number : \n"))
    if(b>a):
        print("lower number pls!\n")

    elif(b<a):
        print("Highr numer please!\n")

    elif(a==b):
        print("Perfect guess!\n")
        print(f"you have guessed it {guess} attempts!")
        break
    guess=guess+1
      
   
print("End of chances")

with open("hiscore.txt","r") as f:
    hiscore=int(f.read())

if(guess<hiscore)    :
    print(f"Congo u have just broke a record of {hiscore}")
    with open("hiscore.txt","w") as f:
        f.write(str(guess))