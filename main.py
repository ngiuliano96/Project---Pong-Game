import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

# Starting paddle positions
R_PADDLE_POSITION = (350, 0)
L_PADDLE_POSITION = (-350, 0)

# Set up screen
screen = Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# Create scoreboard
scoreboard = Scoreboard()

# Create paddles
r_paddle = Paddle(R_PADDLE_POSITION)
l_paddle = Paddle(L_PADDLE_POSITION)

# Create ball
ball = Ball()

# Listen for paddle movement
screen.listen()
screen.onkeypress(r_paddle.paddle_up, "Up")
screen.onkeypress(r_paddle.paddle_down, "Down")
screen.onkeypress(l_paddle.paddle_up, "w")
screen.onkeypress(l_paddle.paddle_down, "s")

# Update screen correctly
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect collision with top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < - 280:
        ball.bounce_y()

    # Detect collision with side of either paddle
    if ball.distance(r_paddle) < 63 and ball.xcor() == 330 or ball.distance(l_paddle) < 63 and ball.xcor() == -330:
        ball.bounce_x()

    # Detect collision with top/bottom of either paddle
    if ball.distance(r_paddle) < 63 and ball.xcor() > 330 or ball.distance(l_paddle) < 63 and ball.xcor() < -330:
        ball.bounce_y()

    # Detect if left player scores
    if ball.xcor() > 380:
        time.sleep(1)
        scoreboard.l_point()
        ball.reset_position()

    # Detect if right player scores
    if ball.xcor() < -380:
        time.sleep(1)
        scoreboard.r_point()
        ball.reset_position()

    # Detect if either player wins
    if scoreboard.r_score > 10:
        scoreboard.game_over("2")
        game_is_on = False

    if scoreboard.l_score > 10:
        scoreboard.game_over("1")
        game_is_on = False

# Exit screen on click
screen.exitonclick()
