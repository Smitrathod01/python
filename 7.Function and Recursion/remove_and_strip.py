def ras(string, word):
    newstr=string.replace(word,"")
    return newstr.strip()

str="     I am not Invincible     "
a=ras(str,"not")
print(a)