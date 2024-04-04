from pygame import *
from random import *
mixer.init()
window = display.set_mode((700, 500))
display.set_caption("шутер")
galaxy = transform.scale(image.load("1703280758129631078.jpg"), (700, 500))
window.blit(galaxy,(0, 0))  
class GameSprite(sprite.Sprite):
    def __init__(self, pimage, speed, x, y,w=110, h=150):
        super().__init__()
        self.image = transform.scale(image.load(pimage), (w, h))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y)) 

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT]:
            self.rect.x -= self.speed
        if keys[K_RIGHT]:
            self.rect.x += self.speed    
    def fire(self):
        bullet = Bullet('bullet.png',-15, self.rect.centerx, self.rect.top,  20, 15)
        bullets.add(bullet)
class E(GameSprite):
    def m(self):
        pass

class Enemy(E):
    def  update(self):
        self.rect.y += self.speed     
        if self.rect.y > 500:
            self.rect.x = randint(80, 700)
            self.rect.y = -100
            global miss
            miss = miss + 1
class Bullet(GameSprite):
   def update(self):
       self.rect.y += self.speed
       if self.rect.y < 0:
           self.kill()

clock = time.Clock() 
FPS = 60
speed = 3
mixer.music.load('space.ogg')
mixer.music.play()
fire = mixer.Sound('fire.ogg')
run = True
igrok = Player('1200px-AK-47.png', 3, 310, 400)
terrors = sprite.Group()
bullets = sprite.Group()

FPS = 60
miss = 0
kill = 0

for i in range(5):
    terrors.add(Enemy('Terrorist-PNG-Picture.png', randint(1, 2), randint(0, 600), -100))


font.init()
font1 = font.SysFont('Arial', 36)
end = False
font = font.SysFont('Arial', 55)
win = font.render("победа победа время до обеда", True, (255, 83, 193))
lose = font.render("тебя убили ха-ха", True, (201, 92, 63))
while run == True:
    for e in event.get():
        if e.type == QUIT:
            run = False

        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                fire.play()
                igrok.fire()
    if not end:     
    
        window.blit(galaxy,(0,0))
        igrok.reset()
        igrok.update()
        terrors.draw(window)
        terrors.update()
        bullets.update()
        bullets.draw(window)
        if  kill > 19:
            end = True
            window.blit(win ,(50, 150))
        if miss > 4:
            end = True
            window.blit(lose, (170, 190))

        sprite_list = sprite.groupcollide(terrors, bullets, True, True)
        for pon in sprite_list:
            kill += 1
            terrors.add(Enemy('Terrorist-PNG-Picture.png', randint(1, 2), randint(0, 600), -100))
        text_lose = font1.render("Пропущено:  " + str(miss), 1, (255, 255, 255))
        window.blit(text_lose, (10, 20))
        text_lose = font1.render("убито:  " + str(kill), 1, (255, 255, 255))
        window.blit(text_lose, (10, 60))
        clock.tick(FPS)
        display.update()
    else:
        miss, kill = 0, 0
        end = False 
        time.delay(5000)