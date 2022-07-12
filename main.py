from turtle import Turtle, Screen
screen = Screen()
import random

screen.setup(700, 700)

our_guess = screen.textinput("WINNER", "What is your guess about WINNER? Which colr do you think win in this race?")

turtle_list = ["tommy", "timmy", "burney", "boby", "roby"]

pace = [10, 15, 20, 25, 30, 35, 40]
turtles=[]
for turtle in turtle_list:
    turtle = Turtle()
    turtle.shape("turtle")
    turtles.append(turtle)




color_list = ["blue", "green", "red", "black", "purple"]

for i in range(5):
    turtles[i].color(color_list[i])

for _ in range(5):
    turtles[_].penup()
    turtles[_].goto(-250, -250+ 120* _)

match = True
while match == True:
    for _ in range(5):
        turtles[_].forward(random.choice(pace))

        if turtles[_].xcor()>300:
            match = False
            print(f"{color_list[_]} win this game")
            if our_guess == color_list[_]:
                   print(f"Congratultion you win the game!!!! by {color_list[_]}")
            else:
                 print("sorry you lose the  game")


screen.exitonclick()