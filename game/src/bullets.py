import pygame
from .ui import display


vw = display.view_width
vh = display.view_height

surf = pygame.Surface((vw, vh))
surf = surf.convert_alpha()
surf.set_colorkey((0,0,0,0))
class Bullet:
    def __init__(self, pos, power):
        self.mask = pygame.mask.from_surface(surf)
        self.outline_lock = []
        for pt in self.mask.outline():
            self.outline_lock.append((pt[0], pt[1]))
        self.outline = []
        
        self.exist = True
        self.power = power
        self.pos = self.pos_init = pos
        self.puffed = False


class Craft1(Bullet):
    def __init__(self, pos, rad, power):
        super().__init__(pos, power)
        self.vel = [0,-5]
        self.color = (255, 205, 55, 255)
        self.rad = rad
        self.rad_init = 2

        surf.fill((0,0,0,0))
        pygame.draw.circle(surf, (255,255,255,255), (self.rad, self.rad), self.rad)
        '''if self.rad > self.rad_init:
            pygame.draw.circle(surf, (255,255,255,255), (self.rad, self.rad), self.rad)
        else:
            pygame.draw.circle(surf, (255,255,255,255), (self.rad_init, self.rad_init), self.rad_init)'''
        '''if self.rad > 2:
            rect_w = round(self.rad / 2)
        else:
            rect_w = 1
        self.rect = pygame.Rect(0,0, rect_w, self.rad * 8)'''
        self.rect = pygame.Rect(0,0, 1, self.rad_init * 8)
        
    def draw(self, bg_obj):
        if self.puffed:
            pygame.draw.circle(bg_obj, self.color, self.pos, self.rad)
        else:
            pygame.draw.circle(bg_obj, self.color, self.pos, self.rad_init)

    def draw_outline(self, bg_obj):
        pygame.draw.lines(bg_obj, (255,255,255), True, self.outline)
        pygame.draw.rect(bg_obj, (255,0,0), self.rect, 1)
    
    def move(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        if not self.puffed and (self.rad > self.rad_init) and (self.pos[1] + self.rad < self.pos_init[1] - 40):
            self.rect = pygame.Rect(0,0, round(self.rad / 2), self.rad * 8)
            self.puffed = True
        self.rect.midtop = self.pos

    def update_outline(self):
        self.outline = []
        for pt in self.outline_lock:
            self.outline.append( [self.pos[0] + pt[0] - self.rad, self.pos[1] + pt[1] -self.rad] )