a=[12,34,56,4,3,6,7,8,45,67,89]
#b=[]

#for i in a:
 #   if i%2==0:
  #      b.append(i)

#print(b)

b = [i for i in a if i%2==0]
print(b)

#it will work for set and dictionary also