import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from center_line import Line


screen=Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong")

screen.tracer(0)
center_line= Line()
ball=Ball()
scoreboard=Scoreboard()
paddle_1=Paddle((350,0))
paddle_2=Paddle((-350,0))

screen.listen()
screen.onkey(paddle_1.move_up,"Up")
screen.onkey(paddle_1.move_down,"Down")
screen.onkey(paddle_2.move_up,"w")
screen.onkey(paddle_2.move_down,"s")


game_on = True

while game_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.moving_pos()
    if ball.ycor() > 280 or ball.ycor() <-280:
        ball.bounce_y()

    if ball.distance(paddle_1) < 50 and ball.xcor() > 330 and ball.x_move > 0: 
        ball.bounce_x()

    if ball.distance(paddle_2) < 50 and ball.xcor() <- 330 and ball.y_move > 0:
        ball.bounce_x()

    if ball.xcor() > 395:
        ball.ball_out()
        scoreboard.left_side()

    if ball.xcor() < - 395:
        ball.ball_out()
        scoreboard.right_side()


screen.exitonclick()



