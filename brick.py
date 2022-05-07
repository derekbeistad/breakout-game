from turtle import Turtle

starting_x_coord = -449
starting_y_coord = 239
x_change = 100
y_change = -39
color_list = ['#A6483F', '#F27141', '#F28444', '#D9BD6A', '#D4D9CC', '#BFD7FF']


class Brick(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape('square')
        self.goto(position)
        self.shapesize(stretch_wid=2, stretch_len=5)


class Bricks():
    def __init__(self):
        self.bricks = []
        self.create_bricks()

    def create_bricks(self):
        starting_x_coord = -449
        starting_y_coord = 239
        x_change = 100
        y_change = -39
        color_list = ['#A6483F', '#F27141', '#F28444', '#D9BD6A', '#D4D9CC', '#F1EFF8']
        n = 0
        l = 6
        for c in range(6):
            for _ in range (10):
                new_brick = Brick((starting_x_coord + (n * x_change), starting_y_coord))
                new_brick.color(color_list[c])
                new_brick.level = l
                n += 1
                self.bricks.append(new_brick)
            n = 0
            c += 1
            l -= 1
            starting_y_coord += y_change

    def delete_brick(self, brick):
        brick.goto(1000, 1000)
