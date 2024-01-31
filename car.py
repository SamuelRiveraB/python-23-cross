import random
from turtle import Turtle
import turtle

turtle.colormode(255)


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.color(random_color)
        self.up()
        self.shapesize(stretch_len=2)
        self.teleport(x=random.randint(-280, 280), y=random.randint(-240, 280))

    def move_left(self):
        new_x = self.xcor() - 10
        self.goto(new_x, self.ycor())

    def loop(self):
        self.goto(320, self.ycor())
