from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.x_coor_change = 10
        self.y_coor_change = 10
        self.ball_speed = 0.1
    def move_around(self):
        self.penup()
        new_x_coor = self.xcor() + self.x_coor_change
        new_y_coor = self.ycor() + self.y_coor_change
        self.goto(new_x_coor, new_y_coor)
    def bounce_off_wall(self):
        self.y_coor_change *= -1
    def bounce_off_bat(self):
        self.x_coor_change *= -1
        self.ball_speed *= 0.9
    def reset_position(self):
        self.goto(0, 0)
        self.ball_speed = 0.1
        self.bounce_off_bat()
