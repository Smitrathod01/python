a=set()

a.add(4)
a.add(7)
# a.add(9,8) #wont work only takes one argument at one time
# a.add([2,34,54]) #wont work because list cant be inserted into set bcoz unhasable nor dicionary
a.add((1,9,8))  #nested set as maths
print(a)  

print(len(a))

a.remove(7)
print(a)

print(a.pop()) #removes an arbir=tary value means random

print(a.clear()) #empties a set
print(a)

#for two set there is also an union and intersection format is xyz.union/intersection({x,y,z})
