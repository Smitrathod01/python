a="good morning, "
b="smit"
c=a+b
print(c)#also we can write in print directly that a+b without c

name="smit"
print(name[1])#it will print m

#we cant change characters by this method like name[0]=b 

print(name[1:4])#last char will be excluded means thre values are gonna print
#[:4] is same as [0:4] and [0:] is same as [0:4] it concerns the border value
#Also the last character of any word/string starts from -1 lke

print(name[-1]) #it will print t
print(name[-3:-1])#will print mi

name="IamInvincible"
d=name[0::2]#it will go to end because end value is empty and every 2nd value will be skipped
print(d)