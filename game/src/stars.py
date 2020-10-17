import pygame
import pygame.gfxdraw
import random
from .ui import colors

class Dot:
    def __init__(self, kind, pos, color):
        self.kind  = kind
        self.pos = pos
        self.color = color


class Circle(Dot):
    def __init__(self, kind, pos, color):
        super().__init__(kind, pos, color)
        

        self.radii = list( range(1, random.randrange(2,4)) )
        radii_len = len(self.radii)

        self.timer = 1 / random.randrange(10, 121)
        self.time = self.timer

        self.static_i = self.color['static_index']
        self.color = self.color['color']
        self.colors = []
        self.dym_color = [self.color[0], self.color[1], self.color[2]]
        self.chromes_step = []

        if self.static_i:
            for index in range(0,3):
                chrome = self.dym_color[index]

                if index == self.static_i:
                    self.chromes_step.append(0)
                else:
                    if chrome == 255:
                        self.chromes_step.append(255 / len(self.radii))
                        self.dym_color[index] = 0
                    else:
                        self.chromes_step.append((255 - self.dym_color[index]) / len(self.radii))
        else:
            for index in range(0,3):
                chrome = self.dym_color[index]
                if chrome == 255:
                    self.chromes_step.append(255 / len(self.radii))
                    self.dym_color[index] = 0
                else:
                    self.chromes_step.append((255 - self.dym_color[index]) / len(self.radii))

        for n in range(1, len(self.radii) + 1):
            r_plus = int(self.chromes_step[0] * n)
            g_plus = int(self.chromes_step[1] * n)
            b_plus = int(self.chromes_step[2] * n)
            self.colors.append([self.dym_color[0] + r_plus, self.dym_color[1] + g_plus, self.dym_color[2] + b_plus])

    def timing(self):
        self.time += self.timer * self.time

        if int(self.time) >= len(self.radii):
            self.time = self.timer
        return int(self.time)

        
def gen(vw, vh):
    MIN_PIXEL_GAP = 3*9*6*3*9
    MAX_PIXEL_GAP = MIN_PIXEL_GAP * 3
    avg_pixel_gap = random.randrange(MIN_PIXEL_GAP, MAX_PIXEL_GAP)
    bg_area = vw * vh
    n_stars = round(bg_area / avg_pixel_gap)
    positions = []
    x_positions = []
    y_positions = []
    for i in range(n_stars):
        x = random.randrange(0, vw)
        while x in x_positions:
            x = random.randrange(0, vw)
        x_positions.append(x)

        y = random.randrange(0, vh)
        while y in y_positions:
            y = random.randrange(0, vh)
        y_positions.append(y)
        positions.append((x,y))

    min_chrome = 100
    stars_count = 0
    stars_alive = []
    for x,y in positions:
        if stars_count <= round(n_stars * 50/100):
            stars_alive.append(Dot('dot', (x, y), colors.WHITE))
        elif stars_count >= round(n_stars * 50/100) and stars_count <= round(n_stars * 75/100):
            chrome_focus = random.randrange(0, 3)
            if chrome_focus == 0:
                r = 255
                g = random.randrange(min_chrome, 256)
                b = random.randrange(min_chrome, 256)
            elif chrome_focus == 1:
                r = random.randrange(min_chrome, 256)
                g = 255
                b = random.randrange(min_chrome, 256)
            elif chrome_focus == 2:
                r = random.randrange(min_chrome, 256)
                g = random.randrange(min_chrome, 256)
                b = 255
            stars_alive.append(Dot('dot', (x, y), (r,g,b)))
        elif stars_count > round(n_stars * 75/100):
            chrome_focus = random.randrange(0,3)
            if chrome_focus == 2:
                color = {'color': (255,255,125), 'static_index': 2}
            else:
                color = {'color': colors.WHITE, 'static_index': None}
            stars_alive.append(Circle('circle', (x, y), color))

        stars_count += 1
    return stars_alive


def fix(bg_obj, stars):
    dotObj = pygame.PixelArray(bg_obj)
    for star in stars:
        kind = star.kind
        x = star.pos[0]
        y = star.pos[1]

        if kind == 'dot':
            dotObj[x][y] = star.color
        elif kind == 'circle':
            radii = star.radii
            time = star.timing()
            colors = star.colors
            pygame.gfxdraw.filled_circle(bg_obj, x, y, radii[time], colors[time])

    del dotObj