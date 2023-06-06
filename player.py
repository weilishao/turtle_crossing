from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.go_home()
        self.level = 0

    def go_home(self):
        self.goto(STARTING_POSITION)

    def lvl_up(self):
        if self.ycor() > FINISH_LINE_Y:
            self.level += 1
            self.go_home()

    def move(self):
        self.forward(MOVE_DISTANCE)
