def fun(num):
    if num>2:
        return True
    else:
        return False

l = [1,2,3,4,5,6]

print(list(filter(fun,l)))

#by lambda
s=lambda num :num>3
print(list(filter(s,l)))