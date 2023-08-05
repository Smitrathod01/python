num=int(input("Enter your number : \n"))

for i in range(1,11):
    print(f"{num}x{i}={num*i}") #concept of f string
   # print(str(num)+"x"+str(i)+"="+str(num*i)) both are valid

i=1
while(i<11):
    print(str(num)+"x"+str(i)+"="+str(num*i))
    i=i+1
    



