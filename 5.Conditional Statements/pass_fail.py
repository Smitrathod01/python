mat=int(input("Enter your marks : \n"))
phy=int(input("Enter your marks : \n"))
chem=int(input("Enter your marks : \n"))
total=(mat+phy+chem)/3

if(total>40 and mat>=33 and phy>=33 and chem>=33):
    print("Pass")

else:
    print("Fail")

#another way is to use if elif and else
#in if write about 33 in each subj with or
#in elif total
#in else pass..