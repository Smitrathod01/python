Letter =''' Dear!! <Name>
You are selected...
Greetings from our company
<date>'''

name=input("Enter your name :\n")
date=input("Enter your date :\n")

Letter=Letter.replace("<Name>",name)
Letter=Letter.replace("<date>",date)

print(Letter)
