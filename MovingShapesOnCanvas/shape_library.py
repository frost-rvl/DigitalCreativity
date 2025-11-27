# Phase 1
import turtle

screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Shape Library")


class Shape:
    def __init__(self, x, y, color="black"):
        self.x = x
        self.y = y
        self.color = color
        self.t = turtle.Turtle()
        self.t.hideturtle()
        self.t.penup()
        self.t.color(self.color)
        pass

    def move_to(self, x, y):
        self.x = x
        self.y = y
        self.t.goto(x, y)
        pass


class Circle(Shape):
    def __init__(self, x, y, radius, color="black"):
        super().__init__(x, y, color)
        self.radius = radius
        pass

    def draw(self):
        self.t.clear()
        self.t.goto(self.x, self.y - self.radius)
        self.t.pendown()
        self.t.begin_fill()
        self.t.circle(self.radius)
        self.t.end_fill()
        self.t.penup()
        pass


class Square(Shape):
    def __init__(self, x, y, size, color="black"):
        super().__init__(x, y, color)
        self.size = size
        pass

    def draw(self):
        self.t.clear()
        self.t.goto(self.x - self.size / 2, self.y - self.size / 2)
        self.t.pendown()
        self.t.begin_fill()
        for _ in range(4):
            self.t.forward(self.size)
            self.t.left(90)
        self.t.end_fill()
        self.t.penup()
        pass


class Triangle(Shape):
    def __init__(self, x, y, size, color="black"):
        super().__init__(x, y, color)
        self.size = size
        pass

    def draw(self):
        self.t.clear()
        self.t.goto(self.x, self.y - self.size / 2)
        self.t.pendown()
        self.t.begin_fill()
        for _ in range(3):
            self.t.forward(self.size)
            self.t.left(120)
        self.t.end_fill()
        self.t.penup()
        pass


if __name__ == "__main__":
    print("This is the shape_library.py file")
