from turtle import Turtle


class Scoreboard(Turtle):
    
    SCORE_COLOR = "cyan"
    SCORE_FONT = ("Courier", 80, "bold") 

    def __init__(self):
        super().__init__()

        self.color(self.SCORE_COLOR)
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 250)
        self.write(self.l_score, align="center", font=self.SCORE_FONT)
        self.goto(100, 250)
        self.write(self.r_score, align="center", font=self.SCORE_FONT)

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()
     
    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def game_over(self, winner_message="GAME OVER"):
        """Displays the Game Over message in the center of the screen."""
        self.goto(0, 0)
        self.color("red")
   
        self.write(winner_message, align="center", font=("Courier", 60, "bold"))
