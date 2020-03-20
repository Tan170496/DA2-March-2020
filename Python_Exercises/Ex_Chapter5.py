import turtle
wn = turtle.Screen()

tan = turtle.Turtle()

distance = 10
tan.forward(distance)
tan.left(90)
distance = distance + 10



wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.color("blue")
tess.shape("turtle")
tess.penup()

for size in range(10):
    tess.forward(50)
    tess.stamp()
    tess.forward(-50)
    tess.right(36)
    
    



tan = turtle.Turtle()
for size in range(100):
    print("we like Python's turtles!")
wn.exitonclick()