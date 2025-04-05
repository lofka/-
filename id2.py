from pygame import *
from random import *
import time
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,size_x,size_y,speed):
        sprite.Sprite.__init__(self)
        self.im=player_image
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed=speed
        self.speed_x=1#
        self.speed_y=1#
        self.pos_x1=0
        self.pos_x2=0
        self.pos_y1=0
        self.pos_y2=0
        self.size_x=size_x
        self.size_y=size_y
        
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))
class player(GameSprite):
    def update(self):
            keys_pressed = key.get_pressed()                 
            self.dvig=False
            if keys_pressed[K_RIGHT] and self.rect.x <self.pos_x1:#
                    self.rect.x += self.speed        
            if keys_pressed[K_LEFT] and self.rect.x >self.pos_x2:#
                    self.rect.x -= self.speed               
            if keys_pressed[K_UP] and self.rect.y >self.pos_y1:#
                    self.rect.y-= self.speed 
            if keys_pressed[K_DOWN] and self.rect.y <self.pos_y2:#
                    self.rect.y += self.speed 
    def cvtyf(self,skpsok,nomer):#
        self.rect.x=skpsok[nomer][1]
        self.rect.y=skpsok[nomer][2]
        self.pos_x1=skpsok[nomer][3]
        self.pos_x2=skpsok[nomer][4]
        self.pos_y1=skpsok[nomer][5]
        self.pos_y2=skpsok[nomer][6]
class enemu(GameSprite):
    def update(self,skpsok,nomer):
        self.rect.x+=self.speed *self.speed_x
        self.rect.y+=self.speed *self.speed_y
        if  self.rect.x>=self.pos_x1 or self.rect.x<=self.pos_x2:
            self.speed_x=self.speed_x*-1
        if  self.rect.y>=self.pos_y2 or self.rect.y<=self.pos_y1:
            self.speed_y=self.speed_y*-1

    def cvtyf(self,skpsok,nomer):
        #self.rect.x=skpsok[nomer][1]
        #self.rect.y=skpsok[nomer][2]
        self.pos_x1=skpsok[nomer][3]
        self.pos_x2=skpsok[nomer][4]
        self.pos_y1=skpsok[nomer][5]
        self.pos_y2=skpsok[nomer][6]        
        self.rect.x=randint( self.pos_x2+self.size_x,self.pos_x1-self.size_x)
        self.rect.x=randint( self.pos_y1+2*self.size_y, self.pos_y2-self.size_y)
class prsledovatel(GameSprite):
    def update(self,ingok):  
        if  self.rect.x>=ingok.rect.x:
            self.rect.x-=self.speed
        if  self.rect.x<=ingok.rect.x:
            self.rect.x+=self.speed

        if  self.rect.y>=ingok.rect.y:
            self.rect.y-=self.speed
        if  self.rect.y<=ingok.rect.y:
            self.rect.y+=self.speed
win_width = 500
win_height = 500
kof=4# ДЛЯ УДОБСТВА
display.set_caption('Вопрос-Ответ')
konmate=[[1,250,250,370,30,70,420],######
          [2,250,250,370,120,200,310],
           [3,250,250,310,45,35,375] ]###
window  = display.set_mode((win_width, win_height))
w = GameSprite('forlorn_mausoleum_of_dawn_arrow.png',-win_width*kof//2,-win_height*kof//2+200, win_width*kof, win_height*kof, 0)
gamer = player('7.png',250,250, 50, 50, 5)
enemutt = enemu('7.png',350,400, 25, 25, 1)
prsl = prsledovatel('7.png',350,400, 25, 25, 1)
gamer.cvtyf(konmate,0)
enemutt.cvtyf(konmate,0)

karta=[[1,-win_width*kof//2,-win_height*kof//2+200],
        [2,-600,-1000],
        [3,-600,-700]]
u=1
back = (80,80, 80)
run = True
while run:
    print(gamer.rect.x,gamer.rect.y,u, w.rect.x, w.rect.y)
    window.fill(back)    
    w.reset()
    if u==1:        
        if gamer.rect.y>400 and  gamer.rect.y<500 and gamer.rect.x<=30:   #из 1 в 2   
           u=2
           #self.rect.x=skpsok[nomer][1]
           #self.rect.y=skpsok[nomer][2]
           gamer.cvtyf(konmate,u-1)
           enemutt.cvtyf(konmate,u-1)
           w.rect.x=karta[u-1][1]
           w.rect.y=karta[u-1][2]
           #w.rect.x+=400
           #w.rect.y-=200
        if gamer.rect.y>90 and  gamer.rect.y<130 and gamer.rect.x<=30:
            u=3
            gamer.cvtyf(konmate,u-1)
            enemutt.cvtyf(konmate,u-1)
            w.rect.x=karta[u-1][1]
            w.rect.y=karta[u-1][2]
            #w.rect.x+=400
            #w.rect.y+=100
    if u==2:
        if gamer.rect.y>210 and  gamer.rect.y<250 and gamer.rect.x>=370:  #из 2 в 1 
           u=1
           gamer.cvtyf(konmate,u-1)
           enemutt.cvtyf(konmate,u-1)
           w.rect.x=karta[u-1][1]
           w.rect.y=karta[u-1][2]
           #w.rect.x-=400
           #w.rect.y+=200
    if u==2:
        if gamer.rect.x>200 and  gamer.rect.x<240 and gamer.rect.y<=200:  #из 2 в 3 
           u=3
           gamer.cvtyf(konmate,u-1)
           enemutt.cvtyf(konmate,u-1)
           w.rect.x=karta[u-1][1]
           w.rect.y=karta[u-1][2]
           #w.rect.x+=0
           #w.rect.y+=+300
    if u==3:
        prsl.reset()
        prsl.update(gamer)
        if gamer.rect.y>180 and  gamer.rect.y<240 and gamer.rect.x>=310:  #из 2 в 3 
           u=1
           gamer.cvtyf(konmate,u-1)
           enemutt.cvtyf(konmate,u-1)
           w.rect.x=karta[u-1][1]
           w.rect.y=karta[u-1][2]

           #w.rect.x+=-400
           #w.rect.y+=-100
    for e in event.get():
        if e.type == QUIT:
            run = False     

    gamer.update() 
    gamer.reset() 
    enemutt.reset() 
    enemutt.update(konmate,u-1)

 


    display.update()
    