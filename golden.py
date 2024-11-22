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
    R = 3
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


def draw_fibonacci_squares(num_squares):
    R = 1
    pen.hideturtle()
    for _ in range(num_squares):
        turtle.color("black")
        for _ in range(4):
            turtle.fd(R)
            turtle.lt(90)
        turtle.penup()
        turtle.circle(R, 90)
        turtle.pendown()
        R *= G


def draw_fibonacci_star(lines):
    R = 1
    for _ in range(lines):
        pen.forward(R * 10)  # Line length based on Fibonacci number
        pen.right(144)  # Star angle (5-point star)
        
        # Update Fibonacci sequence
        R *= G

def draw_fibonacci_flower(cycles):
    R = 1
    petals = 6
    pen.speed(0)

    for _ in range(cycles):
        for _ in range(petals):
            pen.circle(R * 10)  # Petal radius based on Fibonacci number
            pen.left(360 / petals)  # Rotate for the next petal
        
        # Update Fibonacci sequence
        R *= G

def draw_fibonacci_typhoon(cycles):
    R = 1
    petals = 12
    pen.speed(0)

    for _ in range(cycles):
        pen.circle(R * 10)  # Petal radius based on Fibonacci number
        pen.left(360/petals)
        
        # Update Fibonacci sequence
        R *= G


# Start position
pen.penup()
pen.goto(0, 0)
pen.setheading(0)  
pen.pendown()
pen.speed(0)

# Draw the golden spiral
draw_golden_spiral(15)  
# draw_fibonacci_squares(15)
# draw_fibonacci_star(15)
# draw_fibonacci_flower(6)
# draw_fibonacci_typhoon(15)

# Hide the turtle and finish
pen.hideturtle()
turtle.done()
