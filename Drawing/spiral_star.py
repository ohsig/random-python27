import turtle 

spiral = turtle.Turtle()
spiral.pencolor("red")
spiral.pensize(2)
spiral.speed(750)
window = turtle.Screen()

window.bgcolor("black")

for i in range(350):
    spiral.forward(i * 10)
    spiral.right(144)

spiral = turtle.Turtle()
spiral.pencolor("black")
spiral.pensize(2)
spiral.speed(750)
window = turtle.Screen()

window.bgcolor("black")

for i in range(350):
    spiral.forward(i * 10)
    spiral.right(144)


painter = turtle.Turtle()

painter.pencolor("blue")
painter.pensize(2)
painter.speed(200)

for i in range(150):
    painter.forward(250)
    painter.left(123) # Let's go counterclockwise this time 
    
painter.pencolor("red")
for i in range(150):
    painter.forward(250)
    painter.left(123)

painter.pencolor("black")

for i in range(150):
    painter.forward(250)
    painter.left(123) # Let's go counterclockwise this time 


print("Last black painter")    
painter.pencolor("black")
for i in range(250):
    painter.forward(100)
    painter.left(123)
    
turtle.done()
