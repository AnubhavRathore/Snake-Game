from turtle import Turtle


class Snake:

    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        for item in range(3):
            tim = Turtle(shape="square")
            tim.penup()
            tim.color("white")
            # print(tim)
            pos = - item * 20
            tim.goto(x=pos, y=0)
            self.segment.append(tim)

    def reset_snake(self):
        # print(self.segment)
        for seg in self.segment:
            seg.goto(1000, 1000)
        # print(self.segment)
        self.segment.clear()
        # print(self.segment)
        self.create_snake()
        self.head = self.segment[0]

    def extend(self):
        tim = Turtle(shape="square")
        tim.penup()
        tim.color("white")
        len_of_segment = len(self.segment)
        x_cor_of_last = self.segment[len_of_segment - 1].xcor()
        y_cor_of_last = self.segment[len_of_segment - 1].ycor()
        tim.goto(x=x_cor_of_last, y=y_cor_of_last)
        self.segment.append(tim)

    def move(self):
        for seg in range(len(self.segment) - 1, 0, - 1):
            x_pos = self.segment[seg - 1].xcor()
            y_pos = self.segment[seg - 1].ycor()
            self.segment[seg].goto(x_pos, y_pos)
        self.segment[0].forward(20)

    def snake_left(self):
        self.head.left(90)

    def snake_right(self):
        self.head.right(90)



