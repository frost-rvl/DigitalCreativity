import time

from model.ball import Ball
from model.player import Player
from model.shape_library import screen

window_size = [screen.window_width(), screen.window_height()]
keys = set()


def key_down(key):
    keys.add(key)


def key_up(key):
    keys.discard(key)


screen.onkeypress(lambda: key_down("Up"), "Up")
screen.onkeyrelease(lambda: key_up("Up"), "Up")
screen.onkeypress(lambda: key_down("Down"), "Down")
screen.onkeyrelease(lambda: key_up("Down"), "Down")

screen.onkeypress(lambda: key_down("w"), "w")
screen.onkeyrelease(lambda: key_up("w"), "w")
screen.onkeypress(lambda: key_down("s"), "s")
screen.onkeyrelease(lambda: key_up("s"), "s")


def update_players(p1, p2):
    if "Up" in keys:
        p1.stepUp()
    if "Down" in keys:
        p1.stepDown()
    if "w" in keys:
        p2.stepUp()
    if "s" in keys:
        p2.stepDown()

    p1.draw()
    p2.draw()
    screen.update()


def update_ball(ball):
    ball.step()
    ball.draw()
    ball.checkPosition()
    screen.update()


def main():
    b = Ball()
    p1 = Player(window_size[0] - 200, 0, "blue")
    p2 = Player(-window_size[0] + 200, 0, "red")

    while True:
        screen.listen()
        update_ball(b)
        update_players(p1, p2)
        screen.update()
        time.sleep(0.01)


if __name__ == "__main__":
    main()
