from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 12, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.new_score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        """Below is my own method to read"""
        # self.high_score = int(open("data.txt", mode="r").read())
        self.shape()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-20, 280)
        self.write(arg=f'Score: {self.new_score}     High Score: {self.high_score}', align=ALIGNMENT, font=FONT)
        self.new_score += 1
        # self.highest_score()

    def highest_score(self):
        # self.clear()
        # self.goto(50, 280)
        if self.new_score - 1 >= self.high_score:
            self.high_score = self.new_score - 1
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
                """This way is also right"""
                # data.write(str(self.high_score))
            """Below two lines are my own method to write"""
            # file = open("data.txt", mode="w")
            # file.write(str(self.high_score))
            # self.write(arg=f'High Score: {self.high_score}', align=ALIGNMENT, font=FONT)
        self.new_score = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(-10, 0)
    #     self.write(arg="GAMEOVER", align=ALIGNMENT, font=FONT)

        """My own method for high score"""
        # self.new_score -= 1
        # if self.new_score >= self.high_score:
        #     self.high_score = self.new_score
        #     self.clear()
        #     self.update_score()







