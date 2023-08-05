import smtplib


name = "smit"
sur = "rathod"

a=f"i am {name} {sur}"
b="i am {} {}".format(name,sur) #used as f string
c="i am {1} {0}".format(name,sur) #will define the order

print(a)
print(b)
print(c)