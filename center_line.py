from turtle import Turtle

class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.line()

    def line(self):
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0,300)
        self.setheading(270)
        self.length=20
        self.gap=20
        for _ in range(15):
            self.pendown()
            self.forward(self.length)
            self.penup()
            self.forward(self.gap)
