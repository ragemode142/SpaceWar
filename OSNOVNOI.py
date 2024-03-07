import pygame as pg
import sprite as sp
import pygame.freetype as pf
pg.init()


def hit_Meteor_and_korablik():
    for meteor in spisok_M:
        if meteor.hitbox.colliderect(korabl.hitbox) == True:
            spisok_M.remove(meteor)
            korabl.live = korabl.live - 1
            return True
    return False

def hit_lazer_and_meteor():
    for lazer in spisok_L:
        for meteor in spisok_M:
            if lazer.hitbox.colliderect(meteor.hitbox) == True:
                spisok_L.remove(lazer)
                spisok_M.remove(meteor)
                korabl.kills = korabl.kills + 1



# окно
okoshko = pg.display.set_mode([1400, 900])
a = 1

# загрузка фона
fon = pg.image.load('fon.jpg')
new_fon = pg.transform.scale(fon, [1400, 900])

# загрузка меню
menu = pg.image.load('menu.jpg')
new_menu = pg.transform.scale(menu, [1400, 900])
game = 0

# загрузка статы
stata = pg.image.load('stata.jpg')
new_stata = pg.transform.scale(stata, [1400, 900])
shrift = pf.Font('shrift3.otf', 60)
time1 = 0
lose_time = 0
Time = 0

# загрузка жизней
lives = pg.image.load('lives.png')
new_lives = pg.transform.scale(lives, [ 50, 50])

# звуки
music = pg.mixer.Sound('музыка.wav')
lazer_music = pg.mixer.Sound('звук лазера.wav')
lazer_music.set_volume(0.05)
music.set_volume(0.05)

# корабль
korabl = sp.Korablik()

# лазеры
spisok_L = []

# метеориты
spisok_M = []
number = pg.USEREVENT
pg.time.set_timer(number, 500)

# кнопки
button = sp.Buttons(500, 700, 'Start', 90, 8)
button2 = sp.Buttons(500, 780, 'Exit', 90, 7)
button3 = sp.Buttons(0, 0, 'Main menu', 10, 8)

#  часы
clock = pg.time.Clock()

# код игры
music.play(-1)
while a == 1:
    # отрисовка
    if game == 1:
        okoshko.blit(new_fon, [0, 0])
        korabl.draw(okoshko)
        music.set_volume(0.02)
        if korabl.live == 3:
            okoshko.blit(new_lives, [1250, 0])
            okoshko.blit(new_lives, [1300, 0])
            okoshko.blit(new_lives, [1350, 0])
        elif korabl.live == 2:
            okoshko.blit(new_lives, [1250, 0])
            okoshko.blit(new_lives, [1300, 0])
        elif korabl.live == 1:
            okoshko.blit(new_lives, [1250, 0])
        for meteor in spisok_M:
            meteor.draw(okoshko)
            meteor.fly()
        for lazer in spisok_L:
            lazer.draw(okoshko)
            lazer.fly()
        pg.display.update()

        # логика игры
        korabl.fly()
        hit = hit_Meteor_and_korablik()
        if korabl.live == 0:
            game = 2
            lose_time = pg.time.get_ticks()
            Time = lose_time - time1
        hit_lazer_and_meteor()

    elif game == 0:
        okoshko.blit(new_menu, [0, 0])
        button.draw(okoshko)
        button2.draw(okoshko)
        pg.display.update()
    elif game == 2:
        okoshko.blit(new_stata, [0, 0])
        shrift.render_to(okoshko, [500, 200], 'Statistics', [255, 255, 255])
        shrift.render_to(okoshko, [500, 300], 'Kills: '+ str(korabl.kills), [255, 255, 255])
        shrift.render_to(okoshko, [500, 400], 'Time: '+ str(Time // 1000), [255, 255, 255])
        button3.draw(okoshko)
        pg.display.update()


    # обработка событий
    sobitia = pg.event.get()
    for sobitie in sobitia:
        if sobitie.type == pg.QUIT:
            a = a + 1
        if sobitie.type == number and game == 1:
            danger = sp.Meteorit()
            spisok_M.append(danger)
        if sobitie.type == pg.MOUSEBUTTONDOWN:
            if game == 1:
                gun = sp.Lazer(korabl.hitbox.centerx, korabl.hitbox.top)
                spisok_L.append(gun)
                lazer_music.play()
            else:
                if button.hitbox.collidepoint(sobitie.pos):
                    game = 1
                    korabl = sp.Korablik()
                    spisok_M = []
                    spisok_L = []
                    time1 = pg.time.get_ticks()

                if button2.hitbox.collidepoint(sobitie.pos):
                    a = a + 1
                if button3.hitbox.collidepoint(sobitie.pos):
                    game = 0
    clock.tick(144)


