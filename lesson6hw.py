import turtle
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Art Design")

board = turtle.Turtle()
board.speed("fast")
board.hideturtle()

color = ["red","orange","yellow","lime","cyan"]
for i in range(180):
    board.color(color[i%len(color)])
    board.width(2)
    board.forward(i*2)
    board.right(91)

board.penup()
board.goto(0,180)
board.pendown()
board.color("lime")
board.begin_fill()
for i in range(360):
    board.forward(1)
    board.left(1)
board.end_fill()

board.penup()
board.goto(180,0)
board.pendown()
board.color("red")
board.begin_fill()
for i in range(360):
    board.forward(1)
    board.left(1)
board.end_fill()

board.penup()
board.goto(-180,0)
board.pendown()
board.color("orange")
board.begin_fill()
for i in range(360):
    board.forward(1)
    board.left(1)
board.end_fill()

board.penup()
board.goto(0,0)
board.pendown()
board.color("yellow")
board.begin_fill()
for i in range(360):
    board.forward(1)
    board.left(1)
board.end_fill()


turtle.done()