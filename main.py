from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
screen = Screen()
# # screen.delay(50)

# segment = []
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

obj_for_snake = Snake()
# obj_for_snake.create_snake()
food_for_snake = Food()
score_of_game = Scoreboard()
# score_of_game.high_score()

# screen.update()
game_is_on = True
screen.listen()
# screen.onkey(fun=snake_up, key="up")
# screen.onkey(fun=snake_down, key="down")
screen.onkey(fun=obj_for_snake.snake_right, key="Right")
screen.onkey(fun=obj_for_snake.snake_left, key="Left")

while game_is_on:
    """how can length of segment be changed by overlapping"""
    obj_for_snake.move()

    if obj_for_snake.head.distance(food_for_snake) < 15:
        food_for_snake.refresh()
        score_of_game.update_score()
        obj_for_snake.extend()

    if obj_for_snake.head.xcor() > 285 or obj_for_snake.head.xcor() < -285 or obj_for_snake.head.ycor() > 285 or obj_for_snake.head.ycor() < -285:
        # game_is_on = False
        score_of_game.highest_score()
        # score_of_game.game_over()
        obj_for_snake.reset_snake()

    for seg in obj_for_snake.segment[1:]:
        """using slicing method and not following conventional method"""
        if seg.distance(obj_for_snake.head) < 1:
            # game_is_on = False
            score_of_game.highest_score()
            # score_of_game.game_over()
            obj_for_snake.reset_snake()

    # if score_of_game.new_score > score_of_game.high_score:
    #     score_of_game.highest_score()

        """this is conventional method"""
        # if seg != obj_for_snake.head:
        #     if seg.distance(obj_for_snake.head) < 1:
        #         game_is_on = False
        #         score_of_game.game_over()


    # if obj_for_snake.segment.distance(obj_for_snake.head) == 0:
    #     game_is_on = False
    #     score_of_game.game_over()

    time.sleep(0.1)
    screen.update()
# print(obj_for_snake.apple)

screen.exitonclick()
