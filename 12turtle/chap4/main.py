from turtle import Turtle, Screen

# Set up the screen
screen = Screen()
screen.setup(width=1200, height=600)
screen.title("Dinoo")
screen.tracer(0)  # Disable automatic updates

# First turtle
dino = Turtle()
dino.shape("classic")
dino.color("red")
dino.penup()
dino.goto(-580, 0)
dino.pendown()

# Moving the red turtle across the screen
for i in range(2):
    dino.forward(580)
    screen.update()  # Update the screen after each move

# Second turtle
dinoOne = Turtle()
dinoOne.shape("triangle")
dinoOne.color("black")
dinoOne.penup()
dinoOne.goto(-580, 20)
screen.update()

# Function to move the black turtle when "Up" key is pressed
def move_up_down():
    dinoOne.setheading(45)  
    dinoOne.forward(50)
    screen.update()     
    dinoOne.setheading(0)  
    dinoOne.forward(50)     
    screen.update()

# Register keypress event listener
screen.listen()
screen.onkey(move_up_down, "space")

# Keep the window open and responsive
screen.mainloop()
