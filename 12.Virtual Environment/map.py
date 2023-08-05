from sqlite3 import SQLITE_UPDATE


def sqrt(num):
    return num*num

l = [2,4,5,7]

#method 1
l2=[]
for item in l:
    l2.append(sqrt(item))

print(l2)

#method 2 
print(list(map(sqrt,l)))

