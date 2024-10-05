import turtle as t
import random
from turtle import Screen

tim = t.Turtle()
t.colormode(255) #need to apply before move ahead




def randomColors():
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)
    color = (red,green,blue)
    return color


tim.speed("fastest")



def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(randomColors())
        tim.circle(100)

        # current_Heading = tim.heading()
        # tim.setheading(current_Heading+10) 

        # tim.setheading(tim.heading()+10)

        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)























screen = Screen()
screen.exitonclick()