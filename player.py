from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.left(90)
        self.up()
        self.teleport(0, y=-280)
        self.sp = 10
        self.game_sp = 0.1

    def move_up(self):
        self.forward(self.sp)

    def to_start(self):
        self.teleport(0, y=-280)
