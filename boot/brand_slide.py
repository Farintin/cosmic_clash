import sys
import pygame
from pygame.locals import *


FPSClock = pygame.time.Clock()

def run(bg, vw, vh, vc):
    logo = pygame.image.load('game/src/img/ibrand_studios.png')
    logo_rect = logo.get_rect()
    logoAspectDim = (logo_rect.width, logo_rect.height)

    logo = pygame.transform.scale( logo, (150, round( 150/(logoAspectDim[0] / logoAspectDim[1]) ) ))
    logo_rect = logo.get_rect()
    logo_rect.center = vc

    FPS = 2
    slide1period = 3
    slide1FPSperiod = slide1period * FPS

    FPSsec_i = 0

    slide1 = True
    while slide1:
        bg.fill((0,0,0))
        bg.blit(logo, logo_rect.topleft)

        #bg.blit(bootSurf, (0,0))

        if FPSsec_i >= slide1FPSperiod:
            slide1 = False
            #FPSsec_i = 0
        else:
            FPSsec_i += 1


        for event in pygame.event.get(): # Event loop block
                e_type = event.type
                if e_type == QUIT:
                    pygame.quit()
                    sys.exit()


        pygame.display.update()
        FPSClock.tick(FPS)




if __name__ == '__main__':
    from game.src.ui import display
    vw = display.view_width
    vh = display.view_height
    vc = display.view_center
    bg = display.BACKGROUND
    run(bg, vw, vh, vc)