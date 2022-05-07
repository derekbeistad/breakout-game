from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.player_score = 0
        self.player_lives = 3
        self.update_scoreboard()

    def score_text(self):
        self.goto(-470, 367)
        self.write("S", align='center', font=("Atari Font Full Version", 13, "normal"))
        self.goto(-470, 352)
        self.write("C", align='center', font=("Atari Font Full Version", 13, "normal"))
        self.goto(-470, 337)
        self.write("O", align='center', font=("Atari Font Full Version", 13, "normal"))
        self.goto(-470, 322)
        self.write("R", align='center', font=("Atari Font Full Version", 13, "normal"))
        self.goto(-470, 307)
        self.write("E", align='center', font=("Atari Font Full Version", 13, "normal"))

    def show_title(self):
        self.goto(15, 302)
        self.write("Breakout!", align="center", font=("Atari Font Full Version", 80, "normal"))

    def update_scoreboard(self):
        self.clear()
        self.board_background()
        self.color('#141717')
        self.show_title()
        self.score_text()
        self.display_lives()
        self.goto(-410, 325)
        self.write(self.player_score, align="center", font=("Atari Font Full Version", 40, "normal"))

    def increase_score(self):
        self.player_score += 1
        self.update_scoreboard()

    def board_background(self):
        self.color('#D4D9CC')
        self.shape('square')
        self.shapesize(stretch_wid=5.5, stretch_len=50)
        self.goto(0, 350)
        self.stamp()

    def display_lives(self):
        self.goto(445, 315)
        self.write("Lives\nLeft", align='center', font=("Atari Font Full Version", 12, "normal"))
        self.goto(440, 350)
        self.write(self.player_lives, align='center', font=("Atari Font Full Version", 20, "normal"))

    def lose_life(self):
        self.player_lives -= 1
        self.update_scoreboard()
