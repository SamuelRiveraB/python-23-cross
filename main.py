import time
from turtle import Screen

from car import Car
from scoreboard import ScoreBoard
from player import Player

screen = Screen()
screen.title("CROSSING GAME")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = []
scoreboard = ScoreBoard()

for car in range(0, 40):
    new = Car()
    cars.append(new)

screen.listen()
screen.onkey(player.move_up, 'w')

game = True
while game:
    time.sleep(player.game_sp)
    screen.update()
    for car in cars:
        car.move_left()
        if car.xcor() < -320:
            car.loop()
        if player.distance(car) < 15:
            scoreboard.game_over()
            game = False
    if player.ycor() > 300:
        scoreboard.update()
        player.to_start()
        player.sp *= 1.5
        player.game_sp *= 0.5

screen.exitonclick()