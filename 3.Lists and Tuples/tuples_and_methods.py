a=()    #empty tuple
b=(1,)  #singular tuple cant be created without an comma
c=(12,34,56,75,12,34,12)   #tuple with many values 

#c[0]=99 # unlike lists we can't modify elements in tuples
print(c)

print(c.count(12))  #count no of 12

print(c.index(12))  #shows us in which index that element is present and only first element is considered