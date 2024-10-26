import turtle

screen = turtle.Screen()
screen.bgcolor("white")

donut = turtle.Turtle()
donut.shape("turtle")
donut.speed(0) 
donut.width(2)
donut.color("purple")

for i in range(36):  
    donut.circle(100) 
    donut.right(10)  

donut.hideturtle()
turtle.done()
