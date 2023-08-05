a=10  #global variable
def fun():
    global a
    a=8 #local variable
    print(a)

fun()
print(a)#without global keyword it will print 10 but after global it will print 8