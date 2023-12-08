from turtle import Turtle, Screen
import random
screen=Screen()
screen.setup(width=500, height=400)
user_bet=screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour among red, orange, yellow, green, purple, blue: ")
colors=["red", "orange", "yellow", "green", "purple", "blue"]

def extra(tur):
    tur.shape("turtle")
    turtle_colour = random.choice(colors)
    tur.color(turtle_colour)
    colors.remove(turtle_colour)
    tur.penup()

all_turtle=[]
y_cor=-100
for num in range(6):
    tony=Turtle()
    extra(tony)
    tony.goto(x=-230, y=y_cor)
    y_cor+=40
    all_turtle.append(tony)

is_bet_on=True
while is_bet_on:
    for num in range(6):
        all_turtle[num].forward(random.randint(0,10))
        if all_turtle[num].xcor() >= 230:
            winner_turtle_colour=all_turtle[num].pencolor()
            if user_bet==winner_turtle_colour:
                print(f"You have won! the {winner_turtle_colour} turtle is the winner.")
            else:
                print(f"You have lost! the {winner_turtle_colour} turtle is the winner.")
            is_bet_on=False


screen.exitonclick()


######## ___"Two or more Objects of Same Class can have the Same Name"___ #####
#### Example of above statement:-

# from turtle import Turtle, Screen
# screen=Screen()
# tonn2=Turtle()
# tonn2.color("red")
# tonn2.forward(100)
# tonn2=Turtle()
# tonn2.color("blue")
#
# screen.exitonclick()