import turtle

screen = turtle.Screen()
screen.bgcolor("black")

spiral_turtle = turtle.Turtle()
spiral_turtle.speed(0)  
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

for i in range(100):
    spiral_turtle.color(colors[i % 6]) 
    spiral_turtle.forward(i * 10)  
    spiral_turtle.right(144)      

spiral_turtle.hideturtle()
turtle.done()
