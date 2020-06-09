import pygame
import time
import random
 
pygame.init()

#############
#crash_sound = pygame.mixer.Sound("crash.wav")
#############
 
display_width = 800
display_height = 600
 
black = (0,0,0)
white = (255,255,255)

red = (200,0,0)
green = (0,200,0)
yellow = (255,255,0)

bright_red = (255,0,0)
bright_green = (0,255,0)
 
block_color = (bright_red)
 
ship_width = 73
 
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('The Space Express')
clock = pygame.time.Clock()
 
shipImg = pygame.image.load('c:/Users/Philipp Baar/Desktop/coding/spaceship_red.png').convert()
#gameIcon = pygame.image.load('carIcon.png')

#pygame.display.set_icon(gameIcon)

pause = False
crash = True
 
def boxs_dodged(count):
    font = pygame.font.SysFont("comicsansms", 25)
    text = font.render("Dodged: "+str(count), True, yellow)
    gameDisplay.blit(text,(0,0))
 
def boxs(boxx, boxy, boxw, boxh, color):
    pygame.draw.rect(gameDisplay, color, [boxx, boxy, boxw, boxh])

def stars(starcolor, starcenter, starradius, starwidth):
    pygame.draw.circle(gameDisplay, starcolor, (starcenter,starradius), starwidth)
 
def ship(x,y):
    gameDisplay.blit(shipImg,(x,y))
 
def text_objects(text, font):
    textSurface = font.render(text, True, yellow)
    return textSurface, textSurface.get_rect()

def hull_status(hulldmg):
    font = pygame.font.SysFont("comicsansms", 25)
    text = font.render("Hull: "+str(), True, yellow)
    gameDisplay.blit(text,(10,0))


def damagecount(dmg):
    #hulldmg = 0
    dmg += 1
    if dmg == 5:
        crash()

def crash():
    ####################################
  #  pygame.mixer.Sound.play(crash_sound)
 #   pygame.mixer.music.stop()
    ####################################
    largeText = pygame.font.SysFont("comicsansms",115)
    TextSurf, TextRect = text_objects("You Crashed", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        

        button("Start Again",150,450,100,50,green,bright_green,game_loop)
        button("Quit",550,450,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15) 

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))
    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)
    

def quitgame():
    pygame.quit()
    quit()

def unpause():
    global pause
    #pygame.mixer.music.unpause()
    pause = False
    

def paused():
    ############
    #pygame.mixer.music.pause()
    #############
    largeText = pygame.font.SysFont("comicsansms",115)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        button("Continue",150,450,100,50,green,bright_green,unpause)
        button("Quit",550,450,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)   


def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(white)
        largeText = pygame.font.SysFont("comicsansms",115)
        TextSurf, TextRect = text_objects("Space Express", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("GO!",150,450,100,50,green,bright_green,game_loop)
        button("Quit",550,450,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)
        
        
    
    

    
def game_loop():
    global pause
    ############
    #pygame.mixer.music.load('jazz.wav')
    #pygame.mixer.music.play(-1)
    ############
    x = (display_width * 0.45)
    y = (display_height * 0.8)
 
    x_change = 0
 
    box_startx = random.randrange(0, display_width)
    box_starty = -600
    box_speed = 3
    box_width = 50
    box_height = 50

    star_center = random.randrange(0, display_width)
    star_radius = 10
    star_width = 5
    star_speed = 50
 
    boxCount = 1
 
    dodged = 0
    dmg = 0
    
 
    gameExit = False
 
    while not gameExit:
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_p:
                    pause = True
                    paused()
                    
 
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
 
        x += x_change
        gameDisplay.fill(black)
 
        boxs(box_startx, box_starty, box_width, box_height, block_color)
        #stars(white, 150,150, 75)
        stars(white, star_center, star_radius, star_width)
        stars(white, star_center, star_radius, star_width)
        stars(white, star_center, star_radius, star_width)
        stars(white, star_center, star_radius, star_width)
        stars(white, star_center, star_radius, star_width)
        stars(white, star_center, star_radius, star_width)
        stars(white, star_center, star_radius, star_width)
        stars(white, star_center, star_radius, star_width)
        stars(white, star_center, star_radius, star_width)
        stars(white, star_center, star_radius, star_width)
        stars(white, star_center, star_radius, star_width)
        stars(white, star_center, star_radius, star_width)
        stars(white, star_center, star_radius, star_width)
        stars(white, star_center, star_radius, star_width)
        stars(white, star_center, star_radius, star_width)
        stars(white, star_center, star_radius, star_width)
 
        star_radius += star_speed
        box_starty += box_speed
        ship(x,y)
        boxs_dodged(dodged)
        
        hull_status(dmg)
        #hulldmg = 0
 
        if x > display_width - ship_width or x < 0:
            damagecount(dmg)
            #hulldmg += 1
            #crash()
 
        if box_starty > display_height:
            box_starty = 0 - box_height
            box_startx = random.randrange(0,display_width)
            dodged += 1
            box_speed += 0.8
            box_width += (dodged * 1.1)

        if star_radius > display_height:
            star_radius = 0 - star_width
            star_center = random.randrange(0,display_width)


        if y < box_starty+box_height:
            #print('y crossover')
 
            if x > box_startx and x < box_startx + box_width or x+ship_width > box_startx and x + ship_width < box_startx+box_width:
                #print('x crossover')
                #crash()
                damagecount(dmg)
        
        pygame.display.update()
        clock.tick(60)

game_intro()
game_loop()
pygame.quit()
quit()