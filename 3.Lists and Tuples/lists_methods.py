a=[23,54,999,65,34,345]
#print(a.sort())  #we cant perform this way

a.sort()
print(a)

a.reverse()
print(a)

a.append(5)
print(a)

a.insert(1,1024) #will insert 1024 at index 1
print(a)

a.pop(1)
print(a)  #remove from index

a.remove(999)
print(a)  #remove actual value