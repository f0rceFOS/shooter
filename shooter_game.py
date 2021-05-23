from pygame import *
from random import randint

class Player(sprite.Sprite):
    def __init__ (self,x,y,filename,speed = 3):
        self.image = image.load(filename) 
        self.image = transform.scale(self.image,(100,100))
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def update(self):
        keys = key.get_pressed()
        if keys[K_a]:
            self.rect.x -= self.speed
        if keys[K_d]:
            self.rect.x += self.speed
        

        if self.rect.x < 1:
            self.rect.x += 5
        if self.rect.x > 600:
            self.rect.x -= 5

        self.reset()
    def reset(self):
        win.blit(self.image, (self.rect.x,self.rect.y))
    def fire(self):
        if len(bullets) < 50:
            b = Bullet(x = self.rect.center[0] - 15, y = self.rect.y, filename = 'bullet.png')
            bullets.add(b)

class Boss(sprite.Sprite):
    def __init__ (self,x,y,filename,speed = 1):
        super().__init__()
        self.image = image.load(filename) 
        self.image = transform.scale(self.image,(200,200))
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def update(self):
        self.rect.y += self.speed
        if sprite.collide_rect(self,rocket):
            rocket.HP -= 2
        
        self.reset()
    def reset(self):
        win.blit(self.image, (self.rect.x,self.rect.y))
    
class Asteroid(sprite.Sprite):
    def __init__ (self,x,y,filename,speed = randint(1,2)):
        super().__init__()
        self.image = image.load(filename) 
        self.image = transform.scale(self.image,(100,100))
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def update(self):
        self.rect.x += self.speed
        if self.rect.x > 720:
            self.rect.x = randint(-400,-10)
            self.rect.y = randint(10,690)
        self.reset()
    def reset(self):
        win.blit(self.image, (self.rect.x,self.rect.y))

class Enemy(sprite.Sprite):
    def __init__ (self,x,y,filename,speed = 2):
        super().__init__()
        self.image = image.load(filename) 
        self.image = transform.scale(self.image,(100,100))
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 450:
            rocket.HP -= 1
            self.rect.x = randint(10,500)
            self.rect.y = randint(-400,-10)
        if sprite.collide_rect(self,rocket):
            rocket.HP -= 1
            NLO.remove(self)

        if rocket.HP < 1:
            win.blit(loose,(250,250))
            global finish
            finish = 0
        self.reset()
    def reset(self):
        win.blit(self.image, (self.rect.x,self.rect.y))
    
new = image.load('ayfer.jpg')
new = transform.scale(new,(100,100))
#рестарт и идея
class Bullet(sprite.Sprite):
    def __init__ (self,x,y,filename,speed = 5):
        super().__init__()
        self.image = image.load(filename) 
        self.image = transform.scale(self.image,(30,30))
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            bullets.remove(self)
        if sprite.collide_rect(self,boss):
            bullets.remove(self)
            boss.HP -= 1
            print(boss.HP)
        if boss.HP < 1:
            global finish
            gg = image.load('rockata.jpg')
            gg = transform.scale(gg, resolution) 
            win.blit(gg,(0,0))
            win.blit(pobeda,(200,0))
            VRAG.empty()
        self.reset()

    def reset(self):
        win.blit(self.image, (self.rect.x,self.rect.y))


class Button:
    def __init__(self,x,y,w,h,text,color=(128,128,128),text_color=(0,0,0)):
        self.rect = Rect(x,y,w,h)
        self.color = color
        self.text = text
        self.text_color = text_color
        self.font = font.SysFont('Arial', 40)
        self.text_pic = self.font.render(text,1,text_color)
    def draw(self):
        draw.rect(win, self.color, self.rect)
        win.blit(self.text_pic,(self.rect.x, self.rect.y)) #+- 20
    def check_click(self,pos):
        return self.rect.collidepoint(pos)
font.init()

shrift = font.Font(None,70)
rocket = Player(x = 300,y = 450,filename = 'rocket.png',speed = 5)
vrag1 = Enemy(x = randint(10,500), y = randint(-400,-10), filename = 'ufo.png')
vrag2 = Enemy(x = randint(10,500), y = randint(-400,-10), filename = 'ufo.png')
vrag3 = Enemy(x = randint(10,500), y = randint(-400,-10), filename = 'ufo.png')
vrag4 = Enemy(x = randint(10,500), y = randint(-400,-10), filename = 'ufo.png')
vrag5 = Enemy(x = randint(10,500), y = randint(-400,-10), filename = 'ufo.png')

aster1 = Asteroid(x = randint(0,1), y = randint(10,690), filename = 'asteroid.png')

boss = Boss(x = 230, y = -212, filename = 'ufo.png')
bat_start = Button(x=600,y=500,w=100,h=50,text = 'ПАУЗА')
batbat = Button(x=600,y=500,w=100,h=50,text = 'СТАРТ')
bat2 = Button(x=0,y=500,w=100,h=50,text = 'Reset')
b_star = Button(x = 250,y=400,w=200,h=50,text = 'Начать игру')
#сделать жизни
boss.HP = 10
rocket.HP = 2
VRAG = sprite.Group()
NLO = sprite.Group()
VRAG.add(boss)
NLO.add(vrag1, vrag2, vrag3, vrag4, vrag5)
bullets = sprite.Group()

ASTER = sprite.Group()
ASTER.add(aster1)

loose = shrift.render('ТЫ ПРОИГРАЛ!', True, (100,255,255))
pobeda = shrift.render('ТЫ ВЫЙГРАЛ!', True, (250,0,0))
payse = shrift.render('ПАУЗА', True, (0,0,0))
start = shrift.render('Нажми что-бы начать игру', True,(10,250,50))



resolution = [700,550]

win = display.set_mode(resolution)
display.set_caption('Стрелялки')

a = 0

bg = image.load('galaxy.jpg')
bg = transform.scale(bg, resolution)

timer = time.Clock()
FPS = 60

mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
p = False
finish = True
lose = False
showbss = 0 

while True:
    if finish == True:
        fon = image.load('ff.jpg')
        fon = transform.scale(fon, resolution)
        win.blit(fon,(0,0))
        b_star.draw()
        win.blit(start,(25,250))
        ASTER.update()

    if finish == False:
        win.blit(bg, (0,0))
        if p:
            batbat.draw()
        if not p:
            bat_start.draw()
        HP = shrift.render('HP: ' + str(rocket.HP), True, (100,255,255))
        win.blit(HP,(0,500))
        kill = shrift.render('ТЫ УБИЛ:' + str(a) + '/20', True, (100,255,0))
        win.blit(kill,(0,0))
        rocket.update()
        if p == False:
            
            if showbss:
                VRAG.update()
            else:
                NLO.update()
            bullets.update()
            stalker = sprite.groupcollide(NLO, bullets, False, True)
            if rocket.HP < 1:
                lose = True
            for ch in stalker:
                a += 1
                if a > 18:
                    showbss = 1
                    NLO.empty()
                ch.rect.y = randint(-400,-10)
                ch.rect.x = randint(10,500)

     
    if lose == True:
        win.fill((0,0,0))
        ay = image.load('ryins.jpg')
        ay = transform.scale(ay, resolution) 
        win.blit(ay,(0,0))
        win.blit(loose,(200,0))
        bat2.draw()
    if a > 19:
        
        finish = 0
        win.fill((0,0,0))
        gg = image.load('rockata.jpg')
        gg = transform.scale(gg, resolution) 
        win.blit(gg,(0,0))
        win.blit(pobeda,(200,0))
    for e in event.get():
        if e.type == QUIT:
            exit()
        if e.type == MOUSEBUTTONDOWN:
            if bat_start.check_click(e.pos):
                if p:
                    p = False
                    
                else:
                    p = True
                   
            
                   
            if bat2.check_click(e.pos):
                finish = False
                lose = False
                a = 0 
                rocket.HP = 2
                vrag1 = Enemy(x = randint(10,500), y = randint(-400,-10), filename = 'ufo.png')
                vrag2 = Enemy(x = randint(10,500), y = randint(-400,-10), filename = 'ufo.png')
                vrag3 = Enemy(x = randint(10,500), y = randint(-400,-10), filename = 'ufo.png')
                vrag4 = Enemy(x = randint(10,500), y = randint(-400,-10), filename = 'ufo.png')
                vrag5 = Enemy(x = randint(10,500), y = randint(-400,-10), filename = 'ufo.png')
                NLO = sprite.Group()
                NLO.add(vrag1, vrag2, vrag3, vrag4, vrag5)
            if b_star.check_click(e.pos):
                finish = False
        if e.type == KEYUP:
            if e.key == K_SPACE:
                rocket.fire()

    timer.tick(FPS)
    display.update()
   


   

