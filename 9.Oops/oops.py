class Employee: #always write first letter in capital in class name
       company="Google"

smit=Employee()  #its an object derived from class
smit.salary=20000  #instance attribute bcoz it doesnt made in class
print(smit.salary)
print(smit.company) #class attribute bcoz it was made in class
 
#we can change class attribute value in instance attribute like..
smit.company="microsoft"
print(smit.company)