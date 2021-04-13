import pygame as py
import random
from pygame import mixer

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
black = (0,0,0)
white = (255,255,255)

py.init()
py.mixer.init()

width = 800
height = 600
fps = 100
exit_game = False
game_over = False
snake_x = 50
snake_y = 50
snake_size = 20
vel_x = 0
vel_y = 0
speed = 10
food_x = random.randint(0,width-10)
food_y = random.randint(0,height-10)
food_size = 20
score = 0
snake_list = []
snake_length = 1







win = py.display.set_mode((width,height))
py.display.set_caption("Snake Game")
clock = py.time.Clock()


background1 = py.image.load('back.png')

def mytext(text,color,x,y):
    font = py.font.SysFont('arial',25)
    screentext = font.render(text,True,color)
    win.blit(screentext,(x,y))

def plot_snake(window,color,snake_list,snake_size):
    c=1
    for x,y in snake_list:
        if c==len(snake_list):
            py.draw.rect(window,color,(x,y,snake_size,snake_size))
        else:
            py.draw.rect(window,(random.randint(0,255),random.randint(0,255),random.randint(0,255)),(x,y,snake_size,snake_size))
        c=c+1
mixer.music.load("background.wav")
cc=25
add=1
kk=cc
while not exit_game:
    win.blit(background1, (0, 0))
    
    
    
    if game_over:
        win.fill((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
        kk=kk+add
        font = py.font.SysFont('arial',kk)
        if kk<=25:
            add=add*(-1)
        if kk>=80:
            add=add*(-1)
            
        screentext = font.render("!! GAME OVER !!",True,black)
        win.blit(screentext,(270-kk,280))
        clock.tick(fps-10)
        
        py.display.update()
        
    else :
        
        
        
        win.blit(background1, (0, 0))
        for event in py.event.get():
            if event.type == py.QUIT:
                exit_game = True

            if event.type == py.KEYDOWN:
                if event.key == py.K_UP:
                    vel_y = -speed
                    vel_x = 0
                if event.key == py.K_DOWN:
                    vel_y = speed
                    vel_x = 0
                if event.key == py.K_LEFT:
                    vel_y = 0
                    vel_x = -speed
                if event.key == py.K_RIGHT:
                    vel_y = 0
                    vel_x = speed
        if abs(snake_x-food_x)<8 and abs(snake_y-food_y)<8:
            food_x = random.randint(0,width)
            food_y = random.randint(0,height)
            score = score+10
            snake_length = snake_length+5
            explosionSound = mixer.Sound("laser.wav")
            explosionSound.play()
            
        head = []
        head.append(snake_x)
        head.append(snake_y)
        snake_list.append(head)
        #print(len(snake_list))

        if len(snake_list) > snake_length:
            del snake_list[0]

        if head in snake_list[:-1]:
            game_over = True
            print("Game_over")
            game_over_Sound = mixer.Sound("explosion.wav")
            game_over_Sound.play()
            mixer.music.play(-1)
        
        snake_x = (snake_x + vel_x)%width
        snake_y = (snake_y + vel_y)%height



        
        win.fill(black)
        mytext("Score:"+str(score),white,5,5)
        plot_snake(win,green,snake_list,snake_size)
        py.draw.rect(win,red,(food_x,food_y,food_size,food_size))
        clock.tick(fps)
        py.display.update()
py.quit()
quit()
