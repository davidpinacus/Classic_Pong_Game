from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.ball_speed = 0.1
        self.x_move = 5
        self.y_move = 5
        self.ball()
        self.moving_pos()

    def ball(self):
        self.shape("square")
        self.color("white")
        self.shapesize(1,1)
        self.goto(x=0,y=0)
        self.penup()

    def moving_pos(self):

        x_axis=self.xcor() + self.x_move
        y_axis=self.ycor() + self.y_move
        self.goto(x_axis,y_axis)

    def bounce_y(self):
        self.y_move *= -1
        self.sety(self.ycor() + self.y_move)

    def bounce_x(self):
        self.ball_speed*=0.7
        self.x_move *= -1
        self.setx(self.xcor() + self.x_move)
    
    def ball_out(self):
        self.goto(0,0)
        self.bounce_x()
        self.ball_speed=0.07




             