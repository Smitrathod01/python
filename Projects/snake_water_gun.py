import random

def game(a,b):
    if(a=='s' and b=='w'):
        print("you are winner")
    elif(a=='s' and b=='g'):
        print("you are loser")
    elif(a=='w' and b=='s'):
        print("you are loser")
    elif(a=='w' and b=='g'):
        print("you are winner")
    elif(a=='g' and b=='w'):
        print("you are loser")
    elif(a=='g' and b=='s'):
        print("you are winner")
    else:
        print("tie")

comp=0
b=random.randint(1,3)
if(b==1):
    comp='s'
elif(b==2):
    comp='w'
elif(b==3):
    comp='g'

a=input("Choose snake(s),water(w) or gun(g) : \n")

print(f"you have chosed {a} and comp has chosen {comp} so \n")
game(a,comp)


