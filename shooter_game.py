from pygame import*
from random import randint
new_ship = 1
more_diamonds = 1
n = randint(1, 3)
ship_type = 'atc_cmn1'
b = 1
c = 2
s_score = 0
sc = 1
shield_health = 0
shield_act = False
window = display.set_mode((700, 500))
display.set_caption('Space shooter')
finish = False
pause = False
score = 0
best_score = 0
last_best_score = 0
b_score = False
health = 5
max_health = 5
menu_money = 100
game_money = 0
menu_diams = 0
game_diams = 0
cd = 30
r1 = 1
r2 = 5
ship_shield_common1 = False
ship_help_common1 = False
font.init()
f = font.SysFont(None, 70)
lose = f.render('Поражение', True, (255, 0, 0))
f2 = font.SysFont(None, 45)
f3 = font.SysFont(None, 25)
f4 = font.SysFont(None, 30)
f5 = font.SysFont(None, 10)
f6 = font.SysFont(None, 50)
present3 = f6.render('1', True, (255, 255, 255))
cost = f3.render('100', True, (0, 0, 0))
version = f4.render('v0.1', True, (255, 255, 255))
new_record = f2.render('Новый рекорд!', True, (255, 195, 14))
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_speed, player_x, player_y, s_x, s_y):
        super().__init__()
        self.s_x = s_x
        self.s_y = s_y
        self.speed = player_speed
        self.image = transform.scale(image.load(player_image), (s_x, s_y))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def __init__(self, image, speed, x, y, s_x, s_y, type):
        super().__init__(image, speed, x, y, s_x, s_y)
        self.type = type
    def moving(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 430:
            self.rect.y += self.speed
        if keys_pressed[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x < 630:
            self.rect.x += self.speed
    def death(self):
        self.image = transform.scale(image.load('death.png'), (self.s_x, self.s_y)) 
    def damage(self):
        self.image = transform.scale(image.load('damage.png'), (self.s_x, self.s_y)) 
    def undamage(self):
        self.image = transform.scale(image.load('ship.png'), (self.s_x, self.s_y)) 
    def restart(self):
        self.rect.x = 300
        self.rect.y = 400
    def restart2(self):
        self.rect.x = 337
        self.rect.y = 437
    def red(self, type):
        if type == 'atc_cmn1':
            self.image = transform.scale(image.load('ship1.png'), (self.s_x, self.s_y)) 
        elif type == 'shd_cmn1':
            self.image = transform.scale(image.load('ship2.png'), (self.s_x, self.s_y)) 
        else:
            self.image = transform.scale(image.load('ship3.png'), (self.s_x, self.s_y)) 
class Enemy(GameSprite):
    def __init__(self, image, speed, x, y, s_x, s_y):
        super().__init__(image, speed, x, y, s_x, s_y)
    def update(self, r1, r2):
        rand_x = randint(25, 625)
        rand_y = randint(-250, -100)
        if self.rect.y < 500:
            self.rect.y += self.speed
        else:
            self.rect.y = rand_y
            self.rect.x = rand_x
            randspeed = randint(r1, r2)
            self.speed = randspeed
# class StrongEnemy(GameSprite):
#     def __init__(self, image, speed, x, y, s_x, s_y, health):
#         super().__init__(image, speed, x, y, s_x, s_y)
#         self.health = 3
#         h = self.health
#     def update(self):
#         rand_x = randint(25, 625)
#         rand_y = randint(-250, -100)
#         if self.rect.y < 500:
#             self.rect.y += self.speed
#         else:
#             self.rect.y = rand_y
#             self.rect.x = rand_x
#             randspeed = randint(2, 5)
#             self.speed = randspeed
#         global shoot
#         h = self.health
#         if shoot == 1:
#             self.health -= 1
#             shoot = 0
#             self.image = transform.scale(image.load('Damaged_meteorit.png'), (self.s_x, self.s_y))
#             display.update()
#             self.image = transform.scale(image.load('прочный_метеорит.png'), (self.s_x, self.s_y))
#         if h == 0:
#             rand_x = randint(25, 625)
#             rand_y = randint(-250, -100)
#             self.rect.y = rand_y
#             self.rect.x = rand_x
#             randspeed = randint(2, 5)
#             self.speed = randspeed
#             self.health = 3
class Bullet(GameSprite):
    def __init__(self, image, speed, x, y, s_x, s_y):
        super().__init__(image, speed, x, y, s_x, s_y)
    def update(self):
        self.rect.y -= self.speed
class Money(Enemy):
    def __init__(self, image, speed, x, y, s_x, s_y, type):
        super().__init__(image, speed, x, y, s_x, s_y)
        self.type = type          
    def update(self):
        rand_x = randint(25, 625)
        rand_y = randint(-250, -100)
        if self.rect.y < 500:
            self.rect.y += self.speed
        else:
            self.rect.y = rand_y
            self.rect.x = rand_x
class Box(GameSprite):
    def __init__(self, image, speed, x, y, s_x, s_y):
        super().__init__(image, speed, x, y, s_x, s_y)
    def moving(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 465:
            self.rect.y += self.speed
        if keys_pressed[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x < 630:
            self.rect.x += self.speed
    def restart(self):
        self.rect.x = 300
        self.rect.y = 447
class Button(GameSprite):
    def __init__(self, image, speed, x, y, s_x, s_y, t_b):
        self.t_b = t_b
        self.u_t = image
        super().__init__(image, speed, x, y, s_x, s_y)
    def draw(self):
        m = mouse.get_pos()
        if self.rect.x < m[0] < self.rect.x+self.s_x and self.rect.y < m[1] < self.rect.y+self.s_y:
            self.image = transform.scale(image.load(self.t_b), (self.s_x, self.s_y)) 
        else:
            self.image = transform.scale(image.load(self.u_t), (self.s_x, self.s_y))
class Bar(GameSprite):
    def __init__(self, image, speed, x, y, s_x, s_y):
        super().__init__(image, speed, x, y, s_x, s_y)
    def draw(self, an, max_an):
        if max_an - an == 0:
            self.image = transform.scale(image.load('h_b1.png'), (self.s_x, self.s_y)) 
        elif max_an - an == 1 and max_an == 7:
            self.image = transform.scale(image.load('h_b2_1.png'), (self.s_x, self.s_y)) 
        elif max_an - an == 2 and max_an == 7:
            self.image = transform.scale(image.load('h_b3_1.png'), (self.s_x, self.s_y)) 
        elif max_an - an == 3 and max_an == 7:
            self.image = transform.scale(image.load('h_b3.png'), (self.s_x, self.s_y)) 
        elif max_an - an == 4 and max_an == 7:
            self.image = transform.scale(image.load('h_b4_1.png'), (self.s_x, self.s_y)) 
        elif max_an - an == 5 and max_an == 7:
            self.image = transform.scale(image.load('h_b5_1.png'), (self.s_x, self.s_y)) 
        elif max_an - an == 6 and max_an == 7:
            self.image = transform.scale(image.load('h_b6_1.png'), (self.s_x, self.s_y)) 
        elif max_an - an == 1 and max_an == 6:
            self.image = transform.scale(image.load('h_b2_2.png'), (self.s_x, self.s_y)) 
        elif max_an - an == 2 and max_an == 6:
            self.image = transform.scale(image.load('h_b3_2.png'), (self.s_x, self.s_y)) 
        elif max_an - an == 3 and max_an == 6:
            self.image = transform.scale(image.load('h_b3.png'), (self.s_x, self.s_y)) 
        elif max_an - an == 4 and max_an == 6:
            self.image = transform.scale(image.load('h_b4_2.png'), (self.s_x, self.s_y)) 
        elif max_an - an == 5 and max_an == 6:
            self.image = transform.scale(image.load('h_b6_1.png'), (self.s_x, self.s_y)) 
        elif max_an - an == 1 and max_an == 5:
            self.image = transform.scale(image.load('h_b2.png'), (self.s_x, self.s_y)) 
        elif max_an - an == 2 and max_an == 5:
            self.image = transform.scale(image.load('h_b3.png'), (self.s_x, self.s_y)) 
        elif max_an - an == 3 and max_an == 5:
            self.image = transform.scale(image.load('h_b4.png'), (self.s_x, self.s_y)) 
        elif max_an - an == 4 and max_an == 5:
            self.image = transform.scale(image.load('h_b5.png'), (self.s_x, self.s_y)) 
        else:
            self.image = transform.scale(image.load('h_b6.png'), (self.s_x, self.s_y)) 
class SpecialBar(GameSprite):
    def __init__(self, image, speed, x, y, s_x, s_y):
        super().__init__(image, speed, x, y, s_x, s_y)
    def draw(self, hp):
        if hp == 3:
            self.image = transform.scale(image.load('shield_healthbar1.png'), (self.s_x, self.s_y)) 
        elif hp == 2:
            self.image = transform.scale(image.load('shield_healthbar2.png'), (self.s_x, self.s_y)) 
        elif hp == 1:
            self.image = transform.scale(image.load('shield_healthbar3.png'), (self.s_x, self.s_y)) 
        else:
            self.image = transform.scale(image.load('no_bar.png'), (self.s_x, self.s_y)) 
player = Player('ship1.png', 5, 300, 400, 75, 75, 'atc_cmn1')
ship_icon1 = GameSprite('ship2.png', 0, 265, 172, 150, 150)
ship_icon2 = GameSprite('ship3.png', 0, 265, 172, 150, 150)
health_bar = Bar('h_b1.png', 0, 200, 0, 250, 40)
shield_bar = SpecialBar('no_bar.png', 0, 200, 0, 250, 40)
box = Box('meteorit.png', 5, 300, 447, 75, 50)  
button1 = Button('play_button.png', 0, 302, 202, 96, 96, 'pressed_play_button.png')
button2 = Button('ships_button.png', 0, 302, 298, 48, 48, 'pressed_ships_button.png')
m1 = GameSprite('coin.png', 0, 455, 5, 23, 23)
m2 = GameSprite('coin.png', 0, 415, 173, 15, 15)
m3 = GameSprite('coin.png', 0, 415, 322, 15, 15)
m4 = GameSprite('coin.png', 0, 215, 168, 17, 17)
big_m = GameSprite('coin.png', 0, 265, 172, 150, 150)
big_d = GameSprite('diamond.png', 0, 265, 172, 150, 150)
ch1 = Button('choose1.png', 0, 100, 100, 96, 96, 'pressed_choose1.png')
ch2 = Button('choose2.png', 0, 100, 296, 96, 96, 'pressed_choose2.png')
ch3 = Button('choose3.png', 0, 246, 296, 96, 96, 'pressed_choose3.png')
buy1 = Button('choose2.png', 0, 344, 100, 96, 96, 'pressed_choose2.png')
buy2 = Button('choose3.png', 0, 344, 250, 96, 96, 'pressed_choose3.png')
button3 = Button('exit_button.png', 0, 632, 16, 48, 48, 'pressed_exit_button.png')
button3_1 = Button('exit_button.png', 0, 568, 16, 48, 48, 'pressed_exit_button.png')
button4 = Button('pause_button.png', 0, 632, 16, 48, 48, 'pressed_pause_button.png')
button5 = Button('shop_button.png', 0, 350, 298, 48, 48, 'pressed_shop_button.png')
box_button = Button('box_button.png', 0, 100, 100, 216, 96, 'pressed_box_button.png')
case_button = Button('case_button.png', 0, 100, 250, 216, 96, 'pressed_case_button.png')
d1 = GameSprite('diamond.png', 0, 300, 5, 25, 25)
d2 = GameSprite('diamond.png', 0, 455, 25, 25, 25)
d3 = GameSprite('diamond.png', 0, 215, 318, 19, 19)
present1 = GameSprite('bg3.png', 0, 630, 430, 50, 50)
present2 = GameSprite('diamon.png', 0, 630, 430, 50, 50)
present4 = GameSprite('bg2.png', 0, 630, 430, 50, 50)
mixer.init()
mixer.music.load('menu.ogg')
mixer.music.play(loops=-1)
py = True
background = transform.scale(image.load('space.gif'), (700, 520))
box_bg = transform.scale(image.load('bg.png'), (700, 500))
box_bg2 = transform.scale(image.load('bg2.png'), (700, 500))
box_bg3 = transform.scale(image.load('bg3.png'), (700, 500))

clock = time.Clock()
keys_pressed2 = key.get_pressed()
meteorits = sprite.Group()
coins = sprite.Group()
diamonds = sprite.Group()
shields = sprite.Group()
hearts = sprite.Group()
golden_hearts = sprite.Group()
diamond_hearts = sprite.Group()
strong_meteorits = sprite.Group()
very_strong_meteorits = sprite.Group()
for i in range(randint(4, 5)): 
    r_s = randint(40, 60) 
    randspeed = randint(1, 5)
    rand_x = randint(25, 625)
    rand_y = randint(-1000, -100)    
    met1 = Enemy('meteorit.png', randspeed, rand_x, rand_y, r_s, r_s)
    meteorits.add(met1)
for i in range(randint(3, 5)):
    rand_x = randint(25, 625)
    rand_y = randint(-5000, -2500)
    money = Money('coin.png', 5, rand_x, rand_y, 23, 23, 'money')
    coins.add(money)
for i in range(randint(1, 3)):
    rand_x = randint(25, 625)
    rand_y = randint(-50000, -25000)
    diamond = Money('diamond.png', 5, rand_x, rand_y, 25, 25, 'diamond')
    diamonds.add(diamond)
for i in range(randint(1, 3)):
    rand_x = randint(25, 625)
    rand_y = randint(-10000, -7500)
    shield_bonus = Money('shield.png', 5, rand_x, rand_y, 25, 25, 'shield')
    shields.add(shield_bonus)
for i in range(randint(2, 4)):
    rand_x = randint(25, 625)
    rand_y = randint(-10000, -7500)
    heart_bonus = Money('heart.png', 5, rand_x, rand_y, 25, 25, 'heart')
    hearts.add(heart_bonus)
for i in range(randint(2, 4)):
    rand_x = randint(25, 625)
    rand_y = randint(-12500, -10000)
    heart_bonus_gold = Money('golden_heart.png', 5, rand_x, rand_y, 25, 25, 'heart')
    golden_hearts.add(heart_bonus_gold)
for i in range(randint(1, 3)):
    rand_x = randint(25, 625)
    rand_y = randint(-50000, -25000)
    heart_bonus_diam = Money('diamond_heart.png', 5, rand_x, rand_y, 25, 25, 'heart')
    diamond_hearts.add(heart_bonus_diam)
# for i in range(randint(1, 2)):
#     rand_x = randint(25, 625)
#     rand_y = randint(-500, -100) 
#     randspeed = randint(1, 4)
#     met2 = StrongEnemy('прочный_метеорит.png', randspeed, rand_x, rand_y, 50, 50, 3)
#     strong_meteorits.add(met2)
# for i in range(randint(1, 2)):
#     rand_x = randint(25, 625)
#     rand_y = randint(-250, -100) 
#     randspeed = randint(1, 3)
#     met3 = Enemy('очень_прочный_метеорит.png', randspeed, rand_x, rand_y, 50, 50, 5)
#     very_strong_meteorits.add(met3)
bullets = sprite.Group()
while py: 
    if sc == 2:
        if not finish and not pause:
            s_score += 1
            box.reset()
            window.blit(background, (0, 0))
            text_score = f2.render('Score: ' + str(score), 1, (255, 255, 255))
            window.blit(text_score, ((0, 0)))
            text_score2 = f3.render('Best: ' + str(best_score), 1, (255, 255, 255))
            window.blit(text_score2, ((0, 25)))
            text_score3 = f4.render(str(game_money), 1, (255, 255, 255))
            window.blit(text_score3, ((485, 8)))
            text_score4 = f4.render(str(game_diams), 1, (255, 255, 255))
            window.blit(text_score4, ((485, 28)))
            player.reset()
            player.moving()
            player.red(ship_type)
            health_bar.reset()
            shield_bar.reset()
            if shield_health == 3:
                shield = Player('shield_full.png', 5, player.rect.x-20, player.rect.y-15, 115, 115, 'none')
                shield.reset()
                shield_bar.draw(3)
            elif shield_health == 2:
                shield = Player('damaged_shield2.png', 5, player.rect.x-20, player.rect.y-15, 115, 115, 'none')
                shield.reset()
                shield_bar.draw(2)
            elif shield_health == 1:
                shield = Player('damaged_shield4.png', 5, player.rect.x-20, player.rect.y-15, 115, 115, 'none')
                shield.reset() 
                shield_bar.draw(1)
            elif shield_health == 0:
                shield_act = False
                shield_bar.draw(0)
            box.moving()
            bullets.update()
            m1.reset()
            d2.reset()
            meteorits.draw(window)
            meteorits.update(r1, r2) 
            button4.reset()
            button4.draw()
            # new_record.reset()
            # strong_meteorits.draw(window)
            # strong_meteorits.update() 
            # very_strong_meteorits.draw(window)
            # very_strong_meteorits.update() 
            coins.draw(window)
            coins.update()
            diamonds.draw(window)
            diamonds.update()
            shields.draw(window)
            shields.update()
            bullets.draw(window)
            bullets.update()
            hearts.draw(window)
            hearts.update()
            golden_hearts.draw(window)
            golden_hearts.update()
            diamond_hearts.draw(window)
            diamond_hearts.update()
            window.blit(version, ((660, 480)))
            display.update()
            clock.tick(60)
            if s_score == 3600:
                s_score = 0
                r1 += 1
                r2 += 1
            if r1 > 5:
                r1 = 1
            if r2 > 10:
                r2 = 5
            if randint(1, 1000) == 58:
                if r1 > 1:
                    r1 -= 1
                    r2 -= 1
            keys_pressed3 = key.get_pressed()
            if ship_type == 'atc_cmn1':
                if cd == 30:
                    if keys_pressed3[K_SPACE]:
                        bullet = Bullet('bullet.png', 5,  player.rect.centerx-12, player.rect.top+15, 25, 25)
                        bullets.add(bullet)
                        cd = 0
                        mixer.init()
                        fire = mixer.Sound('FIRE.wav')
                        fire.play()                        
                else:
                    cd += 1
            elif ship_type == 'shd_cmn1':
                if cd == 30:
                    if keys_pressed3[K_SPACE]:
                        bullet = Bullet('bullet.png', 5,  player.rect.centerx-12, player.rect.top+15, 25, 25)
                        bullets.add(bullet)
                        cd = -15
                        mixer.init()
                        fire = mixer.Sound('FIRE.wav')
                        fire.play()                        
                else:
                    cd += 1
            else:
                if cd == 30:
                    if keys_pressed3[K_SPACE]:
                        bullet = Bullet('bullet.png', 5,  player.rect.centerx-12, player.rect.top+15, 25, 25)
                        bullets.add(bullet)
                        cd = -30
                        mixer.init()
                        fire = mixer.Sound('FIRE.wav')
                        fire.play()                        
                else:
                    cd += 1
            sp_l = sprite.groupcollide(meteorits, bullets, True, True)
            if sp_l:
                r_s = randint(40, 60)
                score += 1
                bullet.kill()
                randspeed = randint(r1, r2)
                rand_x = randint(25, 625)
                rand_y = randint(-1000, -100)    
                met1 = Enemy('meteorit.png', randspeed, rand_x, rand_y, r_s, r_s)
                meteorits.add(met1)
                if score > best_score:
                    best_score = score
                    b_score = True                   
            # sp_l2 = sprite.groupcollide(strong_meteorits, bullets, False, True)
            # if sp_l2:
            #     bullet.kill()
            #     shoot = 1
            #     strong_meteorits.update()               
            # sp_l3 = sprite.groupcollide(very_strong_meteorits, bullets, False, True)
            # if sp_l3:
            #     bullet.kill()
            #     damag = 1
            #     very_strong_meteorits.update()
            sprites_list = sprite.spritecollide(box, meteorits, True)
            if sprites_list:
                mixer.init()
                damage = mixer.Sound('damage.ogg')
                damage.play()
                r_s = randint(40, 60)
                if shield_act:
                    shield_health -= 1
                else:
                    player.damage()
                    player.reset()
                    display.update()
                    health -= 1
                    if ship_type == 'atc_cmn1':
                        health_bar.draw(health, 5)
                    elif ship_type == 'shd_cmn1':
                        health_bar.draw(health, 7)
                    else:
                        health_bar.draw(health, 6)
                randspeed = randint(1, 5)
                rand_x = randint(25, 625)
                rand_y = randint(-1000, -100)    
                met1 = Enemy('meteorit.png', randspeed, rand_x, rand_y, r_s, r_s)
                meteorits.add(met1)
                player.undamage()
                player.reset()
            sprites_list2 = sprite.spritecollide(box, coins, True)
            if sprites_list2:
                mixer.init()
                coin_sound = mixer.Sound('coin.ogg')
                coin_sound.play() 
                rand_x = randint(25, 625)
                rand_y = randint(-5000, -2500)
                money = Money('coin.png', 5, rand_x, rand_y, 23, 23, 'money')
                coins.add(money)
                game_money += 1
            sprites_list3 = sprite.spritecollide(box, diamonds, True)
            if sprites_list3:
                mixer.init()
                coin_sound = mixer.Sound('diamond.ogg')
                coin_sound.play() 
                rand_x = randint(25, 625)
                rand_y = randint(-50000, -25000)
                diamond = Money('diamond.png', 5, rand_x, rand_y, 25, 25, 'diamond')
                diamonds.add(diamond)
                game_diams += 1
            sprites_list4 = sprite.spritecollide(box, shields, True)
            if sprites_list4:
                mixer.init()
                coin_sound = mixer.Sound('shield_effect.ogg')
                mixer.music.set_volume(2)
                coin_sound.play() 
                rand_x = randint(25, 625)
                rand_y = randint(-10000, -7500)
                shield_bonus = Money('shield.png', 5, rand_x, rand_y, 25, 25, 'shield')
                shields.add(shield_bonus)
                shield_act = True
                shield_health = 3
            sprites_list5 = sprite.spritecollide(box, hearts, True)
            if sprites_list5:
                mixer.init()
                coin_sound = mixer.Sound('heart_effect1.ogg')
                mixer.music.set_volume(2)
                coin_sound.play() 
                rand_x = randint(25, 625)
                rand_y = randint(-10000, -7500)
                heart_bonus = Money('heart.png', 5, rand_x, rand_y, 25, 25, 'heart')
                hearts.add(heart_bonus)
                if max_health -  health == 0:
                    game_money += 10
                else:
                    health += 1
                    health_bar.draw(health, max_health)
                    health_bar.reset()
            sprites_list6 = sprite.spritecollide(box, golden_hearts, True)
            if sprites_list6:
                mixer.init()
                coin_sound = mixer.Sound('heart_effect2.ogg')
                mixer.music.set_volume(2)
                coin_sound.play() 
                rand_x = randint(25, 625)
                rand_y = randint(-12500, -10000)
                heart_bonus_gold = Money('golden_heart.png', 5, rand_x, rand_y, 25, 25, 'heart')
                golden_hearts.add(heart_bonus_gold)
                if max_health - health == 0:
                    game_money += 50
                elif max_health - health == 1:
                    game_money += 25
                    health += 1
                    health_bar.draw(health, max_health)
                    health_bar.reset()
                else:
                    health += 2
                    health_bar.draw(health, max_health)
                    health_bar.reset()
            sprites_list7 = sprite.spritecollide(box, diamond_hearts, True)
            if sprites_list7:
                mixer.init()
                coin_sound = mixer.Sound('heart_effect3.ogg')
                mixer.music.set_volume(2)
                coin_sound.play() 
                rand_x = randint(25, 625)
                rand_y = randint(-50000, -25000)
                heart_bonus_diam = Money('diamond_heart.png', 5, rand_x, rand_y, 25, 25, 'heart')
                diamond_hearts.add(heart_bonus_diam)
                if max_health - health == 0:
                    game_diams += 5
                elif max_health - health == 1:
                    game_money += 75
                    health += 1
                    health_bar.draw(health, max_health)
                    health_bar.reset()
                elif max_health - health == 2:
                    game_money += 50
                    health += 2
                    health_bar.draw(health, max_health)
                    health_bar.reset()
                else:
                    health += 3
                    health_bar.draw(health, max_health)
                    health_bar.reset()
            for h in event.get():
                if h.type == MOUSEBUTTONDOWN and h.button == 1:
                    s, d = h.pos
                    if button4.rect.collidepoint(s, d):
                        pause = True
                        button4 = Button('play_button.png', 0, 632, 16, 48, 48, 'pressed_play_button.png')
                if h.type == QUIT:
                    py = False
        if pause:
            button4.reset()
            button4.draw()
            button3_1.reset()
            button3_1.draw()
            display.update()
            for h in event.get():
                if h.type == MOUSEBUTTONDOWN and h.button == 1:
                    s, d = h.pos
                    if button4.rect.collidepoint(s, d):
                        pause = False
                        button4 = Button('pause_button.png', 0, 632, 16, 48, 48, 'pressed_pause_button.png')
                    if button3_1.rect.collidepoint(s, d):
                        sc = 1
                        mixer.music.stop()
                        mixer.music.load('menu.ogg')
                        mixer.music.play(loops=-1)
                        menu_money += int(best_score - last_best_score)
                        menu_money += game_money
                        menu_money += int(score / 5)
                        menu_diams += game_diams
                        last_best_score = best_score
                        pause = False
                        game_money = 0
                        game_diams = 0
                        score = 0
                        button4 = Button('pause_button.png', 0, 632, 16, 48, 48, 'pressed_pause_button.png')       
            if h.type == QUIT:
                py = False      
    if health == 0:
        s_score = 0
        r1 = 1
        r2 = 5
        finish = True
        mixer.music.stop()
        mixer.music.load('lose.ogg')
        mixer.music.play(loops=-1)
        window.blit(lose, (225, 200))
        text_score = f2.render('Счёт: ' + str(score), 1, (255, 0, 0))
        window.blit(text_score, ((280, 250)))
        bt = f3.render('Нажми q, чтобы продолжить ', 1, (255, 255, 255))
        window.blit(bt, ((250, 475)))
        player.death()
        player.reset()
        health_bar.draw(0, max_health)
        health_bar.reset()
        if b_score:
            window.blit(new_record, ((250, 170)))
        display.update()
        health = 1
        b_score = False
    if finish:
        s_score = 0
        r1 = 1
        r2 = 5
        keys_pressed = key.get_pressed() 
        if keys_pressed[K_q]:
            pause = False
            sc = 1
            finish = False
            menu_money += game_money
            menu_money += int(best_score - last_best_score)
            menu_money += int(score / 5)
            menu_diams += game_diams
            game_money = 0
            game_diams = 0
            score = 0
            mixer.music.stop()
            mixer.music.load('menu.ogg')
            mixer.music.play()
            last_best_score = best_score
            # sprites_list2 = sprite.spritecollide(hit_box, strong_meteorits, False)
            # if sprites_list2:
            #     finish = True
            #     mixer.music.stop()
            #     mixer.music.load('lose.ogg')
            #     mixer.music.play()
            #     window.blit(lose, (225, 200))
            #     text_score = f2.render('Счёт: ' + str(score), 1, (255, 0, 0))
            #     window.blit(text_score, ((280, 250)))
            #     player.death()
            #     player.reset()
            #     display.update()
            # sprites_list3 = sprite.spritecollide(hit_box, very_strong_meteorits, False)
            # if sprites_list3:
            #     finish = True
            #     mixer.music.stop()
            #     mixer.music.load('lose.ogg')
            #     mixer.music.play()
            #     window.blit(lose, (225, 200))
            #     text_score = f2.render('Счёт: ' + str(score), 1, (255, 0, 0))
            #     window.blit(text_score, ((280, 250)))
            #     player.death()
            #     player.reset()
            #     display.update()
    if sc == 3:
        window.blit(background, (0, 0))
        ch1.reset()
        ch1.draw()
        ch2.reset()
        ch2.draw()
        ch3.reset()
        ch3.draw()
        unlocked = f2.render('Открыто:', 1, (255, 255, 255))
        window.blit(unlocked, ((280, 50)))
        locked = f2.render('Закрыто:', 1, (255, 255, 255))
        window.blit(locked, ((280, 250)))
        button3.reset()
        button3.draw()
        window.blit(version, ((660, 480)))
        display.update()
        if ship_shield_common1:
            ch2 = Button('choose2.png', 0, 246, 100, 96, 96, 'pressed_choose2.png')
            ch3 = Button('choose3.png', 0, 100, 296, 96, 96, 'pressed_choose3.png')
            ch2.reset()
            ch2.draw()
            ch3.draw()
            ch3.reset()
        if ship_help_common1 and not ship_shield_common1:
            ch3 = Button('choose3.png', 0, 246, 100, 96, 96, 'pressed_choose3.png')
            ch2.reset()
            ch2.draw()
            ch3.draw()
            ch3.reset()
        if ship_help_common1 and ship_shield_common1:
            ch2 = Button('choose2.png', 0, 246, 100, 96, 96, 'pressed_choose2.png')
            ch3 = Button('choose3.png', 0, 392, 100, 96, 96, 'pressed_choose3.png')
            ch2.reset()
            ch2.draw()
            ch3.draw()
            ch3.reset()
        for a in event.get():
            if a.type == MOUSEBUTTONDOWN and a.button == 1:
                s, d = a.pos
                if button3.rect.collidepoint(s, d):
                    sc = 1
                if ch2.rect.collidepoint(s, d) and ship_shield_common1:
                    ship_type = 'shd_cmn1'
                    health = 7
                    max_health = 7
                if ch3.rect.collidepoint(s, d) and ship_help_common1:
                    ship_type = 'hlp_cmn1'
                    health = 6
                    max_health = 6
                if ch1.rect.collidepoint(s, d):
                    ship_type = 'atc_cmn1'
                    health = 1
                    max_health = 5
            if a.type == QUIT:
                py = False
    if sc == 4:
        window.blit(background, (0, 0))
        m1.reset()
        d1.reset()
        window.blit(mon, ((480, 8)))
        window.blit(diam, ((330, 8)))
        box_button.draw()
        box_button.reset()
        case_button.draw()
        case_button.reset()
        window.blit(cost, ((185, 320)))
        window.blit(cost, ((185, 170)))
        d3.reset()
        m4.reset()
        if not ship_shield_common1:
            ct = f3.render('10000', 1, (0, 0, 0))
            buy1.reset()
            buy1.draw()
            m2.reset()
            window.blit(ct, ((364, 173))) 
        if not ship_help_common1:
            ct1 = f3.render('5000', 1, (0, 0, 0))
            buy2.reset()
            buy2.draw()  
            m3.reset()  
            window.blit(ct1, ((374, 323)))   
        button3.draw()
        button3.reset()
        window.blit(version, ((660, 480)))
        display.update()
        for a in event.get():
            if a.type == QUIT:
                    py = False
            if a.type == MOUSEBUTTONDOWN and a.button == 1:
                s, d = a.pos
                if buy1.rect.collidepoint(s, d):
                    if menu_money > 9999 and ship_shield_common1 == False:
                        menu_money -= 10000
                        ship_shield_common1 = True
                        mon = f4.render(str(menu_money) , 1, (255, 255, 255))
                        diam = f4.render(str(menu_diams) , 1, (255, 255, 255))
                if buy2.rect.collidepoint(s, d):
                    if menu_money > 4999 and ship_help_common1 == False:
                        menu_money -= 5000
                        ship_help_common1 = True
                        mon = f4.render(str(menu_money) , 1, (255, 255, 255))
                        diam = f4.render(str(menu_diams) , 1, (255, 255, 255))  
                if box_button.rect.collidepoint(s, d):
                    if menu_money > 99:
                        menu_money -= 100
                        sc = 5
                        s_money = randint(25, 150)
                        if not ship_shield_common1 or not ship_help_common1:
                            new_ship = randint(1, 1000)
                        else:
                            new_ship = 1
                        if new_ship != 2:
                            more_diamonds = randint(1, 250)
                if case_button.rect.collidepoint(s, d):
                    if menu_diams > 99:
                        menu_diams -= 100
                        sc = 8
                        s_money = randint(150, 275)
                        if not ship_shield_common1 or not ship_help_common1:
                            new_ship = randint(1, 250)
                        else:
                            new_ship = 1
                        if new_ship != 250:
                            more_diamonds = randint(1, 5)
                if button3.rect.collidepoint(s, d):
                    sc = 1
                    mixer.music.stop()
                    mixer.music.load('menu.ogg')
                    mixer.music.play(loops=-1)
    if sc == 5:
        money_at_box = f.render('x'+str(s_money), 1, (255, 255, 255))
        window.blit(box_bg, (0, 0))
        window.blit(money_at_box, (295, 350))
        big_m.reset()
        if new_ship == 1000:
            present4.reset()
            window.blit(present3, (645, 440))
        if more_diamonds == 250:
            present2.reset()
            window.blit(present3, (645, 440))
        display.update()
        for a in event.get():
            if a.type == MOUSEBUTTONDOWN:
                if not ship_help_common1 or not ship_shield_common1:
                    if new_ship == 1000:
                        sc = 6
                        window.blit(box_bg3, (0, 0))
                        # new_ship = 1
                if more_diamonds == 250:
                    sc = 7
                    s_diamonds = randint(1, 5)
                if new_ship != 1000 and more_diamonds != 250:
                    menu_money += s_money
                    sc = 4
                    mon = f4.render(str(menu_money) , 1, (255, 255, 255))
            if a.type == QUIT:
                py = False
    if sc == 6:
        window.blit(box_bg3, (0, 0))
        if n == b and not ship_shield_common1:
            ship_icon1.reset()
        else:
            ship_icon2.reset()
        display.update()
        for a in event.get():
            if a.type == MOUSEBUTTONDOWN:
                if n == b and not ship_shield_common1:
                    ship_shield_common1 = True
                    b = 0
                    ship_icon1.reset()
                else:
                    ship_help_common1 = True
                    n = 1
                    ship_icon2.reset()
                menu_money += s_money
                sc = 4
                mon = f4.render(str(menu_money) , 1, (255, 255, 255))
            if a.type == QUIT:
                py = False
    if sc == 7:
        window.blit(box_bg2, (0, 0))
        diams_at_box = f.render('x'+(str(s_diamonds), 1, (255, 255, 255)))
        window.blit(diams_at_box, (300, 350))
        big_d.reset()
        display.update()
        display.update()
        for a in event.get():
            if a.type == MOUSEBUTTONDOWN:
                big_d.reset()
                menu_money += s_money
                menu_diams += s_diamonds
                sc = 4
                mon = f4.render(str(menu_money) , 1, (255, 255, 255))
                diam = f4.render(str(menu_diams) , 1, (255, 255, 255))
            if a.type == QUIT:
                py = False
    if sc == 8:
        money_at_box = f.render('x'+str(s_money), 1, (255, 255, 255))
        window.blit(box_bg, (0, 0))
        window.blit(money_at_box, (295, 350))
        big_m.reset()
        if new_ship == 250:
            present1.reset()
            window.blit(present3, (645, 440))
        if more_diamonds == 5:
            present2.reset()
            window.blit(present3, (645, 440))
        display.update()
        for a in event.get():
            if a.type == MOUSEBUTTONDOWN:
                if not ship_help_common1 or not ship_shield_common1:
                    if new_ship == 250:
                        sc = 9
                        window.blit(box_bg3, (0, 0))
                        # new_ship = 1
                if more_diamonds == 5:
                    sc = 10
                    s_diamonds = randint(5, 25)
                if new_ship != 250 and more_diamonds != 5:
                    menu_money += s_money
                    sc = 4
                    mon = f4.render(str(menu_money) , 1, (255, 255, 255))
                    diam = f4.render(str(menu_diams) , 1, (255, 255, 255))
            if a.type == QUIT:
                py = False
    if sc == 9:
        window.blit(box_bg3, (0, 0))
        if n == b and not ship_shield_common1:
            ship_icon1.reset()
        else:
            ship_icon2.reset()
        display.update()
        for a in event.get():
            if a.type == MOUSEBUTTONDOWN:
                if n == b and not ship_shield_common1:
                    ship_shield_common1 = True
                    b = 0
                else:
                    ship_help_common1 = True
                    n = 1
                menu_money += s_money
                sc = 4
                diam = f4.render(str(menu_diams) , 1, (255, 255, 255))
                mon = f4.render(str(menu_money) , 1, (255, 255, 255))
            if a.type == QUIT:
                py = False
    if sc == 10:
        window.blit(box_bg2, (0, 0))
        diams_at_box = f.render('x'+str(s_diamonds), 1, (255, 255, 255))
        window.blit(diams_at_box, (300, 350))
        big_d.reset()
        display.update()
        display.update()
        for a in event.get():
            if a.type == MOUSEBUTTONDOWN:
                big_d.reset()
                menu_money += s_money
                menu_diams += s_diamonds
                sc = 4
                mon = f4.render(str(menu_money) , 1, (255, 255, 255))
                diam = f4.render(str(menu_diams) , 1, (255, 255, 255))
            if a.type == QUIT:
                py = False
    if sc == 1:
        s_score = 0
        r1 = 1
        r2 = 5
        button1.draw()
        button2.draw()
        button5.draw()
        mon = f4.render(str(menu_money) , 1, (255, 255, 255))
        diam = f4.render(str(menu_diams) , 1, (255, 255, 255))
        health = max_health
        window.blit(background, (0, 0))
        button1.reset()
        button2.reset()
        button5.reset()
        m1.reset()
        d1.reset()
        window.blit(mon, ((480, 8)))
        window.blit(diam, ((330, 8)))
        window.blit(version, ((660, 480)))
        display.update()
        clock.tick(60)
        for a in event.get():
            if a.type == MOUSEBUTTONDOWN and a.button == 1:
                s, d = a.pos
                if button1.rect.collidepoint(s, d):
                    player.undamage()
                    player.restart()
                    box.restart()
                    sc = 2
                    shield_act = False 
                    shield_health = 0
                    mixer.init()
                    mixer.music.load('space.ogg')
                    mixer.music.play(loops=-1)
                    health_bar.draw(health, max_health)
                if button2.rect.collidepoint(s, d):
                    sc = 3
                if button5.rect.collidepoint(s, d):
                    sc = 4
                    mixer.music.stop()
                    mixer.music.load('shop.ogg')
                    mixer.music.play(loops=-1)
            if a.type == QUIT:
                py = False
    for x in event.get():
            if x.type == QUIT:
                py = False  