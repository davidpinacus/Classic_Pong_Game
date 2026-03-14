from turtle import Turtle
Distance=60

class Paddle(Turtle):
    def __init__(self,position):
           super().__init__()
           self.both_paddles(position)

    def both_paddles(self, position):
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.goto(position)

    def move_up(self):
         if self.ycor() < 240:
            self.sety(self.ycor() + Distance)
        
    def move_down(self):
         if self.ycor() >- 240:
            self.sety(self.ycor() - Distance)

    

        
