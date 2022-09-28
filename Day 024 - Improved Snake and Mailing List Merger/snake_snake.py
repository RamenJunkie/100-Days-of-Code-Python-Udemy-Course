from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.create_snake()

    def create_snake(self):
        self.snake_length = 3
        self.snake = []
        self.snake_pos = [0, 0]
        for each in range(0, self.snake_length):
            self.add_segment(self.snake_pos, 20)
        self.head = self.snake[0]


    def add_segment(self, postion, offset):
        self.new_segment = Turtle(shape="square")
        self.new_segment.penup()
        self.new_segment.goto(postion[0]- offset, postion[1])
        self.new_segment.color("green")
        self.snake.append(self.new_segment)

    def new_seg(self):
        self.add_segment([self.snake[-1].xcor(), self.snake[-1].ycor()], 0)

    def eat_self(self):
        for segment in self.snake[1:-1]:
            if self.head.distance(segment) < 10:
                return True

    def move(self):
        for seg_num in range(len(self.snake) - 1, 0, -1):
            new_coord = [self.snake[seg_num - 1].xcor(), self.snake[seg_num - 1].ycor()]
            self.snake[seg_num].goto(new_coord[0], new_coord[1])
        self.head.forward(MOVE_DISTANCE)

    def go_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def go_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def go_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def go_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for each in self.snake:
            each.goto(0,-600)
        self.snake.clear()
        self.create_snake()