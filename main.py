from turtle import Screen
import tkinter as tk
from tkinter import ttk
from ball import Ball
from brick import Bricks
from paddle import Paddle
from scoreboard import Scoreboard


def end_program():
    screen.bye()


def play_game(popup):
    popup.destroy()
    paddle_hit = 0
    game_is_on = True

    while game_is_on:
        global bricks
        screen.update()
        ball.move()

        # Detect Collision with walls
        if ball.ycor() > 280:
            ball.bounce_y()

        if ball.xcor() > 478 or ball.xcor() < -485:
            ball.bounce_x()

        # Detect collision with paddle
        if ball.distance(paddle) < 80 and -295 < ball.ycor() < -292:
            ball.bounce_y()
            paddle_hit += 1
            if paddle_hit == 4:
                ball.speed_up()
                ball.adjust_trajectory()
                paddle_hit = 0

        # Detect Collision with bricks
        for brick in bricks.bricks:
            if 38 < ball.distance(brick) < 45:
                ball.bounce_y()
                bricks.delete_brick(brick)
                if brick.level == 4:
                    ball.fastest()
                scoreboard.increase_score()
                break
            elif ball.distance(brick) < 20:
                ball.bounce_x()
                if brick.level == 4:
                    ball.fastest()
                scoreboard.increase_score()
                break

        # Detect Paddle Misses
        if ball.ycor() < -380:
            print("BALL MISSES PADDLE")
            scoreboard.lose_life()
            ball.lose_life()

        # Detect Wall Destroyed
        if scoreboard.player_score >= 60 and wall_cycles < 2:
            bricks = create_wall()
        elif wall_cycles >= 2:
            game_is_on = False
            game_over_popup()

        # Detect End of Game
        if scoreboard.player_lives <= 0:
            game_is_on = False
            game_over_popup()


def game_over_popup():
    popup_end = tk.Tk()
    popup_end.wm_title("Game Over!")
    screen_width = popup_end.winfo_screenwidth()
    screen_height = popup_end.winfo_screenheight()
    window_width = 300
    window_height = 200
    x_cordinate = int((screen_width / 2) - (window_width / 2))
    y_cordinate = int((screen_height / 2) - (window_height / 2))
    popup_end.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")
    label = ttk.Label(popup_end, text="Game Over!", font=("Atari Font Full Version", 20))
    label.pack(pady=20, padx=20)
    label2 = ttk.Label(popup_end, text=f"You scored: {scoreboard.player_score}!", font=("Atari Font Full Version", 20))
    label2.pack(pady=20, padx=20)
    B = ttk.Button(popup_end, text="Quit", command=lambda: [end_program(), popup_end.destroy()])
    B.pack()
    popup_end.mainloop()


def start_popup():
    popup = tk.Tk()
    popup.wm_title("Start Game?")
    screen_width = popup.winfo_screenwidth()
    screen_height = popup.winfo_screenheight()
    window_width = 200
    window_height = 70
    x_cordinate = int((screen_width / 2) - (window_width / 2))
    y_cordinate = int((screen_height / 2) - (window_height / 2))
    popup.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")
    B1 = ttk.Button(popup, text="Click to Start!", command=lambda:[play_game(popup)])
    B1.pack(padx=20, pady=20)
    popup.mainloop()


def create_wall():
    global wall_cycles
    wall_cycles += 1
    wall = Bricks()
    return wall


wall_cycles = 0
# Screen Setup
screen = Screen()
screen.bgcolor('#141717')
screen.setup(width=1000, height=800)
screen.title("Breakout of Here!")
screen.tracer(0)

# Create Paddle
paddle = Paddle()

# Create Ball
ball = Ball()

# Create Bricks/wall
bricks = create_wall()

# Create Scoreboard
scoreboard = Scoreboard()

# Listening
screen.listen()
screen.onkey(end_program, 'q')
screen.onkey(paddle.go_l, 'Left')
screen.onkey(paddle.go_r, 'Right')

start_popup()
