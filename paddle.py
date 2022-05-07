from turtle import Turtle

STARTING_POSITION = (0, -300)


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("#F2A0B6")
        self.shapesize(stretch_wid=0.5, stretch_len=6)
        self.penup()
        self.speed('fastest')
        self.goto(STARTING_POSITION)

    def go_l(self):
        new_x = self.xcor() - 60
        self.goto(new_x, self.ycor())

    def go_r(self):
        new_x = self.xcor() + 60
        self.goto(new_x, self.ycor())
