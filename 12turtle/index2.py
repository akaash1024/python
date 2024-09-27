import turtle as t
import random
from turtle import Screen

tim = t.Turtle()
t.colormode(255) #need to apply before move ahead

# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

#  instead of
def randomColors():
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)
    randomColor = (red,green,blue)
    return randomColor

directions = [0, 90, 180, 270]
tim.pensize(15)
# tim.speed("fastest")

for _ in range(100):
    # tim.color(random.choice(colours))
    tim.color(randomColors())
    tim.forward(40)
    tim.setheading(random.choice(directions))












screen = Screen()
screen.exitonclick()