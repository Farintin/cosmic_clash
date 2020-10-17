import pygame
from pygame.locals import *
from game.src.ui import display
from game.src.ui.dom import *
from math import *
import db




FPSClock = pygame.time.Clock()

vw = display.view_width
vh = display.view_height
vc = display.view_center

bgImg = pygame.image.load('game/src/img/menu_bg.png')
bgImg_rect = bgImg.get_rect()

bgImgAspectDim = (bgImg_rect.width, bgImg_rect.height)
bgImg = pygame.transform.scale( bgImg, (round((bgImgAspectDim[0] / bgImgAspectDim[1]) * vh), vh) )
bgImg_rect = bgImg.get_rect()

bgImg_rect.midtop = (vc[0], 0)


surf = pygame.Surface((vw, vh))
surf = surf.convert_alpha()
surf.set_colorkey((0,0,0,0))
class Level:
    def __init__(self, n, x, y, attacks = 0):
        self.n = n
        self.dom_obj = Circle((255,255,255), 25, (x, y))
        children = (Circle((255,255,255,155), 15, (x, y)), Text(str(self.n), color = (155,155,155), font_size = 14))
        for child in children:
            child.id = 'sub_icon'
        self.dom_obj.addChildren( children )

        self.attacks = attacks

        self.body_probability = db.document['levels']['body_probability'][str(n)]

    def draw(self, bg_alpha):
        self.dom_obj.show(bg_alpha)

    def update(self):
        current = db.document['levels']['current']
        if self.n <= current:
            self.unlocked = True
        else:
            self.unlocked = False

        if self.n == current:
            self.current = True
        else:
            self.current = False




def render(bg, bg_alpha, Home, Levels, Action):
    selected = None

    if Levels:
        backBtn = Rect((8, 8, vw * 0.1, vw * 0.1), bgColor = (255,255,255,185))
        backBtn.borderWidth(2)
        backBtn.addChild( Text('Back', color = (225,225,225), font_size = 12) )
        backBtn.center_children()

        scrollFrame = Rect((vw - 8, 0, 8, vh), bgColor = (105,105,105,155))
        scrollBar = Rect((0,0, scrollFrame.rect.width,72), bgColor = (255,255,255,255))
        scrollBar.rect.bottomleft = scrollFrame.rect.bottomleft
        scrollFrame.addChild( scrollBar )

        stages, gridFrame, grid_h = set_grids()
        gridFrame.rect.top = -grid_h + vh
        i = 0
        for obj in gridFrame.children:
            obj.rect.centery = gridFrame.rect.top + obj.offSet[1]
            obj.center_children()

            stages[i].update()
            if stages[i].unlocked:
                obj.default['border_width'] = obj.border_width = 0
                obj.bg_color((255,45,255,225))
                obj.default['bg'] = obj.bg = True

                obj.getChildBy('name', 'circle').bg_color((255,255,255,255))
                child_text = obj.getChildBy('name', 'text')
                child_text.default['color'] = child_text.setColor((255,255,255))
                
            if stages[i].current:
                obj.default['border_width'] = obj.border_width = 0
                obj.bg_color((255,255,0,230))
                obj.default['bg'] = obj.bg = True

                obj.getChildBy('name', 'circle').bg_color((255,255,255,255))
                child_text = obj.getChildBy('name', 'text')
                child_text.default['color'] = child_text.setColor((255,255,255))

                current_lvl_dom = obj
                current_lvl = stages[i]
            i += 1


        MouseMotion = False
        Click = False
        Scroll_dy = 0
        MouseHeld = False
        MouseHeld_counter = 0
        ScrollBarFocus = False
        scrollRule = [vh - scrollBar.rect.height / 2, 0 + scrollBar.rect.height / 2]
        scrollRule.append( scrollRule[0] - scrollRule[1] )
        scrollBarPercent = 0
        init = True
    while Levels:
        mx, my = pygame.mouse.get_pos()

        bg.blit(bgImg, bgImg_rect.topleft)

        if Scroll_dy:
            if Scroll_dy > 0 and gridFrame.rect.top >= 0:
                Scroll_dy = 0
                gridFrame.rect.top = 0
            elif Scroll_dy < 0 and gridFrame.rect.bottom <= vh:
                Scroll_dy = 0
                gridFrame.rect.bottom = vh

            gridFrame.rect.top += Scroll_dy 
            for obj in gridFrame.children:
                obj.rect.centery = gridFrame.rect.top + obj.offSet[1]
                obj.center_children()
            
            scrollBar.rect.centery = -(((gridFrame.rect.top + (grid_h - vh)) / (grid_h - vh)) * scrollRule[2]) + scrollRule[0]


        if init:
            Tposy = vh - round(vh * 0.15)

            gridFrame.rect.top = -(grid_h - vh)
            gridFrame.rect.top += Tposy - current_lvl_dom.rect.centery
            for obj in gridFrame.children:
                obj.rect.centery = gridFrame.rect.top + obj.offSet[1]
                obj.center_children()

            scrollBar.rect.centery = -(((gridFrame.rect.top + (grid_h - vh)) / (grid_h - vh)) * scrollRule[2]) + scrollRule[0]
            init = False
        if ScrollBarFocus:
            scrollBar.rect.centery = my
            if scrollBar.rect.top <= 0:
                scrollBar.rect.top = 0
            elif scrollBar.rect.bottom >= vh:
                scrollBar.rect.bottom = vh
            
            scrollBarPercent = ( abs(scrollBar.rect.centery - scrollRule[0]) / scrollRule[2] ) * 100
            ScrollBar_dy = round( (grid_h - vh) * (scrollBarPercent / 100) )

            gridFrame.rect.top =  -((grid_h - vh) - ScrollBar_dy)
            for obj in gridFrame.children:
                obj.rect.centery = gridFrame.rect.top + obj.offSet[1]
                obj.center_children()
        else:
            ScrollBar_dy = 0
        

        if MouseMotion:
            handler1 = Handler( func = bgColor, value = {'bgColor': (255,255,255,255)} )
            handler2 = Handler( func = borderWidth, value = {'border_width': 0} )
            handler3 = Handler( func = color, value = {'color': (15,15,15,255)}, elem = backBtn.getChildBy('name', 'text') )
            backBtn.onHover([handler1, handler2, handler3], (mx, my))

            i = 0
            for lvl in gridFrame.children:
                handler1 = Handler( func = bg_state, value = {'bg': True} )
                if stages[i].unlocked:
                    handler2 = Handler( func = bgColor, value = {'bgColor': (45,255,45,225)} )
                else:
                    handler2 = Handler( func = bgColor, value = {'bgColor': (255,0,0,255)} )
                handler3 = Handler( func = bgColor, value = {'bgColor': (255,255,255,255)}, elem = lvl.getChildBy('name', 'circle') )
                handler4 = Handler( func = color, value = {'color': (255,255,255)}, elem = lvl.getChildBy('name', 'text') )

                lvl.onHover([handler1, handler2, handler3, handler4], (mx, my))
                i += 1


        gridFrame.show(bg_alpha)
        show_grids(bg_alpha, gridFrame)
        backBtn.show(bg_alpha)
        scrollFrame.show(bg_alpha)


        if MouseHeld:
            if MouseHeld_counter == 0:
                handler1 = Handler( value = [ScrollBarFocus] )
                ScrollBarFocus, = scrollBar.onClick([handler1], (mx_up, my_up))[0]
                
            MouseHeld_counter += 1
        else:
            MouseHeld_counter = 0
            ScrollBarFocus = False

        if Click:
            handler1 = Handler( value = [Home, Levels] )
            backBtn.onClick([handler1], (mx_up, my_up))[0]
            if backBtn.click:
                Home = True
                Levels = False

            i = 0
            handler1 = Handler( func = moveBack_moveOn, value = [Levels] )
            for lvl in gridFrame.children:
                '''if stages[i].unlocked:
                    handler1 = Handler( func = moveBack_moveOn, value = [Home, Levels] )
                    Home, Levels = lvl.onClick([handler1], (mx_up, my_up))[0]

                    if lvl.clicked:
                        #print('Clicked')
                        selected = stages[i]
                        lvl.clicked = False
                        break
                    '''
                lvl.onClick([handler1], (mx_up, my_up))[0]
                if lvl.click:
                    selected = stages[i]
                    #lvl.clicked = False
                    Levels = False
                    Action = True
                    break

                i += 1

            Click = False


        bg.blit(bg_alpha, (0,0))


        for event in pygame.event.get(): # Event loop block
            kind = event.type

            if kind == QUIT:
                pygame.quit()
                sys.exit()

            if kind == MOUSEMOTION:
                MouseMotion = True
            else:
                MouseMotion = False

            if kind == MOUSEBUTTONDOWN:
                mx_up, my_up = event.pos
                MouseHeld = True

            if kind == MOUSEBUTTONUP:
                mx_up, my_up = event.pos
                Click = True
                MouseHeld = False

            if kind == KEYDOWN:
                key = event.key
                if key == K_UP:
                    Scroll_dy = vh * 0.05
                if key == K_DOWN:
                    Scroll_dy = -vh * 0.05
            
            if kind == KEYUP:
                key = event.key
                if key == K_UP or key == K_DOWN:
                    Scroll_dy = 0


        pygame.display.update()
        FPSClock.tick(15)
    
    return {'level': selected,
            'bools': {
                'home': Home,
                'self': Levels,
                'action': Action
            }
        }




def set_grids(n_levels = 100):
    levels = []

    w_vec = -1
    w = round(vw * 0.5)
    h = round(vh * 0.15)

    grid_h = h * (n_levels + 2)
    
    gridFrame = Rect((0, 0, vw, grid_h), bgColor = (0,0,0,155))
    x = round(vw * 0.25)
    #y = round(vh * 0.85)
    y = grid_h - h

    ### Attacks preparation
    
    attacks = [5,10,15]
    for n in range(1, n_levels + 1):
        if len(attacks) < n_levels:
            if n > 3 and n <= 50:
                attacks += [n * 5] * 5
            elif n > 50:
                attacks += [n * 5] * 6
        else:
            break

    for n in range(1, n_levels + 1):
        attack = attacks[n - 1]
        lvl = Level(n, x, y, attacks = attack)
        lvl.dom_obj.offSet = (x, y)
        #lvl.dom_obj.state['bg'] = False
        #lvl.dom_obj.hovering['bg'] = True
        levels.append(lvl)
        gridFrame.addChild(lvl.dom_obj)

        x += w * (w_vec ** (n + 1))
        y -= h
    
    return levels, gridFrame, grid_h


def show_grids(bg_alpha, gridFrame):
    w = round(vw * 0.5)
    h = round(vh * 0.15)
    diag = sqrt(w ** 2 + h ** 2)
    sin = h / diag
    cos = w / diag

    rad = gridFrame.children[0].getChildBy('name', 'circle').radius
    dx = cos * rad
    dy = sin * rad

    i = 0
    slope_vec = -1
    for lvl_icon in gridFrame.children:
        if i > 0:
            vec = slope_vec ** (i + 1)
            
            centerx1, centery1 = gridFrame.children[i - 1].rect.center
            centerx2, centery2 = lvl_icon.rect.center
            if vec == 1:
                pt1 = (centerx1 + dx, centery1 - dy)
                pt2 = (centerx2 - dx, centery2 + dy)
            elif vec == -1:
                pt1 = (centerx1 - dx, centery1 - dy)
                pt2 = (centerx2 + dx, centery2 + dy)

            pygame.draw.aaline(bg_alpha, (255,255,255), pt1, pt2)
            
        i += 1




if __name__ == '__main__':
    bg = display.BACKGROUND
    bg_alpha = display.bg_alpha
    render(bg, bg_alpha, True, True)