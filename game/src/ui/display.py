import pygame

vw = view_width = 400
vh = view_height = 600
vc = view_center = (round(view_width / 2), round(view_height / 2))

bg = BACKGROUND = pygame.display.set_mode((view_width, view_height))
pygame.display.set_caption('Cosmic Clash')
bg_alpha = BACKGROUND.copy()
bg_alpha = bg_alpha.convert_alpha()

FPSClock = pygame.time.Clock()
FPS = 60
FPSsec = 1 / FPS
pygame.init()

fontObj = pygame.font.Font('freesansbold.ttf', 16)