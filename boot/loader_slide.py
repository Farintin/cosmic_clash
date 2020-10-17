import sys, random
import pygame
from pygame.locals import *
from game.src import items
from game.src.celest import Sprites


FPSClock = pygame.time.Clock()

def run(bg, vw, vh, vc, FPS):
    bgImg = pygame.image.load('game/src/img/bg_and_title.png')
    bgImg_rect = bgImg.get_rect()
    bgImgAspectDim = (bgImg_rect.width, bgImg_rect.height)
    bgImg = pygame.transform.scale( bgImg, (vw, round( vw/(bgImgAspectDim[0] / bgImgAspectDim[1]) ) ))

    loadingBarFrame = pygame.Rect(0,0, vc[0], 2)
    loadingBarFrame.center = (vc[0], round(vh * 0.8))

    loadingBar = pygame.Rect((0,0,0,2))
    loadingBar.topleft = loadingBarFrame.topleft

    slide2period = 7
    slide2FPSperiod = slide2period * FPS

    heavyLoadPoint1 = random.randint(1, int(slide2FPSperiod * 0.5))
    heavyLoadPoint2 = random.randint(int(slide2FPSperiod * 0.5) + 1, slide2FPSperiod)

    FPSsec_i = 0

    slide2 = True
    sprites = None
    while slide2:
        bg.blit(bgImg, (0,0))

        pygame.draw.rect(bg, (55,55,55), loadingBarFrame)
        pygame.draw.rect(bg, (255,255,255), loadingBar)

        if loadingBar.width >= loadingBarFrame.width:
            slide2 = False
        else:
            FPSsec_i += 1
            loadingBar.width = round((FPSsec_i / slide2FPSperiod) * loadingBarFrame.width)

        #bg.blit(bootSurf, (0,0))

        ### Load heavy hardware processing codes
        if FPSsec_i == heavyLoadPoint1:#round(0.3 * slide2FPSperiod):
            items.life_gem_orbits_data = items.make_life_gem_orbs()
            #life = items.Life()
            #del life
        elif FPSsec_i == heavyLoadPoint2:
            sprites = Sprites()
            sprites.load_rotated_sprites()
            sprites.load_comet_outline()

        ###333333333333333333333333333333333333333333333


        for event in pygame.event.get(): # Event loop block
                e_type = event.type
                if e_type == QUIT:
                    pygame.quit()
                    sys.exit()


        pygame.display.update()
        FPSClock.tick(FPS)
    return {'sprites': sprites}





if __name__ == '__main__':
    from game.src.ui import display
    FPS = display.FPS
    vw = display.view_width
    vh = display.view_height
    vc = display.view_center
    bg = display.BACKGROUND
    run(bg, vw, vh, vc, FPS)