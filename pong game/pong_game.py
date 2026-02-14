from turtle import Screen
from pong import Bat # type: ignore
from pong_ball import Ball # type: ignore
from scoreboard import Scoreboard # type: ignore
import time
screen = Screen()
screen.setup(width=800, height=600)
screen.title("Welcome to the ultimate pong game")
screen.tracer(0)
left_bat = Bat(-350, 0)
right_bat = Bat(350, 0)
ball = Ball()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(right_bat.move_up, "Up")
screen.onkey(right_bat.move_down, "Down")
screen.onkey(left_bat.move_up, "w")
screen.onkey(left_bat.move_down, "s")
game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move_around()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_off_wall()
    if (ball.xcor() > 320 or ball.xcor() < -320) and (ball.distance(right_bat) < 50 or ball.distance(left_bat) < 50):
        ball.bounce_off_bat()
    if (ball.xcor() > 380):
        ball.reset_position()
        scoreboard.increase_score_l()
    if (ball.xcor() < -380):
        ball.reset_position()
        scoreboard.increase_score_r()
    if (scoreboard.l_score == 5 or scoreboard.r_score == 5):
        game_is_on = False
        scoreboard.game_over()
screen.exitonclick()