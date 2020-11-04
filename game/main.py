import sys, os
sys.path += [os.getcwd()]

import pygame
from pygame.locals import *
import db
from game.src import stars, controls, crafts
from game.src.celest import Bodies
from game.src.explode import action as explode_action
from game.src.ui import colors, features, dom
from game.src.ui.colors import bg_color
from game.src.ui.display import *
#from multiprocessing import Process


class Game:
    def __init__(self, Play = False, Level = None):
        self.score = 0

        self.level = Level

        self.craft = crafts.Craft1()

        self.items = []
        self.explosions = []

        self.bg_color = bg_color()
        self.bg_stars = stars.gen(vw, vh)

        self.Play = self.Played = Play
        self.Pause = False
        self.Won = self.Over = False

        self.Click = False
    '''def bodyProcess(self, object bg, object bg_alpha):
        self.renders = []
        for body in self.bodies.bodies:
            if body.rotation:
                body.rot()
            if body.surf_type == 'image':
                self.renders.append( body.show(bg, bg_alpha) )
            else:
                body.show(bg, bg_alpha)

            body.set_outline()
            
            body.show_shield(bg_alpha)
            #body.show_outline(bg_alpha)

            if body.shield < body.MAX_LIFE / 2 and body.flaming:
                if body.name == 'meteor':
                    body.flaming = False
                    body.vel[1] = 1
                
            fail = False
            if body.name == 'comet':
                if body.rect.top > vh:
                    #fail = True
                    body.exist = False
            elif body.smoothed_rot_y > vh:
                #fail = True
                body.exist = False
            self.over = fail
            if fail:
                break
            else:
                for shoot in self.craft.shoots: # Celest and Bullet collision event
                    for bullet in shoot:
                        if not body.exist:
                            break
                        for pt in bullet.outline_pos:
                            if pt in body.outline_pos:
                                body.shield -= bullet.power
                                body.show_outline(bg_alpha)

                                if body.shield <= 0:
                                    # Put Items
                                    unit = body.units
                                    unit.set_pos(body.pos)
                                    self.items.append(unit)
                                    if body.item.name != 'none':
                                        item = body.item
                                        item.set_pos(body.pos)
                                        self.items.append(item)
                                    ###333333333333333333333333333333333

                                    if body.rotation:
                                        body.pos = [body.smoothed_rot_x + body.ROT_DIM[0] / 2, body.smoothed_rot_y + body.ROT_DIM[1] / 2]
                                        self.explosions.append( explodeCy.Ripple(body.pos, explode_avg_rad = body.explode_avg_rad, explode_alpha = body.explode_alpha) )
                                        self.explosions.append( explodeCy.Scatter(body.pos, body.surf_colors) )
                                    else:
                                        self.explosions.append( explodeCy.Ripple(body.rect.center, explode_avg_rad = body.explode_avg_rad, explode_alpha = body.explode_alpha) )
                                        self.explosions.append( explodeCy.Scatter(body.rect.center, body.surf_colors) )

                                    body.exist = False
                                    self.score += 1

                                    bullet.exist = False
                                    break

                                bullet.exist = False
                                break
                                
                if body.bottom >= self.craft.rect.top:
                    for pt in body.outline_pos:
                        if pt[0] in range(self.craft.rect.left, self.craft.rect.right) and pt[1] in range(self.craft.rect.top, self.craft.rect.bottom):
                            if body.rotation:
                                body.pos = [body.smoothed_rot_x + body.ROT_DIM[0] / 2, body.smoothed_rot_y + body.ROT_DIM[1] / 2]
                            self.explosions.append(explodeCy.Ripple(body.pos, explode_avg_rad = body.explode_avg_rad, explode_alpha = body.explode_alpha))
                            self.explosions.append( explodeCy.Scatter(body.pos, body.surf_colors) )

                            body.exist = False

                            self.craft.shield -= body.power

                            if self.craft.shield <= 1:
                                self.over = True

                            self.craft.outline_color = colors.RED
                            self.craft.collide = True
                            break
                body.nav()


        for item in self.items:
            self.renders.append( item.show(bg_alpha) )

            #item.show_bounds(bg_alpha)

            if item.pos[1] > vh: # Terminate Item out of view bottom
                item.exist = False
            else:
                if item.rect.bottom >= self.craft.rect.top:
                    if pygame.sprite.collide_rect(item, self.craft):
                        if item.name == 'shield' and self.craft.shield < 3:
                            self.craft.shield += item.multi

                        item.exist = False

                        self.craft.outline_color = colors.SKYBLUE
                        self.craft.collide = True
                item.nav()'''
    
    def pause(self):
        if self.Pause:
            Quit = False
            while self.Pause:
                features.modal.show(bg_alpha)
            
                if self.Click:
                    if features.playBtn.onClick(pos = (mx_up, my_up)) or features.pauseBtn.onClick(pos = (mx_up, my_up)):
                        self.Pause = False
                    if features.backBtn.onClick(pos = (mx_up, my_up)):
                        self.Pause = self.Play = False
                    if not self.Pause:
                        for child in features.pauseBtn.children:
                            if child.name == 'poly':
                                child.visible = False
                            else:
                                child.visible = True

                    if features.quitBtn.onClick(pos = (mx_up, my_up)):
                        Quit = True

                    self.Click = False

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
                        self.Click = True

                ### Blit updating
                pygame.display.update()
                FPSClock.tick(15)

    def play(self):
        if self.Play:
            self.bodies = Bodies(self.level)
        while self.Play:
            bg.fill(self.bg_color)
            stars.fix(bg, self.bg_stars)

            bg_alpha.fill((0,0,0,0))

            self.run()
            features.show_all(bg_alpha, self.craft, self.score, self.level, self.bodies.attacks)

            self.pause()

            if self.Click:
                features.pauseBtn.onClick(pos = (mx_up, my_up))
                if features.pauseBtn.click:
                    self.Pause = True
                    for child in features.pauseBtn.children:
                        if child.name == 'rect':
                            child.visible = False
                        else:
                            child.visible = True

                self.Click = False
            
            self.won()
            self.over()


            bg.blit(bg_alpha, (0,0))


            ### Event loop block
            for event in pygame.event.get():
                kind = event.type

                if kind == QUIT:
                    pygame.quit()
                    sys.exit()

                if kind == MOUSEBUTTONUP:
                    mx_up, my_up = event.pos
                    self.Click = True

                if kind == KEYDOWN:
                    key = event.key

                    if key == K_ESCAPE:
                        self.bg_color = bg_color()
                        self.bg_stars = stars.gen(vw, vh)

                    if key == K_LEFT:
                        self.craft.dx = - int(self.craft.DIM[0] / 20)
                    elif key == K_RIGHT:
                        self.craft.dx = int(self.craft.DIM[0] / 20)

                    if key == K_UP:
                        self.craft.shooting = True
                        if not self.craft.rapid_strike:
                            self.craft.load_bullets()

                if kind == KEYUP:
                    key = event.key

                    if key == K_LEFT or key == K_RIGHT:
                        self.craft.dx = 0

                    if key == K_UP:
                        self.craft.shooting = False
                            

            pygame.display.update()
            FPSClock.tick(FPS)

        features.updateCraftsUnit(self.craft.units)### Update units

    def run(self):
        renders = []
        self.craft.action(bg, bg_alpha)

        if self.bodies.attacks < self.level.attacks:
            self.bodies.next()

        if self.bodies.attacks == self.level.attacks and not self.bodies.bodies and not self.items:
            self.Won = True

        for body in self.bodies.bodies:
            if not body.exist:
                self.bodies.bodies.remove(body)

        for item in self.items:
            if not item.exist:
                self.items.remove(item)

        '''bodiesAction = Process(target=self.bodyProcess(bg, bg_alpha))
        bodiesAction.start()
        bodiesAction.join()'''
        for body in self.bodies.bodies:
            if body.rotation:
                body.rot()
            if body.sprite_format == 'image':
                renders += body.show(bg_alpha)
            else:
                body.show(bg, bg_alpha)

            body.set_outline()
            
            body.show_life(bg_alpha)
            #body.show_outline(bg_alpha)

            if body.life < body.MAX_LIFE / 2 and body.flaming:
                if body.name == 'meteor':
                    body.flaming = False
                    body.vel[1] = 1
                
            '''body.terminate()
            if not body.exist:continue
                #self.over = True'''
            fail = False
            if body.name == 'comet':
                if body.rect.top > vh:
                    #fail = True
                    body.exist = False
            elif body.smoothed_rot_y > vh:
                #fail = True
                body.exist = False
            self.Over = fail
            if fail:
                break
            else:
                ### Celest and Craft collision event
                self.craft.body_collision(body, self.explosions)
                ### Celest and Bullet collision event
                for shoot in self.craft.shoots:
                    for bullet in shoot:
                        for pt in body.outline:
                            if pt in bullet.outline or (pt[0] in range(bullet.rect.left, bullet.rect.right) and pt[1] in range(bullet.rect.top, bullet.rect.bottom)):
                                body.life -= bullet.power
                                body.show_outline(bg_alpha)

                                if body.life <= 0:
                                    # Put Items
                                    if body.rotation:
                                        pos = body.pos
                                    else:
                                        pos = [body.rect.centerx, body.rect.centery]

                                    for item in body.items:
                                        if item.name:
                                            item.set_pos(pos)
                                            self.items.append(item)

                                    ### Set Explosion
                                    if body.rotation:
                                        explode_pos = [body.smoothed_rot_x + body.ROT_DIM[0] / 2, body.smoothed_rot_y + body.ROT_DIM[1] / 2]
                                    else:
                                        explode_pos = body.rect.center
                                    ripple = body.ripple
                                    ripple.set_pos(explode_pos)
                                    scatter = body.scatter
                                    scatter.set_pos(explode_pos)
                                    scatter.gen()
                                    self.explosions += [ripple, scatter]

                                    body.exist = False
                                    self.score += 1

                                bullet.exist = False
                                break
                body.move()

        if self.craft.shield < 1:
            self.Over = True
        #33333333333333333333333333333333333333333333333333333333333333333333333333

        ### Items obj loops
        for item in self.items:
            renders += item.show(bg_alpha)
            #item.show_bounds(bg_alpha)

            if item.name == 'unit':
                if item.top > vh: # Terminate Item out of view bottom
                    item.exist = False
            else:
                if item.pos[1] > vh: # Terminate Item out of view bottom
                    item.exist = False

            if not item.exist:
                continue
            else:
                self.craft.item_collision(item)
                if item.name == 'unit':
                    item.fall(self.craft)
                else:
                    item.nav(self.craft)


        if self.bodies.attacks == 1 and self.bodies.timer == 0:
            print(self.level.bodys_prob)
                

        # Explosions
        explode_action(self.explosions, bg_alpha)


        bg.blits(renders)


    def over(self):
        if self.Over:
            timer = 0
            Continue = True
            self.Click = False
            while self.Over:
                if db.document["item"]["items"]["life"]["bought"] and Continue:
                    features.continueModal.show(bg_alpha)
                    if self.Click:
                        if features.continueModalComp.yesBtn.onClick(pos = (mx_up, my_up)):
                            self.Over = False
                            Continue = False
                            db.document["item"]["items"]["life"]["bought"] = db.document["item"]["items"]["life"]["bought"] - 1
                            features.continueModalComp.render(features.continueModal)
                            self.craft.shield = self.craft.defaults['shield']
                        elif features.continueModalComp.noBtn.onClick(pos = (mx_up, my_up)):
                            Continue = False

                        self.Click = False
                else:
                    features.gameOver(bg_alpha)
                    timer += 1/15
                    if timer >= 3:
                        self.Over = False
                        self.Play = False


                bg.blit(bg_alpha, (0,0))

                
                for event in pygame.event.get(): ### Event loop block
                    kind = event.type

                    if kind == QUIT:
                        pygame.quit()
                        sys.exit()

                    if kind == MOUSEBUTTONUP:
                        mx_up, my_up = event.pos
                        self.Click = True

                ### Blit updating
                pygame.display.update()
                FPSClock.tick(15)

    def won(self):
        if self.Won:
            self.Play = False
            timer = 0
            features.setCurrentLevel(self.level.n + 1)
            features.updateLevelScore(self.level.n, self.score)
            while self.Won:
                features.won(bg_alpha)

                timer += 1/15
                if timer >= 3:
                    self.Won = False


                bg.blit(bg_alpha, (0,0))

                
                for event in pygame.event.get(): ### Event loop block
                    kind = event.type

                    if kind == QUIT:
                        pygame.quit()
                        sys.exit()

                ### Blit updating
                pygame.display.update()
                FPSClock.tick(15)


if __name__ == '__main__':
    from game.src import items
    items.life_gem_orbits_data = items.make_life_gem_orbs()
    from src.ui import sprites
    import levels
    stages, gridFrame, grid_h = levels.set_grids()
    n_level = 15
    level = stages[n_level - 1]
    game = Game(Play = True, Level = level)
    game.play()