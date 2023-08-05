from ctypes import cdll
from this import d
from tkinter import E


class emp:
    company = "Google"

class ere:
    company = "microsoft"

class ett(emp,ere): #derived class form two parent class
    company = "jaundu"

c=emp()
d=ere()
e=ett()
print(e.company)
#if e has no company then it will take company of emp bcoz we have write its name at first
#in clause of ett means it will concerns about that class first and then check fot the other class
#in short 1st it will check in its own class then emp and ere.