from turtle import *

a=Turtle()
b=Screen()
b.bgcolor("black")
a.pensize(4)
a.speed(10)

for i in range(6):
    for colors in ["yellow","pink","cyan","blue","red","green"]:
        a.color(colors)

        a.circle(100)
        a.left(10)

done()