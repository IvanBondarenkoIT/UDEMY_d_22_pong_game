from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoore

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoore()


screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
# screen.onkey(snake.left, "Left")
# screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.fly()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if (ball.distance(r_paddle) < 60 and ball.xcor() > 330)\
            or (ball.distance(l_paddle) < 60 and ball.xcor() < -330):
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset()
        score.refrash_score(1, 0)

    if  ball.xcor() < -380:
        ball.reset()
        score.refrash_score(0, 1)

screen.exitonclick()