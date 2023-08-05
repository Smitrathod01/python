import turtle

a=turtle.Turtle()
w=turtle.Screen()
w.bgcolor("black")
#a.pensize(2)
a.speed(0)
colors=["red","blue","green","pink","cyan","orange"]

for i in range(360):
        a.pencolor(colors[i%6])
        a.width(i//100+1)       
        a.forward(i)
        a.left(59)
            

turtle.done()