from turtle import Turtle
class Bat(Turtle):
    def __init__(self, x_coor, y_coor):
        super().__init__()
        self.shape("square")
        self.color("green")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x_coor, y_coor)
    def move_up(self):
        new_y_coor = self.ycor() + 20
        self.goto(self.xcor(), new_y_coor)
    def move_down(self):
        new_y_coor = self.ycor() - 20
        self.goto(self.xcor(), new_y_coor)