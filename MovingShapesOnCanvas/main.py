from shape_library import *


def main():
    c = Circle(0, 0, 50, "red")
    c.draw()
    s = Square(-100, -50, 80, "blue")
    s.draw()
    t = Triangle(100, -50, 90, "green")
    t.draw()

    screen.mainloop()
    pass


if __name__ == "__main__":
    main()
