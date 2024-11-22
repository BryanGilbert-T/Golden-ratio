import turtle

# Set up the screen and turtle
screen = turtle.Screen()
screen.title("Pan Wei's Golden Spiral")
screen.bgcolor("white")
screen.setup(width=1.0, height =1.0)

# Create the turtle
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(1)
pen.color("black")

# Golden ratio's ratio is 1.618
G = 1.618
def draw_golden_spiral(spiral_length):
    R = 1
    pen.hideturtle()
    pen.speed(0)
    for i in range(spiral_length):
        turtle.color("gray")
        turtle.speed(0)
        print(i + 1, ": ", R)
        for _ in range(4):
            turtle.fd(R)
            turtle.lt(90)
        turtle.color("black")
        turtle.circle(R, 90)
        R *= G


# Start position
pen.penup()
pen.goto(0, 0)
pen.setheading(0)  
pen.pendown()
pen.speed(0)

# Draw the golden spiral
draw_golden_spiral(15)  

# Hide the turtle and finish
pen.hideturtle()
turtle.done()
