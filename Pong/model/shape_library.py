# Phase 1
import turtle

screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Shape Library")
screen.tracer(0)
screen.setup(1.0, 1.0, None, None)


class Shape:
    def __init__(self, x, y, color="black"):
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
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

    def step(self):
        self.x += self.dx
        self.y += self.dy


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


class Rectangle(Shape):
    def __init__(self, x, y, lo, la, color="black"):
        super().__init__(x, y, color)
        self.lo = lo
        self.la = la
        pass

    def draw(self):
        self.t.clear()
        self.t.goto(self.x - self.la / 2, self.y - self.lo / 2)
        self.t.pendown()
        self.t.begin_fill()
        for _ in range(2):
            self.t.forward(self.la)
            self.t.left(90)
            self.t.forward(self.lo)
            self.t.left(90)
        self.t.end_fill()
        self.t.penup()
        pass


class Square(Rectangle):
    def __init__(self, x, y, size, color="black"):
        super().__init__(x, y, size, size, color)
        self.size = size
        pass


if __name__ == "__main__":
    print("This is the shape_library.py file")
