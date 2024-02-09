import turtle
from turtle import Turtle, Screen
import random

#etch-a-sketch
#tim = Turtle()
#screen = Screen()
# def move_forwards():
#     tim.forward(10)
#
#
# def move_backwards():
#     tim.backward(10)
#
#
# def move_clockwise():
#     tim.right(10)
#
#
# def move_counterclockwise():
#     tim.left(10)
#
#
# screen.listen()
# screen.onkey(move_forwards, "W")
# screen.onkey(move_backwards, "S")
# screen.onkey(move_clockwise, "D")
# screen.onkey(move_counterclockwise, "A")
# screen.onkey(tim.reset, "C")
bar = Turtle()

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet",
                            prompt="Which turtle will win the race? Enter a color from rainbow: ")
is_race_on = False

bar.hideturtle()
bar.penup()
bar.goto(230, -85)
bar.pendown()
bar.setheading(90)
bar.forward(180)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=-75 + 30 * turtle_index)
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

        if turtle.xcor() > 212:
            winning_color = turtle.pencolor()
            is_race_on = False
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner.")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner.")
            break


screen.exitonclick()
