import time
from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

turt = Turtle()
screen = Screen()
scoreboard = Scoreboard()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle_one = Paddle((350,0))
paddle_two = Paddle((-350,0))
ball = Ball()
screen.listen()


screen.onkey(paddle_one.go_up, "Up")
screen.onkey(paddle_one.go_down, "Down")
screen.onkey(paddle_two.go_up, "w")
screen.onkey(paddle_two.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move_ball()

    #Detect collisions with bottom border
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    #Detect collisions with paddle
    if ball.distance(paddle_one) < 50 and ball.xcor() > 320 or ball.distance(paddle_two) < 50 and ball.xcor() < -320 :
        ball.collision()

    #Detect misses on Right side
    if ball.xcor() > 410:
        time.sleep(.001)
        ball.reset()
        scoreboard.l_point()

    #Detect misses on Left side
    if ball.xcor() < -410:
        time.sleep(.001)
        ball.reset()
        scoreboard.r_point()








screen.exitonclick()
