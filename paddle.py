from turtle import Turtle
from ball import Ball

ball = Ball()
ball.hideturtle()


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.setpos(position)

    def paddle_up(self):
        if self.ycor() < 230 and -330 < ball.xcor() < 330:
            new_y = self.ycor() + 20
            self.setpos(self.xcor(), new_y)
        else:
            pass

    def paddle_down(self):
        if self.ycor() > -240 and -330 < ball.xcor() < 330:
            new_y = self.ycor() - 20
            self.setpos(self.xcor(), new_y)
        else:
            pass