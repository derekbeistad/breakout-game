from turtle import Turtle
from random import choice
import numpy as np
BALL_START_POSITION = (0, -250)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.color('#CBF9FE')
        self.goto(BALL_START_POSITION)
        self.move_x = 2
        self.move_y = 2

    def move(self):
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.goto(new_x, new_y)

    def lose_life(self):
        self.goto(BALL_START_POSITION)
        self.bounce_y()

    def bounce_y(self):
        self.move_y *= -1

    def bounce_x(self):
        self.move_x *= -1

    def speed_up(self):
        speed_factor = choice(np.arange(0.8, 1.3, 0.1))
        print("Speed up")
        self.move_x *= speed_factor
        self.move_y *= speed_factor

    def adjust_trajectory(self):
        angle_factor = choice(np.arange(0.6, 1.6, 0.1))
        if 1 == choice(range(2)):
            print("change angle")
            self.move_x *= angle_factor

    def fastest(self):
        print("FASTEST")
        self.move_x *= 1.3
        self.move_y *= 1.3
