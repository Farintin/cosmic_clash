from game.src.ui.display import *


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



sprites = Sprites()
sprites.load_rotated_sprites()
sprites.load_comet_outline()