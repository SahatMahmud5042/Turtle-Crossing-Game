import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
cars = CarManager()

#player control
screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")

game_is_on = True
while game_is_on:
    scoreboard.update_level()

    time.sleep(0.1)
    screen.update()

    cars.gen_cars()
    cars.car_move()

    if player.ycor() > 280:
        player.game_reset()
        scoreboard.level_up()
        cars.move_incr()

    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()