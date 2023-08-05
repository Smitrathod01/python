for i in range(10):
    print(i)
    if i ==6:
     break #here after break loop will stop

else:
    print("bye")

#here else gets only executed if for loop succesfully gets executed in case of break it wont work

for i in range(10):
    
    if i ==6:
     continue
    print(i)

#here after continue the loop will forget about its down side and will continue so 6 will not get print 

i=0
if (i>5):
    pass
print("Hello")
#if we dont want to do anything in something then pass is used means do nothing.
