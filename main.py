import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
manager = CarManager()
level_meter = Scoreboard()

screen.listen()
screen.onkeypress(turtle.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # level up attribute and scoreboard
    if turtle.ycor() > 280:
        level_meter.lvl_up()
    turtle.lvl_up()

    # set speed
    manager.move_cars(turtle.level)

    # set car respawn frequency
    manager.count_loop()
    for car in manager.cars:
        if car.distance(turtle) < 20:
            game_is_on = False
    if turtle.level < 2:
        if manager.counter % 6 == 0:
            manager.make_car()
    elif turtle.level < 4:
        if manager.counter % 3 == 0:
            manager.make_car()
    elif turtle.level < 6:
        if manager.counter % 2 == 0:
            manager.make_car()
    else:
        manager.make_car()

level_meter.game_over()

screen.exitonclick()
