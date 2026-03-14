from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.board()
        self.display()

    def board(self):
        self.color("white")
        self.penup()
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0

    def display(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Press Start 2P", 45, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Press Start 2P", 45, "normal"))

    def right_side(self):
        self.r_score += 1
        self.display()

    def left_side(self):
        self.l_score+=1
        self.display()


