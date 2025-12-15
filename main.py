from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
import turtle


import pygame

pygame.mixer.init()


WINNING_SCORE = 5


try:
    # Ensure the sound file names here match the actual file names exactly (e.g., 'hit_paddle.wav' vs 'hit paddle.wav')
    PADDLE_HIT_SOUND = pygame.mixer.Sound("hit paddle.wav")
    SCORE_SOUND = pygame.mixer.Sound("score_goal.wav")
    WIN_SOUND = pygame.mixer.Sound("win_game.wav")
except pygame.error:
    print("Warning: Could not load sound files. Sounds will be skipped.")



    def play_paddle_hit():
        pass


    def play_score_sound():
        pass


    def play_win_sound():
        pass
else:
    def play_paddle_hit():
        PADDLE_HIT_SOUND.play()


    def play_score_sound():
        SCORE_SOUND.play()


    def play_win_sound():
        WIN_SOUND.play()
# ------------------------------


screen = Screen()

screen.bgcolor("#0A0A0A")
screen.setup(width=800, height=600)
screen.title("Arcade Pong")
screen.tracer(0)



def draw_center_line():
    """Draws a dashed line down the center of the court."""
    line = Turtle()
    line.hideturtle()
    line.color("gray")
    line.penup()
    line.goto(0, 300)
    line.setheading(270)  # Point down

    for _ in range(15):
        line.pendown()
        line.forward(20)
        line.penup()
        line.forward(20)


def draw_goal_lines():
    """Draws solid lines to mark the goal area behind the paddles."""

    # Left Goal Line
    left_line = Turtle("square")
    left_line.hideturtle()
    left_line.penup()
    left_line.speed("fastest")
    left_line.goto(-360, 0)
    left_line.color("red")
    left_line.shapesize(stretch_wid=30, stretch_len=0.1)
    left_line.showturtle()

    # Right Goal Line
    right_line = Turtle("square")
    right_line.hideturtle()
    right_line.penup()
    right_line.speed("fastest")
    right_line.goto(360, 0)
    right_line.color("red")
    right_line.shapesize(stretch_wid=30, stretch_len=0.1)
    right_line.showturtle()


draw_center_line()
draw_goal_lines()


# ------------------------------


# --- PROMPT CLASS FOR START/RESTART MESSAGE ---
class Prompt(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()

    def display_message(self, message):
        self.clear()
        self.goto(0, -50)  # Position message slightly below center
        self.write(message, align="center", font=("Courier", 30, "normal"))


game_prompt = Prompt()
# ---------------------------------------------


# --- OBJECT INITIALIZATION ---
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball(play_paddle_hit, play_score_sound)
scoreboard = Scoreboard()


# -----------------------------


# --- MAIN GAME LOGIC FUNCTION ---
def start_game():
    global game_is_on


    game_prompt.clear()


    ball.goto(0, 0)
    scoreboard.l_score = 0
    scoreboard.r_score = 0
    scoreboard.update_scoreboard()


    ball.x_move = ball.INITIAL_X_MOVE
    ball.y_move = ball.INITIAL_Y_MOVE
    ball.move_speed = 0.015
    ball.bounce_counter = 0
    ball.bounce_x()

    game_is_on = True

    # --- THE MAIN GAME LOOP ---
    while game_is_on:
        time.sleep(ball.move_speed)
        screen.update()
        ball.move()

        # Detect collision with top/bottom wall
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()

        # Detect R paddle hit
        if ball.distance(r_paddle) < 50 and ball.xcor() > 320 and ball.x_move > 0:
            ball.bounce_x(r_paddle)

        # Detect L paddle hit
        elif ball.distance(l_paddle) < 50 and ball.xcor() < -320 and ball.x_move < 0:
            ball.bounce_x(l_paddle)

        # Detect R paddle miss (L player scores)
        if ball.xcor() > 380:
            ball.reset_position()
            scoreboard.l_point()
            play_score_sound()
            ball.speed_up()

            if scoreboard.l_score >= WINNING_SCORE:
                # Game Over Sequence
                ball.x_move = 0
                ball.y_move = 0
                play_win_sound()
                scoreboard.game_over("Left Player Wins!")
                screen.update()
                game_is_on = False
                break

        # Detect L paddle miss (R player scores)
        if ball.xcor() < -380:
            ball.reset_position()
            scoreboard.r_point()
            play_score_sound()
            ball.speed_up()

            if scoreboard.r_score >= WINNING_SCORE:
                # Game Over Sequence
                ball.x_move = 0
                ball.y_move = 0
                play_win_sound()
                scoreboard.game_over("Right Player Wins!")
                screen.update()
                game_is_on = False
                break
    # --- END OF WHILE LOOP ---

    # Once the loop breaks (game is over), display the restart prompt
    game_prompt.display_message("Press SPACE to play again")


# ---------------------------------------------


# --- KEY BINDINGS AND PROGRAM START ---
game_is_on = False  # Start the game in the 'off' state

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")
screen.onkey(r_paddle.dash, "Right")
screen.onkey(l_paddle.dash, "d")


def start_game_wrapper():
    global game_is_on
    # Only start the game if it is currently NOT running
    if not game_is_on:
        start_game()


screen.onkey(start_game_wrapper, "space")  # Start/Restart on Spacebar

# Display the initial prompt
game_prompt.display_message("Press SPACE to start")

# Keep the window open until clicked
screen.exitonclick()
