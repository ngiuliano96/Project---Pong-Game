from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 70, "normal")
R_POSITION = (150, 200)
L_POSITION = (-150, 200)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.setpos(L_POSITION)
        self.write(f"{self.l_score}", align=ALIGNMENT, font=FONT)
        self.setpos(R_POSITION)
        self.write(f"{self.r_score}", align=ALIGNMENT, font=FONT)

    def game_over(self, player):
        self.setpos(0, 0)
        self.write(f"Player {player} Wins!", align=ALIGNMENT, font=("Courier", 30, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.clear()
        self.update_scoreboard()
