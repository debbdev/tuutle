import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=1000, height=600)
screen.bgpic('asset/road.gif')
user_bet = screen.textinput("Turtle Race", "Pick Turtle Color")
ALIGN = "right"
FONT = ("courier", 28, "bold")

y_positions = [-260, -172, -85, 2, 85, 172, 260]
colors = ["yellow", "blue", "red", "purple", "green", "orange", "brown"]
all_turtles = []

for i in range(0, 7):
    new_tuu = Turtle(shape='turtle')
    new_tuu.shapesize(2)
    new_tuu.speed('fastest')
    new_tuu.penup()
    new_tuu.goto(x=-340, y=y_positions[i])
    new_tuu.color(colors[i])
    all_turtles.append(new_tuu)

on_move = True
while on_move:
    for turtle in all_turtles:
        if turtle.xcor() > 350:
            on_move = False
            winner = turtle.pencolor()
            if winner == user_bet:
                turtle.write(f"You won!!, {winner} turtle won", font=FONT, align=ALIGN)
            else:
                turtle.write(f"You lost!, The {winner} turtle is the winner", font=FONT, align=ALIGN)
        turtle_pace = random.randint(0, 20)
        turtle.forward(turtle_pace)

screen.exitonclick()
