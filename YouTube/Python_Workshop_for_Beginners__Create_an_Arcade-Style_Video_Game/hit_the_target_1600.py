import turtle
import random

ball_x_velocity = 7
ball_y_velocity = 7
gravity = -0.5

screen = turtle.Screen()
screen.setup(600, 800)
screen.tracer()

cannon = turtle.Turtle()
cannon.shape("triangle")
cannon.color("green")
cannon.penup()
cannon.setposition(-150, 0)
cannon.setheading(45)

target = turtle.Turtle()
target.shape("circle")
target.color("blue")
target.penup()
target.setposition(
    random.randint(50, 250),
    random.randint(-200, -200),
)


ball = turtle.Turtle()
ball.shape("circle")
ball.turtlesize(0.5)
ball.color("firebrick")
ball.penup()
ball.setposition(cannon.position())

ball.ball_in_motion = False


def shoot():
    ball.ball_in_motion = not ball.ball_in_motion


def move_left():
    cannon.setx(cannon.xcor() - 10)
    if ball.ball_in_motion == False:
        ball.setx(cannon.xcor())


screen.onkeypress(shoot, "space")
screen.onkeypress(move_left, "Left")
screen.listen()

while True:
    if ball.ball_in_motion:
        ball.setx(ball.xcor() + ball_x_velocity)
        ball.sety(ball.ycor() + ball_y_velocity)
        ball_y_velocity += gravity

    if ball.distance(target) < 20:
        ball.setposition(cannon.position())
        ball_y_velocity = 3
        target.setposition(random.randint(50, 250), random.randint(-200, 200))

    screen.update()


turtle.done()
