from turtle import Turtle, Screen
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.snake_length = 3
        self.snake = []
        self.snake_pos = [0, 0]

        offset = 0
        for each in range(0, self.snake_length):
            new_segment = Turtle(shape="square")
            new_segment.penup()
            new_segment.color("green")
            new_segment.goto(self.snake_pos[0] - offset, self.snake_pos[1])
            offset += 20
            self.snake.append(new_segment)

        self.head = self.snake[0]


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