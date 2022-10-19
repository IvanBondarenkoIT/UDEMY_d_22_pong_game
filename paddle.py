from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, start_position):
        super(Paddle, self).__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color("white")
        self.speed("fastest")
        self.goto(start_position)


    def up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def down(self):
        self.goto(self.xcor(), self.ycor() - 20)
