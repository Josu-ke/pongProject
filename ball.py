from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.goto(0,0)
        self.x_move = 10
        self.y_move =10
        self.ball_speed = .1


    def move_ball(self):
        new_x = self.xcor() +self.x_move
        new_y = self.ycor()+self.y_move
        self.goto(new_x,new_y)

    def bounce(self):
        self.y_move = self.y_move * -1

    def collision(self):
        self.x_move = self.x_move * -1
        self.ball_speed *= .9

    def reset(self):
        self.home()
        self.ball_speed =0.1
        self.x_move = self.x_move * -1

