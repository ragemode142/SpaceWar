import pygame as pg
import random
import pygame.freetype as pf


class Korablik:
    def __init__(self):
        self.speed = 5
        self.picture = pg.image.load('korabl.png')
        self.picture = pg.transform.scale(self.picture, [200, 200])
        self.hitbox = pg.rect.Rect(600, 700, 200, 200)
        self.live = 3
        self.kills = 0
    def draw(self, okno):
        okno.blit(self.picture, self.hitbox)
    def fly(self):
        buttons = pg.key.get_pressed()
        if buttons[pg.K_d] == True and self.hitbox.right < 1400:
            self.hitbox.x = self.hitbox.x + self.speed
        if buttons[pg.K_a] == True and self.hitbox.x > 0:
            self.hitbox.x = self.hitbox.x - self.speed
        if buttons[pg.K_w] == True and self.hitbox.y > 0:
            self.hitbox.y = self.hitbox.y - self.speed
        if buttons[pg.K_s] == True and self.hitbox.bottom < 900:
            self.hitbox.y = self.hitbox.y + self.speed


class Meteorit:
    def __init__(self):
        self.picture = pg.image.load('meteor.png')
        razmer = self.picture.get_size()
        shirina = razmer[0]
        dlina = razmer[1]
        number1 = random.randint(5, 20)
        self.picture = pg.transform.scale(self.picture, [shirina/number1, dlina/number1])
        razmer = self.picture.get_size()
        self.hitbox = pg.rect.Rect([random.randint(0, 1400), 0], razmer)
        self.speed_x = random.randint(-2, 2)
        self.speed_y = random.randint(2, 8)
    def draw(self, okno):
        okno.blit(self.picture, self.hitbox)
    def fly(self):
        self.hitbox.x = self.hitbox.x + self.speed_x
        self.hitbox.y = self.hitbox.y + self.speed_y


class Lazer:
    def __init__(self, x, y):
        self.picture = pg.image.load('lazer.png')
        self.picture = pg.transform.scale(self.picture, [20, 30])
        self.speed = 8
        self.hitbox = pg.rect.Rect(x, y, 20, 30)
    def draw(self, okno):
        okno.blit(self.picture, self.hitbox)
    def fly(self):
        self.hitbox.y = self.hitbox.y - self.speed


class Buttons:
    def __init__(self, x, y, text, a, b):
        self.picture = pg.image.load('assets/PNG/UI/buttonRed.png')
        self.picture = pg.transform.scale(self.picture, [400, 60])
        razmer = self.picture.get_size()
        shirina = razmer[0]
        dlina = razmer[1]
        self.hitbox = pg.rect.Rect(x, y, shirina, dlina)
        self.risovlka = pf.Font('shrift2.otf', 70)
        self.text = text
        self.a = a
        self.b = b
    def draw(self, okno):
        okno.blit(self.picture,self.hitbox)
        self.risovlka.render_to(okno, [self.hitbox.x + self.a, self.hitbox.y + self.b], self.text)

