import turtle 

ninja = turtle.Turtle()
window = turtle.Screen()

ninja.speed(0)
ninja.color("red")
ninja.pensize(1)

window.bgcolor("black")

for i in range(180):
    ninja.forward(100)
    ninja.right(30)
    ninja.forward(20)
    ninja.left(60)
    ninja.forward(50)
    ninja.right(30)
    
    ninja.penup()
    ninja.setposition(0, 0)
    ninja.pendown()
    
    ninja.right(2)
    


turtle.done()
