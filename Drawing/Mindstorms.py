import turtle

def draw_squares():
    window = turtle.Screen()
    window.bgcolor("black")

    box = turtle.Turtle()
    box.shape("arrow")
    box.color("red")
    box.speed(10)
    box.pensize(2)

    box_dist = [100,75,50,25,5,-5,-25,-50,-75,-100]
    box_list_count = len(box_dist)
    count = 0

    while count < box_list_count:

        x = box_dist.pop()
        i = 0
        z = 0
        for i in range(4):
            box.forward(x)
            box.right(90)
            i += 1
            
        for z in range(4):
            box.forward(x)
            box.left(90)
            z += 1            

        count += 1

    x = [-12.5,12.5,-25,25,-37.5,37.5,-50,50]
    x_count = len(x)
    print("x_count is ")

    box.speed(10)

    for i in range(x_count):
        box.circle(x.pop())
        i += 1

    box.hideturtle()

    window.exitonclick()
    
draw_squares()
