import turtle

# Game window

window = turtle.Screen()
window.title("Ping Pong")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer()


# Paddle L
paddle_l = turtle.Turtle()
paddle_l.speed(0)
paddle_l.shape("square")
paddle_l.shapesize(stretch_wid=3, stretch_len=1)
paddle_l.color("white")
paddle_l.penup()
paddle_l.goto(-380, 0)

# Paddle R
paddle_r = turtle.Turtle()
paddle_r.speed(0)
paddle_r.shape("square")
paddle_r.shapesize(stretch_wid=3, stretch_len=1)
paddle_r.color("white")
paddle_r.penup()
paddle_r.goto(375, 0)

# Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("yellow")
ball.penup()
ball.goto(0, 0)
ball.dx = 3
ball.dy = -3

# Pen

pen = turtle.Turtle()
pen.speed(0)
pen.color("Green")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1:      Player 2:  ", align="center", font=("Arial", 24, "bold"))

# Scoring system

score_1 = 0
score_2 = 0

# Function

def paddle_l_up():
    y = paddle_l.ycor()
    y += 20
    paddle_l.sety(y)

def paddle_l_down():
    y = paddle_l.ycor()
    y -= 20
    paddle_l.sety(y)

def paddle_r_up():
    y = paddle_r.ycor()
    y += 20
    paddle_r.sety(y)
def paddle_r_down():
    y = paddle_r.ycor()
    y -= 20
    paddle_r.sety(y)

# Keyboard binds
window.listen()
window.onkeypress(paddle_l_up, "w")
window.onkeypress(paddle_l_down, "s")
window.onkeypress(paddle_r_up, "i")
window.onkeypress(paddle_r_down, "k")

# Game loop

while True:
    window.update()

    # Ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Check for the border
    if ball.ycor() > 285:
        ball.sety(285)
        ball.dy *= -1

    if ball.ycor() < -285:
        ball.sety(-285)
        ball.dy *= -1

    if ball.xcor() > 405:
        ball.goto(0, 0)
        ball.dx *= -1
        score_1 += 1
        pen.clear()
        pen.write("Player 1: {}    Player 2: {}".format(score_1, score_2), align="center", font=("Arial", 24, "bold"))

    if ball.xcor() < -405:
        ball.goto(0, 0)
        ball.dx *= -1
        score_2 += 1
        pen.clear()
        pen.write("Player 1: {}    Player 2: {}".format(score_1, score_2), align="center", font=("Arial", 24, "bold"))

    # Paddle collision

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_r.ycor() + 40 and ball.ycor() > paddle_r.ycor() -40):    # Right Paddle
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_l.ycor() + 40 and ball.ycor() > paddle_l.ycor() -40):    # Left Paddle
        ball.setx(-340)
        ball.dx *= -1