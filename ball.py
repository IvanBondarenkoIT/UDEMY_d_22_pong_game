from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super(Ball, self).__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.speed("fastest")
        self.goto(0, 0)
        self.ball_speed = 10
        self.x_move = 1
        self.y_move = 1

    def reset(self):
        self.goto(0, 0)
        self.ball_speed = 10
        self.bounce_x()


    def fly(self):
        new_x = self.xcor() + (self.x_move * self.ball_speed)
        new_y = self.ycor() + (self.y_move * self.ball_speed)
        self.goto(new_x, new_y)


    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.ball_speed += 2
