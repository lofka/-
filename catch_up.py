from pygame import *
from random import *
import time
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,size_x,size_y,speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed=speed
        self.speed_x=speed
        self.speed_y=speed
        self.pos=0
        self.dvig=True
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))
class player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if  True in keys_pressed:
            #print(keys_pressed)            
            self.dvig=False
            if keys_pressed[K_RIGHT]:
                    self.rect.x += win_width//20              
            if keys_pressed[K_LEFT]:
                    self.rect.x -= win_width//20                
            if keys_pressed[K_UP]:
                    self.rect.y -= win_height//20
            if keys_pressed[K_DOWN]:
                    self.rect.y += win_height//20
    def prov(self,side):
         if sprite.spritecollide(self, barriers1, False):             
            if side=='K_RIGHT':
                    self.rect.x += win_width//20
                    if sprite.spritecollide(self, barriers3, False): 
                        self.rect.x -= win_width//20             
            if side=='K_LEFT':
                    self.rect.x -= win_width//20
                    if sprite.spritecollide(self, barriers3, False): 
                        self.rect.x -= win_width//20                
            if side=='K_UP':
                    self.rect.y -= win_height//20
                    if sprite.spritecollide(self, barriers3, False): 
                        self.rect.x -= win_width//20
            if side=='K_DOWN':
                    if sprite.spritecollide(self, barriers3, False): 
                        self.rect.x -= win_width//20
                    self.rect.y += win_height//20
 
win_width = 900
win_height = 600
display.set_caption('Вопрос-Ответ')
window  = display.set_mode((win_width, win_height))
barriers1=sprite.Group()
barriers2=sprite.Group()
barriers3=sprite.Group()
w = player('7.png',win_width//20*5, win_height//20*5, 20, 20, 30)
all1=list()
kall=list()
for i in range(win_height//20):   
    for j in range(win_width//20):
        k=randint(1,3)
        all1.append(k)
        if k==1:
            b = GameSprite('background.png',win_width//20*i, win_height//20*j, 20, 20, 1)
            b.pos=1
            barriers1.add(b)
        elif  k==2:
            b = GameSprite('sprite1.png',win_width//20*i, win_height//20*j, 20, 20, 1)
            b.pos=2
            barriers2.add(b)
        elif  k==3:
            b = GameSprite('sprite2.png',win_width//20*i, win_height//20*j, 20, 20, 1)
            b.pos=3
            barriers3.add(b) 
    kall.append(all1)

font.init()
back = (80,80, 80)
font = font.SysFont('Arial', 100)
i=0
run = True

start_time=time.time()
cur_time=time.time()
FPS = 60

while run:

    #print(vrema)
    text1 = font.render(str(str(round(cur_time-start_time,2))+ " "+" {}").format(w.dvig), True, (255, 255, 255))   
    #i+=1
    cur_time=time.time()
    for e in event.get():
        if e.type == QUIT:
            run = False     
    window.fill(back)
    window.blit(text1,(0,0))
    barriers1.draw(window)
    barriers3.draw(window)
    barriers2.draw(window)
    w.reset()
    if cur_time-start_time>3 and w.dvig:
        w.update()
    if cur_time-start_time>4:
        w.dvig=True
        start_time=cur_time
        cur_time=time.time()


    display.update()
    