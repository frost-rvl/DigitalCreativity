import math
import random

from model.shape_library import Circle, screen

window_size = [screen.window_width(), screen.window_height()]


class Ball(Circle):
    def __init__(self, x=0, y=0, radius=40, color="black"):
        super().__init__(x, y, radius, color)
        self.base_speed = 20
        self.randomDirection()
        pass

    def randomDirection(self):
        angle = random.uniform(0, 2 * math.pi)
        self.dx = math.cos(angle) * self.base_speed
        self.dy = math.sin(angle) * self.base_speed

    def step(self):
        self.x += self.dx
        self.y += self.dy
        if self.x > window_size[0] or self.x < -window_size[0]:
            self.dx *= -1
        if self.y > window_size[1] or self.y < -window_size[1]:
            self.dy *= -1
        pass

    def checkPosition(self):
        if self.x < -window_size[0] or self.x > window_size[0]:
            self.randomDirection()
            self.move_to(0, 0)
