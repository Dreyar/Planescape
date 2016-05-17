import pygame
import time
import random

pygame.init()

crash_sound = pygame.mixer.Sound("crash.wav")

#megethos para8uroi
display_width = 800
display_height = 600

car_width = 76
car_height = 40

#xromata
black = (0,0,0)
white = (255,255,255)

#dimiourgia para8uroi
gameDisplay = pygame.display.set_mode((display_width,display_height))

#titlos para8uroi
pygame.display.set_caption('Planescape')

#to clock xreiazetai gia na ka8orisoume ta FPS
clock = pygame.time.Clock()

#eikona me aeroplanaki
planeImg = pygame.image.load('plane.png')

def things_dodge(count):
    font = pygame.font.SysFont(None,25)
    text = font.render('Dodged: ' + str(count), True, black)
    gameDisplay.blit(text,(600,0))


def things(thingX, thingY, thingW, thingH, thingC):
    pygame.draw.rect(gameDisplay, thingC,[thingX,thingY,thingW,thingY])


#methodos gia emfanisi aeroplanou
def plane(x,y):
    gameDisplay.blit(planeImg,(x,y))

def crash():
    pygame.mixer.Sound.play(crash_sound)
    message_display('Death!!')


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',110)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()

def text_objects(text,font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def game_loop():

    #arxiki tou 8esi
    x = (display_width * 0.9)
    y = (display_height * 0.8)

    #deiktes allagis 8eseis me ta velaki
    x_change = 0
    y_change = 0



    #death
    gameExit = False

    thing_startX = random.randrange(0,display_width-100)
    thing_startY = random.randrange(200,display_width-200)
    thing_speed = 8
    thing_width = 100
    thing_height = 100

    dodged = 0

    #loopaki mexri na xasoume
    while not gameExit:


        #an patisoyme X kleinei to paixnidi
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            #event handler gia ta pliktra
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_DOWN:
                    y_change = 5
                if event.key == pygame.K_UP:
                    y_change = -5

            #otan den ta patao pliktro oi deiktes allagis einai 0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    x_change = 0
                    y_change = 0

        x += x_change
        y += y_change

        #aspro fonto
        gameDisplay.fill(white)

        #things(thingX, thingY, thingW, thingH, thingC)
        things(thing_startX, thing_startY,thing_width,thing_height, black)
        thing_startX += thing_speed

        #zografizo to aeroplano
        plane(x,y)
        things_dodge(dodged)


        if thing_startX > display_width:
            thing_startX = random.randrange(0,display_width-799)
            thing_startY = random.randrange(0,display_height)
            dodged += 1
            thing_speed +=0.5


        if x <= thing_startX+thing_width:

            if y > thing_startY and y <= thing_startY + thing_height -40 or y + 40 > thing_startY and y + 40 < thing_startY + thing_height:
                print('crash')
                crash()

        #ananeono to periexomeno tou para8uroi
        pygame.display.update()

        #FPS
        clock.tick(60)



game_loop()
pygame.quit()
quit()


