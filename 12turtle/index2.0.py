import turtle as t
import random

tim = t.Turtle()
tim.pensize(1)

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

# #testing
# for i in range(4):
#     tim.forward(100)
#     tim.right(90)
# tim.forward(100)
# tim.right(45)
# tim.forward(100)



def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.left(angle)

for shape_side_n in range(3, 10):
    tim.color(random.choice(colours))
    draw_shape(shape_side_n)




screen = t.Screen()
screen.exitonclick()