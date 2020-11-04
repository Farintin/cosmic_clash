import pygame, sys
from pygame.locals import *
import boot, menu, levels
import db
from game.src.ui import display, features, dom
#from game.src import stars, controls, crafts
#from game.src.ui.colors import bg_color
from game.main import Game


### Setup pygame/window ---------------------------------------- #
FPSClock = display.FPSClock
FPS = display.FPS
FPSsec = display.FPSsec

vw = display.view_width
vh = display.view_height
vc = display.view_center

bg = display.BACKGROUND
bg_alpha = display.bg_alpha



def main():
    boot.run(bg, vw, vh, vc, display.FPS)

    Home = True
    Levels = False
    game = Game()
    while True:
        Home, Levels = menu.run(bg, bg_alpha, Home, Levels)
        state = levels.render(bg, bg_alpha, Home, Levels, game.Play)
        game.level = state['level']
        bools = state['bools']
        Levels = bools['self']
        Home = bools['home']
        game.Play = bools['play']

        game.play()
        if not game.Play and not Home:
            Levels = True 
            game = Game()


'''
def action(Level, Action, Levels):
    game = None
    if Action:
        from game.src.celest import Bodies

        colored_dark = bg_color()
        bg_stars = stars.gen(vw, vh)

        craft = crafts.Craft1()

        Won = False
        Over = False

        game = Game(craft, Level, Bodies, Won, Over)

        Click = False
        Pause = False
    while Action:
        bg.fill(colored_dark)
        stars.fix(bg, bg_stars)
        bg_alpha.fill((0,0,0,0))

        score, count, Won, Over = game.action(bg, bg_alpha)
        features.show_all(bg_alpha, craft, score, Level, count)

        Action, Pause, Levels = pause(Action, Pause, Levels)

        if Click:
            handler1 = dom.Handler( value = [Pause] )
            features.pauseBtn.onClick([handler1], (mx_up, my_up))[0]
            if features.pauseBtn.click:
                Pause = True
                for child in features.pauseBtn.children:
                    if child.name == 'rect':
                        child.visible = False
                    else:
                        child.visible = True

            Click = False
        

        if Won or Over:
            Action = False
            Levels = True
            Won = won(Level, Won, game)
            Over, Action, Levels = over(Over, Action, Levels, game)


        bg.blit(bg_alpha, (0,0))


        ### Event loop block
        for event in pygame.event.get():
            kind = event.type

            if kind == QUIT:
                pygame.quit()
                sys.exit()

            if kind == MOUSEBUTTONUP:
                mx_up, my_up = event.pos
                Click = True

            if kind == KEYDOWN:
                key = event.key

                if key == K_ESCAPE:
                    colored_dark = bg_color()
                    bg_stars = starsCy.gen(vw, vh)

                if key == K_LEFT:
                    craft.dx = - int(craft.DIM[0] / 20)
                elif key == K_RIGHT:
                    craft.dx = int(craft.DIM[0] / 20)

                if key == K_UP:
                    craft.shooting = True
                    if not craft.rapid_strike:
                        craft.load_bullets()

            if kind == KEYUP:
                key = event.key
                
                if key == K_LEFT or key == K_RIGHT:
                    craft.dx = 0

                if key == K_UP:
                    craft.shooting = False
                    

        pygame.display.update()
        FPSClock.tick(FPS)

    return {'game': game,
            'bools': {
                'self': Action,
                'levels': Levels
                }
            }'''


'''
def pause(Action, Pause, Levels):
    if Pause:
        Click = False
        Quit = False
    while Pause:
        features.modal.show(bg_alpha)
    
        if Click:
            handler1 = dom.Handler( value = [Pause] )
            init_pause = Pause
            features.playBtn.onClick([handler1], (mx_up, my_up))[0]
            features.pauseBtn.onClick([handler1], (mx_up, my_up))[0]

            if features.playBtn.click or features.pauseBtn.click:
                Pause = False

            handler1 = dom.Handler( value = [Action, Pause] )
            features.backBtn.onClick([handler1], (mx_up, my_up))[0]
            if features.backBtn.click:
                Action = False
                Pause = False
                Levels = True
            
            if not Pause:
                for child in features.pauseBtn.children:
                    if child.name == 'poly':
                        child.visible = False
                    else:
                        child.visible = True

            handler1 = dom.Handler( value = [Quit] )
            Quit, = features.quitBtn.onClick([handler1], (mx_up, my_up))[0]

            Click = False

        dom.egress(Quit)

        bg.blit(bg_alpha, (0,0))
        

        ### Event loop block
        for event in pygame.event.get():
            kind = event.type

            if kind == QUIT:
                pygame.quit()
                sys.exit()

            if kind == MOUSEBUTTONUP:
                mx_up, my_up = event.pos
                Click = True

            if kind == KEYDOWN:
                key = event.key

                if key == K_LEFT:
                    pass

                elif key == K_RIGHT:
                    pass

        ### Blit updating
        pygame.display.update()
        FPSClock.tick(15)
    
    return Action, Pause, Levels'''

'''
def over(Over, Action, Levels, game):
    if Over:
        timer = 0
        continueModal = True
        Click = False
        while Over:
            if db.document["item"]["items"]["life"]["bought"] and continueModal:
                features.continueModal.show(bg_alpha)
                if Click:
                    handler1 = dom.Handler( value = [Action, Over, Levels] )
                    Action, Over, Levels = features.continueModalComp.yesBtn.onClick([handler1], (mx_up, my_up))[0]
                    handler1 = dom.Handler( value = [Over] )
                    features.continueModalComp.noBtn.onClick([handler1], (mx_up, my_up))[0]

                    if features.continueModalComp.yesBtn.click and not Over and Action:
                        db.document["item"]["items"]["life"]["bought"] = db.document["item"]["items"]["life"]["bought"] - 1
                        features.continueModalComp.render(features.continueModal)
                        game.craft.shield = game.craft.defaults['shield']
                        game.over = False
                        continueModal = False
                    elif features.continueModalComp.noBtn.click:
                        continueModal = False

                    Click = False
            else:
                features.gameOver(bg_alpha)
                timer += 1/15
                if timer >= 3:
                    Over = False

            bg.blit(bg_alpha, (0,0))

            
            for event in pygame.event.get(): ### Event loop block
                kind = event.type

                if kind == QUIT:
                    pygame.quit()
                    sys.exit()

                if kind == MOUSEBUTTONUP:
                    mx_up, my_up = event.pos
                    Click = True

                if kind == KEYDOWN:
                    key = event.key

                    if key == K_LEFT:
                        pass

                    elif key == K_RIGHT:
                        pass

            ### Blit updating
            pygame.display.update()
            FPSClock.tick(15)

    return Over, Action, Levels'''

'''
def won(Level, Won, game):
    if Won:
        timer = 0
    while Won:
        features.won(bg_alpha)
        if timer == 0:### Update data
            features.setCurrentLevel(Level.n + 1)
            features.updateLevelScore(Level.n, game.score)

        timer += 1/15
        if timer >= 3:
            Won = False

        bg.blit(bg_alpha, (0,0))

        
        for event in pygame.event.get(): ### Event loop block
            kind = event.type

            if kind == QUIT:
                pygame.quit()
                sys.exit()

            if kind == KEYDOWN:
                key = event.key

                if key == K_LEFT:
                    pass

                elif key == K_RIGHT:
                    pass

        ### Blit updating
        pygame.display.update()
        FPSClock.tick(15)
    
    return Won'''




if __name__ == '__main__':
    main()