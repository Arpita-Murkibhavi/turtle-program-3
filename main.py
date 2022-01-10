from flask import Flask, render_template
from turtle import Turtle, Screen
import random
# import requests

app = Flask(__name__)

@app.route('/')
def home() :
    return "<h1>Hello world</h1>"

@app.route('/turtle')
def tim() :

    is_race_on = False
    screen = Screen()
    screen.setup(width=500, height=400)
    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    y_positions = [-70, -40, -10, 20, 50, 80]
    all_turtles = []

#Create 6 turtles
    for turtle_index in range(0, 6):
        new_turtle = Turtle(shape="turtle")
        new_turtle.penup()
        new_turtle.color(colors[turtle_index])
        new_turtle.goto(x=-230, y=y_positions[turtle_index])
        all_turtles.append(new_turtle)

    if user_bet:
        is_race_on = True

    while is_race_on:
        for turtle in all_turtles:
            #230 is 250 - half the width of the turtle.
                if turtle.xcor() > 230:
                    is_race_on = False
                    winning_color = turtle.pencolor()
                    if winning_color == user_bet :
                       return '<h1> YOU WON!!</h1>'

                    else :
                        return '<h1> YOU LOST!!</h1>'
                        # print(f")
                           #Make each turtle move a random amount.
                rand_distance = random.randint(0, 10)
                turtle.forward(rand_distance)

    screen.exitonclick()



if __name__ == "__main__":
    #Run the app in debug mode to auto-reload
    app.run(debug=True)