from model.shape_library import Rectangle, screen

window_size = [screen.window_width(), screen.window_height()]


class Player(Rectangle):
    def __init__(self, x=0, y=0, color="black"):
        super().__init__(x, y, 200, 100, color)
        self.base_vitesse = 15
        self.dy = self.base_vitesse
        pass

    def stepUp(self):
        self.y += self.dy
        if self.y > window_size[1] - 100:
            self.y += -self.dy
        pass

    def stepDown(self):
        self.y -= self.dy
        if self.y < -window_size[1] + 100:
            self.y += self.dy
        pass
