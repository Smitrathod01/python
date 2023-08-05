def increament(num):
    try:
        return num+1
    except:
        raise ValueError("enter proper value")  #this is custom error

a=increament(56)
print(a)