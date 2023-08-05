from turtle import *

s=Turtle() #object of turle
w=Screen() #object of screen

w.title("Smit rathod")
w.bgcolor("pink")

s.shape("classic")
s.color("red")
# s.begin_fill()
# s.forward(100)
# s.left(90)
# s.forward(50)
# s.left(90)
# s.forward(100)
# s.left(90)
# s.forward(50)
# s.end_fill()

def curve():
    for i in range(200):
        s.right(1)
        s.forward(1)

def love():
    s.begin_fill()
    s.left(140)
    s.fd(113)

    curve()
    s.left(120)
    curve()
    
    s.forward(112)
    s.end_fill()

def name():
    s.up()
    s.setpos(-68,95)
    s.color("pink")
    s.write("I Love U" ,font=("Arial",20,"bold"))    

love()
name()

done()