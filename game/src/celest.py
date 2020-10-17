import pygame
from .ui.display import view_width, view_height, view_center, FPSsec
from .ui.colors import RED, YELLOW
from .items import *
from .explode import *
import random
import boot



vw = view_width
vh = view_height
vc = view_center

class Bodies:
    def __init__(self, level):
        self.level = level

        self.bodies = []
        '''self.body = Meteor( flame_glow = ((10,11),(116,136),(233,256)), alpha_frac = 0.8, vel = [0,1.7], mass = 2, life = 24, power = 3 )
        self.body.choose_items()'''
        '''self.body = Comet( mass = 0, life = 32, power = 6 )
        self.body.choose_items()
        self.bodies.append(self.body)'''

        self.time_range = (2,8)
        self.timer = self.time = random.randrange(self.time_range[0], self.time_range[1])

        self.attacks_count = 0
    
    def next(self):
        if self.timer >= self.time:
            self.choice = random.choice(self.level.body_probability)
            
            I = int(str(self.choice).split('.')[0])
            dec = int(str(self.choice).split('.')[1])

            mass = int(dec)
            life = int(8 * I + 8 * dec)
            power = int(I + dec)

            if I == 1:
                self.body = Meteorite(mass = mass, life = life, power = power)
                self.body.choose_items()
                self.bodies.append(self.body)
            elif I == 2:
                self.body = Meteor(mass = mass, life = life, power = power )
                self.body.choose_items()
                self.bodies.append(self.body)
            elif I == 3:### m blue
                self.body = Meteor( flame_glow = ((10,11),(116,136),(233,256)), alpha_frac = 0.8, vel = [0,1.7], mass = mass, life = life, power = power )
                self.body.choose_items()
                self.bodies.append(self.body)
            elif I == 4:### c blue-white
                self.body = Comet( mass = mass, life = life, power = power )
                self.body.choose_items()
                self.bodies.append(self.body)
            elif I == 5:### m red
                self.body = Meteor( flame_glow = ((243,256),(16,26),(3,8)), alpha_frac = 0.8, vel = [0,1.9], mass = mass, life = life, power = power )
                self.body.choose_items()
                self.bodies.append(self.body)
            elif I == 6:### m red-orange
                self.body = Meteor( flame_glow = ((233,256),(55,56),(10,11)), alpha_frac = 0.9, vel = [0,2.1], mass = mass, life = life, power = power )
                self.body.choose_items()
                self.bodies.append(self.body)
            elif I == 7:### c red-yellow
                self.body = Comet( vel = [0,2.4], mass = mass, life = life, power = power, core_color = [255,35,35], core_glow = [255,75,75], flame_glow = [255,255,0] )
                self.body.choose_items()
                self.bodies.append(self.body)
            elif I == 8:### m orange
                self.body = Meteor( flame_glow = ((233,256),(146,166),(30,31)), alpha_frac = 0.9, vel = [0,2.3], mass = mass, life = life, power = power )
                self.body.choose_items()
                self.bodies.append(self.body)
            elif I == 9:### m lemon
                self.body = Meteor( flame_glow = ((171,180),(251,256),(0,10)), alpha_frac = 0.8, vel = [0,2.5], mass = mass, life = life, power = power )
                self.body.choose_items()
                self.bodies.append(self.body)
            elif I == 10:### c 3
                self.body = Comet( vel = [0,2.8], mass = mass, life = life, power = power, core_color = [225,225,45], core_glow = [255,255,55], flame_glow = [75,205,75] )
                self.body.choose_items()
                self.bodies.append(self.body)
            elif I == 11:### m green
                self.body = Meteor( flame_glow = ((41,46),(251,256),(50,56)), alpha_frac = 0.8, vel = [0,2.7], mass = mass, life = life, power = power )
                self.body.choose_items()
                self.bodies.append(self.body)
            elif I == 12:### m aqua
                self.body = Meteor( flame_glow = ((0,10),(251,252),(191,192)), alpha_frac = 0.8, vel = [0,2.9], mass = mass, life = life, power = power )
                self.body.choose_items()
                self.bodies.append(self.body)
            elif I == 13:### c 4
                self.body = Comet( vel = [0,3.2], mass = mass, life = life, power = power, core_color = [0,155,0], core_glow = [25,185,25], flame_glow = [225,25,25] )
                self.body.choose_items()
                self.bodies.append(self.body)
            elif I == 14:### m pink
                self.body = Meteor( flame_glow = ((251,256),(51,56),(211,216)), alpha_frac = 0.85, vel = [0,3.1], mass = mass, life = life, power = power )
                self.body.choose_items()
                self.bodies.append(self.body)
            elif I == 15:### m white
                self.body = Meteor( flame_glow = ((221,256),(221,256),(221,256)), alpha_frac = 0.9, vel = [0,3.3], mass = mass, life = life, power = power )
                self.body.choose_items()
                self.bodies.append(self.body)
            elif I == 16:### c 5
                self.body = Comet( vel = [0,3.6], mass = mass, life = life, power = power, core_color = [235,235,235], core_glow = [255,255,255], flame_glow = [175,205,255] )
                self.body.choose_items()
                self.bodies.append(self.body)
            elif I == 17:### m violet
                self.body = Meteor( flame_glow = ((181,190),(1,10),(231,240)), alpha_frac = 0.8, vel = [0,3.5], mass = mass, life = life, power = power )
                self.body.choose_items()
                self.bodies.append(self.body)
            elif I == 18:### m aqua-green
                self.body = Meteor( glow_const = ((105,116),(105,116),(245,256)), flame_glow = ((0,1),(251,256),(250,256)), alpha_frac = 0.8, vel = [0,3.7], mass = mass, life = life, power = power )
                self.body.choose_items()
                self.bodies.append(self.body)
            elif I == 19:### c 6
                self.body = Comet( vel = [0,4], mass = mass, life = life, power = power, core_color = [255,125,0], core_glow = [255,155,55], flame_glow = [255,205,0] )
                self.body.choose_items()
                self.bodies.append(self.body)
            elif I == 20:### m blue-green 
                self.body = Meteor( glow_const = ((55,56),(55,56),(251,256)), flame_glow = ((1,3),(175,186),(1,3)), alpha_frac = 0.95, vel = [0,3.9], mass = mass, life = life, power = power )
                self.body.choose_items()
                self.bodies.append(self.body)
            elif I == 21:### m gold
                self.body = Meteor( glow_const = ((255,256),(140,166),(0,1)), flame_glow = ((255,256),(215,223),(0,1)), alpha_frac = 0.88, vel = [0,4.1], mass = mass, life = life, power = power )
                self.body.choose_items()
                self.bodies.append(self.body)
            elif I == 22:### c 7
                self.body = Comet( vel = [0,4.4], mass = mass, life = life, power = power, core_color = [45,205,255], core_glow = [75,225,255], flame_glow = [255,55,255] )
                self.body.choose_items()
                self.bodies.append(self.body)
            elif I == 23:### m invisble
                self.body = Meteor( glow_const = ((211,214),(211,214),(211,214)), flame_glow = ((190,196),(190,196),(190,196)), alpha_frac = 0.15, vel = [0,4.3], mass = mass, life = life, power = power )
                self.body.choose_items()
                self.bodies.append(self.body)
            
            self.attacks_count += 1
            #print(self.attacks_count, level.attacks)
            self.time = random.randrange(self.time_range[0], self.time_range[1])
            self.timer = 0
        self.timer += FPSsec



class Sprites:
    def __init__(self):
        self.mass1 = 1
        self.mass2 = 1.3
        self.mass3 = 1.6
        self.masses =  [self.mass1, self.mass2, self.mass3]

        meteorite = pygame.image.load('game/src/img/celest/meteorite.png').convert_alpha()
        aspect_ratio = meteorite.get_width() / meteorite.get_height()
        self.meteorite1 = pygame.transform.scale( meteorite, ( 55, round( 55 / aspect_ratio ) ) ).convert_alpha()
        self.meteorite1_DIM = (self.meteorite1.get_width(), self.meteorite1.get_height())
        self.meteorite2 = pygame.transform.scale( self.meteorite1, ( round(55 * self.mass2), round(55 / aspect_ratio * self.mass2) ) ).convert_alpha()
        self.meteorite2_DIM = (self.meteorite2.get_width(), self.meteorite2.get_height())
        self.meteorite3 = pygame.transform.scale( self.meteorite1, ( round(55 * self.mass3), round(55 / aspect_ratio * self.mass3) ) ).convert_alpha()
        self.meteorite3_DIM = (self.meteorite3.get_width(), self.meteorite3.get_height())
        self.meteorite_sprites = [self.meteorite1, self.meteorite2, self.meteorite3]

        self.meteor1 = pygame.image.load('game/src/img/celest/meteor.png').convert_alpha()
        self.meteor1_DIM = (self.meteor1.get_width(), self.meteor1.get_height())
        self.meteor2 = pygame.transform.scale( self.meteor1, (round(self.meteor1.get_width() * self.mass2), round(self.meteor1.get_height() * self.mass2)) ).convert_alpha()
        self.meteor2_DIM = (self.meteor2.get_width(), self.meteor2.get_height())
        self.meteor3 = pygame.transform.scale( self.meteor1, (round(self.meteor1.get_width() * self.mass3), round(self.meteor1.get_height() * self.mass3)) ).convert_alpha()
        self.meteor3_DIM = (self.meteor3.get_width(), self.meteor3.get_height())
        self.meteor_sprites = [self.meteor1, self.meteor2, self.meteor3]

        self.sprites = [self.meteorite_sprites, self.meteor_sprites]
        self.rot_angle_rate = 1

    def load_rotated_sprites(self):
        all_sprites_data = []
        for sprites in self.sprites:
            body_rot_sprites_data = []

            for sprite in sprites:
                rot_sprites_data = []

                for angle in range(0, 360, self.rot_angle_rate):
                    img_rot = pygame.transform.rotate(sprite, angle)
                    mask = pygame.mask.from_surface(img_rot)
                    rot_sprites_data.append( [img_rot, [pt for pt in mask.outline()], (img_rot.get_width(), img_rot.get_height())] )

                body_rot_sprites_data.append(rot_sprites_data)

            all_sprites_data.append(body_rot_sprites_data)

        self.meteorite_rotated_sprites_data1, self.meteorite_rotated_sprites_data2, self.meteorite_rotated_sprites_data3 = all_sprites_data[0]
        self.meteor_rotated_sprites_data1, self.meteor_rotated_sprites_data2, self.meteor_rotated_sprites_data3 = all_sprites_data[1]

    def load_comet_outline(self):
        comets_outlines = []
        for mass in self.masses:
            surf = pygame.Surface((vw, vh))
            surf = surf.convert_alpha()
            surf.set_colorkey((0,0,0,0))
            surf.fill((0,0,0,0))

            w = 32 * mass
            rad = round(w / 2)
            pygame.draw.circle(surf, (255,255,255,255), (rad, rad), rad)
            mask = pygame.mask.from_surface(surf)

            outline = []
            for pt in mask.outline():
                outline.append( (pt[0], pt[1]) )
            
            comets_outlines.append(outline)

        self.comet_outline1 = comets_outlines[0]
        self.comet_outline2 = comets_outlines[1]
        self.comet_outline3 = comets_outlines[2]




class Body:
    def __init__(self, life, power):
        self.exist = True
        self.items = []
        self.life = self.MAX_LIFE = life
        self.power = power

        self.fontObj = pygame.font.Font('freesansbold.ttf', 24)
        self.textSurfaceObj = self.fontObj.render('-'+str(self.power), False, (205,25,25))
        self.textRectObj = self.textSurfaceObj.get_rect()

        if self.sprite_format == 'drawn':
            self.pos = [ random.randrange(0 + round(8 * self.mass), round(vw - self.DIM[0]) - round(8 * self.mass)), - round(self.DIM[1]) ]
        else:
            self.pos = [ random.randrange( round(self.DIM[0] / 2), vw - self.DIM[0]), - self.DIM[1] ]
    
    def move(self):
        self.pos[1] += self.vel[1]
        self.bottom = self.pos[1] + self.DIM[1] / 3
    
    def choose_items(self):
        if self.items:
            self.items = [random.choice(self.items)()]
        self.items += [Unit()]

    def rot(self):
        self.img_rot, self.outline_lock, self.ROT_DIM = self.rotated_sprites_data[int(self.spin['angle'] / self.spin['rate'])]
        if self.spin['angle'] >= 359:
            self.spin['angle'] = 0
        else:
            self.spin['angle'] += self.spin['rate']
            
        self.smoothed_rot_x = round(self.pos[0]) - int(self.ROT_DIM[0] / 2)
        self.smoothed_rot_y = round(self.pos[1]) - round(self.ROT_DIM[1] / 2)

    def set_outline(self):
        self.outline = []
        for pt in self.outline_lock:
            self.outline.append([self.smoothed_rot_x + pt[0], self.smoothed_rot_y + pt[1]])

    def show(self, bg_alpha):
        return [(self.img_rot, (self.smoothed_rot_x, self.smoothed_rot_y))]
        
    def show_life(self, bg_alpha):
        x = self.pos[0] + self.DIM[0] / 2
        y = self.pos[1] - 15
        if x + self.MAX_LIFE + 2 < vw:
            pygame.draw.rect(bg_alpha, RED, (x, y, self.MAX_LIFE + 2, 3))
            pygame.draw.rect(bg_alpha, YELLOW, (x + 1, y + 1, self.life, 1))

            if self.pos[1] < 150:
                self.textRectObj.topleft = [x, y + 30]
        else:
            x = self.pos[0] - self.DIM[0] / 2 - self.MAX_LIFE + 2
            pygame.draw.rect(bg_alpha, RED, (x, y, self.MAX_LIFE + 2, 3))
            pygame.draw.rect(bg_alpha, YELLOW, (x + 1 + (self.MAX_LIFE - self.life), y + 1, self.life, 1))

            if self.pos[1] < 150:
                self.textRectObj.topright = [x + 1 + self.MAX_LIFE, y + 30]

        if self.pos[1] < 150:
            bg_alpha.blit(self.textSurfaceObj, self.textRectObj)
    
    def show_outline(self, bg_obj):
        pygame.draw.lines(bg_obj, RED, True, self.outline, 2)

    def terminate(self):
        # Terminate bodies out of view hieght
        if self.smoothed_rot_y > vh:
            self.exist = False
        '''else:
            if self.pos[1] > vh or self.rect.top > vh:
                self.exist = False'''


class Meteorite(Body):
    def __init__(self, mass = 0, life = 8, power = 1):
        self.name = 'meteorite'
        self.sprite_format = 'image'

        if mass == 0:
            self.mass = 1
            self.DIM = boot.processed_data['sprites'].meteorite1_DIM
            self.rotated_sprites_data = boot.processed_data['sprites'].meteorite_rotated_sprites_data1
        elif mass == 1:
            self.mass = 1.3
            self.DIM = boot.processed_data['sprites'].meteorite2_DIM
            self.rotated_sprites_data = boot.processed_data['sprites'].meteorite_rotated_sprites_data2
        elif mass == 2:
            self.mass = 1.6
            self.DIM = boot.processed_data['sprites'].meteorite3_DIM
            self.rotated_sprites_data = boot.processed_data['sprites'].meteorite_rotated_sprites_data3

        super().__init__(life, power)
        self.flaming = False
        self.rotation = True
        self.spin = {'angle': 0, 'rate': 1}
        
        self.vel = [0,1]
        self.bottom = self.pos[1] + self.DIM[1] / 3

        self.items = [Life]*1 + [Empty]*2 + [Shield]*4 + [Puffy]*8

        self.ripple_props = {
            'avg_r': 18 * self.mass,
            'out_speed': 1.5 * self.mass,
            'acce': 0.2 * self.mass,
            'color': [255,255,255,255],
            'color_decrement': (0,0,0,18)
            }
        self.ripple = Ripple(self.ripple_props)
        self.scatter_props = {
            'colors': [[132,116,101,255], [84,71,63,255]],
            'M': round(600 * self.mass),
            'acce': 0.012 * self.mass
        }
        self.scatter = Scatter(self.scatter_props)
    

class Meteor(Body):
    def __init__(self, mass = 0, life = 8, power = 1, vel = [0,1.7], glow_const = ((245,256),(245,256),(245,256)), flame_glow = ((233,256),(233,256),(0,102)), alpha_frac = 0.9):
        self.name = 'meteor'
        self.sprite_format = 'image'
        if mass == 0:
            self.mass = 1
            self.DIM = boot.processed_data['sprites'].meteor1_DIM
            self.rotated_sprites_data = boot.processed_data['sprites'].meteor_rotated_sprites_data1
        elif mass == 1:
            self.mass = 1.3
            self.DIM = boot.processed_data['sprites'].meteor2_DIM
            self.rotated_sprites_data = boot.processed_data['sprites'].meteor_rotated_sprites_data2
        elif mass == 2:
            self.mass = 1.6
            self.DIM = boot.processed_data['sprites'].meteor3_DIM
            self.rotated_sprites_data = boot.processed_data['sprites'].meteor_rotated_sprites_data3

        super().__init__(life, power)
        self.flaming = True
        self.rotation = True
        self.spin = {'angle': 0, 'rate': 1}

        self.vel = vel
        self.bottom = self.pos[1] + self.DIM[1] / 2

        self.prop = {'pt': (int(self.DIM[0] / 2), int(self.DIM[1] * 0.65)),
                        'acce': (0,0.02)
                        }
        self.props = {'rad_range': range(round(20 * self.mass), round(24 * self.mass)),
                        'vel': ({'min': -0.1, 'max': 0.1},-1),
                        'redux_rate': 0.5 * self.mass,
                        'const_color_range': glow_const,
                        'color_range': flame_glow,
                        'alpha_frac': alpha_frac
                        }
        self.flame = Flame(self.prop, self.props)
        #self.life = self.MAX_LIFE = 24
        #self.power = 2
        self.items = [Life]*1 + [Empty]*4 + [Shield]*4 + [Magnet]*8 + [Rapid]*16 + [Puffy]*32

        self.ripple_props = {
            'avg_r': 18 * self.mass,
            'out_speed': 1.5 * self.mass,
            'acce': 0.2 * self.mass,
            'color': [255,255,255,255],
            'color_decrement': (0,0,0,12)
            }
        self.ripple = Ripple(self.ripple_props)
        self.scatter_props = {
            'colors': [[181,114,59,255], [99,55,28,255], [39,39,39,255]],
            'M': round(600 * self.mass),
            'acce': 0.012 * self.mass
        }
        self.scatter = Scatter(self.scatter_props)

    def show(self, bg_alpha):
        if self.flaming:
            self.prop['pt'] = (round(self.ROT_DIM[0] / 2), round(self.ROT_DIM[1] * 0.65))
            self.flame.combust(bg_alpha, [self.smoothed_rot_x, self.smoothed_rot_y], self.prop['pt'])
        return super().show(bg_alpha)
    

class Comet(Body):
    def __init__(self, mass = 0, life = 8, power = 1, vel = [0,2], core_color = [155,155,255], core_glow = [155,155,255], flame_glow = [255,255,255]):
        self.name = 'comet'
        self.sprite_format = 'drawn'

        if mass == 0:
            self.mass = 1
            self.outline_lock = boot.processed_data['sprites'].comet_outline1
        elif mass == 1:
            self.mass = 1.3
            self.outline_lock = boot.processed_data['sprites'].comet_outline2
        elif mass == 2:
            self.mass = 1.6
            self.outline_lock = boot.processed_data['sprites'].comet_outline3
        self.outline = []
        self.DIM = [32 * self.mass]*2
        #self.rad = round(self.w / 2)
        super().__init__(life, power)
        self.flaming = True
        self.rotation = False

        self.color = core_color

        self.rect = pygame.Rect(self.pos[0], self.pos[1], self.DIM[0], self.DIM[1])
        self.vel = vel
        self.bottom = self.rect.top + self.rect.height

        if mass == 0:
            pty = 17
        elif mass == 1:
            pty = 21
        elif mass == 2:
            pty = 24
        self.prop1 = {'pt': (0, pty),
                        'ax': 0
                        }
        self.props1 = {'rad_range': range(round(5 * self.mass), round(5 * self.mass + 1)),
                        'vel': ({'min': -3, 'max': 3}, 1.3),
                        'redux_rate': 0.25 * self.mass,
                        'colors': [core_glow + [155], flame_glow + [155]]
                        }
        self.coma1 = Coma(self.prop1, self.props1)

        if mass == 0:
            pty = 14
        elif mass == 1:
            pty = 17
        elif mass == 2:
            pty = 20
        self.prop2 = {'pt': (0, pty),
                        'ax': 0
                        }
        self.props2 = {'rad_range': range(round(10 * self.mass), round(10 * self.mass + 1)),
                        'vel': ({'min': -2, 'max': 2}, -0.1),
                        'redux_rate': 0.38 * self.mass,
                        'colors': [core_glow + [125]] + [flame_glow + [125]] * 3
                        }
        self.coma2 = Coma(self.prop2, self.props2)
        self.prop3 = {'pt': (0,6),
                        'ax': 0
                        }
        self.props3 = {'rad_range': range(round(16 * self.mass), round(16 * self.mass + 1)),
                        'vel': ({'min': -1.4, 'max': 1.4}, -2),
                        'redux_rate': 0.8 * self.mass,
                        'colors': [flame_glow + [155]]
                        }
        self.coma3 = Coma(self.prop3, self.props3)
        self.prop4 = {'pt': (0,8),
                        'ax': 0.1
                        }
        self.props4 = {'rad_range': range(round(20 * self.mass), round(20 * self.mass + 1)),
                        'vel': ({'min': -1, 'max': 1}, -8),
                        'redux_rate': 1 * self.mass,
                        'colors': [flame_glow + [205]]
                        }
        self.coma4 = Coma(self.prop4, self.props4)

        self.items = [Life]*1 + [Empty]*4 + [Bubble]*400 + [Shield]*400 + [Magnet]*12 + [Rapid]*24 + [Puffy]*32

        self.ripple_props = {
            'avg_r': 32 * self.mass,
            'out_speed': 2 * self.mass,
            'acce': 0.4 * self.mass,
            'color': flame_glow + [255],
            'color_decrement': (0,0,0,0)
            }
        self.ripple = Ripple(self.ripple_props)
        self.scatter_props = {
            'colors': [flame_glow + [255]] + [core_glow + [255]] * 3,
            'M': round(600 * self.mass),
            'acce': 0.013 * self.mass
        }
        self.scatter = Scatter(self.scatter_props)

    ### Unique
    def move(self):
        #self.pos[1] += self.vel[1]
        self.rect.top += self.vel[1]
        self.bottom = self.rect.top + self.rect.height

    def set_outline(self):
        self.outline = []
        for pt in self.outline_lock:
            self.outline.append([self.rect.left + pt[0], self.rect.top + pt[1]])

    def show(self, bg_obj, bg_alpha):
        self.coma3.outgas(bg_obj, bg_alpha, self.rect.center)
        self.coma2.outgas(bg_obj, bg_alpha, self.rect.center)
        self.coma4.eject(bg_obj, bg_alpha, self.rect.center)
        self.coma1.outgas(bg_obj, bg_alpha, self.rect.center)
        pygame.draw.circle( bg_alpha, self.color, ( int(self.rect.centerx), int(self.rect.centery) ), round(self.DIM[0] / 2) )
        #pygame.draw.rect(bg_alpha, RED, self.rect, 1)
        #pygame.draw.line(bg_alpha, RED, (self.rect.left, self.rect.top + self.rect.height), (self.rect.left + self.rect.width, self.rect.top + self.rect.height))
    
    def show_life(self, bg_alpha):
        x = self.rect.left + self.DIM[0] + round(16 * self.mass)
        y = self.rect.top - 8
        if x + self.MAX_LIFE + 2 < vw:
            pygame.draw.rect(bg_alpha, RED, (x, y, self.MAX_LIFE + 2, 3))
            pygame.draw.rect(bg_alpha, YELLOW, (x + 1, y + 1, self.life, 1))

            if self.rect.top < 150:
                self.textRectObj.topleft = [x, y + 30]

        else:
            x = self.rect.left - self.DIM[0] + round(16 * self.mass) - self.MAX_LIFE + 2
            pygame.draw.rect(bg_alpha, RED, (x, y, self.MAX_LIFE + 2, 3))
            pygame.draw.rect(bg_alpha, YELLOW, (x + 1 + (self.MAX_LIFE - self.life), y + 1, self.life, 1))

            if self.rect.top < 150:
                self.textRectObj.topright = [x + 1 + self.MAX_LIFE, y + 30]

        if self.rect.top < 150:
            bg_alpha.blit(self.textSurfaceObj, self.textRectObj)
    
    def terminate(self):
        # Terminate bodies out of view hieght
        if self.pos[1] > vh or self.rect.top > vh:
            self.exist = False
