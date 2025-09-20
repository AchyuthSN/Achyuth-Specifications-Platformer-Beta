#Achyuth Specifications pre release software

import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Move Box with Arrow Keys")
screen.bgcolor("white")

# Create the black box
box = turtle.Turtle()
box.shape("square")
box.color("black")
box.penup()  # Don't draw lines when moving
box.speed(0)  # Fastest speed

# Functions to move the box
def move_left():
    x = box.xcor()  # Current x position
    x -= 20         # Move left by 20 pixels
    box.setx(x)

def move_right():
    x = box.xcor()
    x += 20         # Move right by 20 pixels
    box.setx(x)

# Keyboard bindings
screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")

# Keep the window open
screen.mainloop()
