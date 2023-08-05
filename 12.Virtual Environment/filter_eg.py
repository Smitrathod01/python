from ast import Lambda


l=[1,2,3,4,5,6,7,8,9,0,15,55,45,67,889]

a=filter(lambda a:a%5==0,l)
print(list(a))