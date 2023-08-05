class Emp:   #dada
    company = "Google"

class Ere(Emp): #beta
    company = "microsoft"

class Ett(Ere): #pota
    company = "jaundu"

#for concerning values it will check for itself and then its clause class and at last the 
#remaining one.

a=Ett()
print(a.company)