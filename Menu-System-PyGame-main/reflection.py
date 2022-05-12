import math
import sys
import pygame
from button import Button
from pyvidplayer import Video
from refraction import refract
pygame.init()


display_widhth = 1200
display_height = 600
screen = pygame.display.set_mode((display_widhth,display_height))
green =(0,255,0)
black = (0,0,0)
red = (255,0,0)
white = (255,255,255)

font14 = pygame.font.SysFont("font.otf" , 22)
font20 = pygame.font.SysFont("font.otf", 22)


SCREEN = pygame.display.set_mode((1200, 600))
pygame.display.set_caption("RJSS Games")
Logo = pygame.image.load("assets/Logo.png")
pygame.display.set_icon(Logo)
Bg = pygame.image.load("assets/Cool Sky.png")

vid = Video("assets/vid.mp4")
vid2 = Video("assets/vid2.mp4")
vid2.set_size((1200, 600))
vid.set_size((1200, 600))


def player(playerx,playery,rot_image):
    screen.blit(rot_image,(playerx,playery))

def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.otf", size)

def intro():

    while True:
        vid.draw(SCREEN, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                vid.close()
                reflect()

def intro2():

    while True:
        vid2.draw(SCREEN, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                vid2.close()
                refract()

def main_menu():
    while True:
        SCREEN.blit(Bg, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(120).render("Let The Light Reflect", True, "#ffb700")
        MENU_RECT = MENU_TEXT.get_rect(center=(600, 65))  #80

        Reflection_BUTTON = Button(image=pygame.image.load("assets/Reflection Rect.png"), pos=(600, 175),#200
                             text_input="Reflection", font=get_font(70), base_color="Black", hovering_color="White")
        Refraction_BUTTON = Button(image=pygame.image.load("assets/Refraction Rect.png"), pos=(600, 292), #350
                                text_input="Refraction", font=get_font(70), base_color="Black", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(600, 530),#490
                             text_input="EXIT", font=get_font(70), base_color="Black", hovering_color="White")
        HELP_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(600, 410),
                             text_input="Help", font=get_font(70), base_color="Black", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [Reflection_BUTTON, Refraction_BUTTON, QUIT_BUTTON, HELP_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Reflection_BUTTON.checkForInput(MENU_MOUSE_POS):
                    intro()
                    # reflect()
                if Refraction_BUTTON.checkForInput(MENU_MOUSE_POS):
                    intro2()
                    # refract()
                if HELP_BUTTON.checkForInput(MENU_MOUSE_POS):
                    help()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


    
def quitMenu(userQuit):  # quit menu options

    while True:

        for event in pygame.event.get():  # get user events

            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                if event.key == pygame.K_LEFT:
                    userQuit = 1

                if event.key == pygame.K_RIGHT:
                    userQuit = 0

                if event.key == pygame.K_RETURN:
                    if userQuit == 1:
                        exitGame = True
                        main_menu()



                    else:
                        return

        pygame.draw.rect(screen, black, (500, 265, 200, 70))
        pygame.draw.rect(screen, white, (502, 267, 196, 66))


        quitPrompt = font14.render("Return to main menu?", 1, black)
        quitYes = font20.render("YES", 1, black)
        quitNo = font20.render("NO", 1, black)

        if userQuit == 1:  # user selection box
            pygame.draw.rect(screen, black, (533, 301, 40, 20), 1)

        if userQuit == 0:
            pygame.draw.rect(screen, black, (631, 301, 31, 20), 1)

        screen.blit(quitPrompt, (520, 276))  # print user prompt quit?(Y/N)
        screen.blit(quitYes, (537, 305))
        screen.blit(quitNo, (635, 305))

        pygame.display.update()


def rot_center(image, angle):
    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image


def reflectLaser(endy, playerx, laserAngle):

    # pygame.draw.line(screen, green, ((playerx + 140),endy),((playerx+140),endy - (400 * math.tan(math.radians(laserAngle)))), 2)
    pygame.draw.line(screen, red, ((playerx + 1000.5),endy),((playerx+150.5),endy - (1020* math.tan(math.radians(laserAngle)))), 2)

    pygame.draw.line(screen, black, ( (playerx + 1000.5),endy), ( (playerx + 950.5),endy), 1)
    pygame.draw.line(screen, black, ( (playerx + 925.5),endy), ( (playerx + 875.5),endy), 1)
    pygame.draw.line(screen, black, ( (playerx + 850.5),endy), ( (playerx + 800.5),endy), 1)

def shootLaser(playerx,playery,laserAngle):

    x = 1020  #-150.5
    endy = playery + 140 - (x * math.tan(math.radians(laserAngle)))

    # if  endy > 22 and endy < 570:
    pygame.draw.line(screen,green,((playerx + 150),(playery + 140)),((playerx + 1000),endy,),2)
    if endy > 22 and endy < 570:
        reflectLaser(endy,playerx,laserAngle)

# def reflect():
#
#     userQuit = 0
#     laserState = -1
#     playerx = -150.5
#     # playery = -115
#     playery = 0
#     movetop = 0
#     movebottom = 0
#     playerCentre = 600
#     laserAngle =0
#
#     leftTilt=0
#     rightTilt=0
#
#     while True:
#
#         for event in pygame.event.get():
#
#             if event.type == pygame.QUIT:
#                 quitMenu(userQuit)
#
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_UP or event.key == pygame.K_w:
#                      movetop = 1
#
#                 if event.key == pygame.K_DOWN or event.key == pygame.K_s:
#                      movebottom = 1
#
#                 if event.key == pygame.K_a:
#                     leftTilt = 1
#
#                 if event.key == pygame.K_d:
#                     rightTilt = 1
#
#                 if event.key == pygame.K_RETURN:
#                     laserState = laserState * -1
#
#                 if event.key == pygame.K_ESCAPE:
#                     quitMenu(userQuit)
#                     # pygame.quit()
#                     # sys.exit()
#
#             if event.type == pygame.KEYUP:
#                 if event.key == pygame.K_UP or event.key == pygame.K_w:
#                      movetop = 0
#
#                 if event.key == pygame.K_DOWN or event.key == pygame.K_s:
#                      movebottom = 0
#
#                 if event.key == pygame.K_a:
#                     leftTilt = 0
#
#                 if event.key == pygame.K_d:
#                     rightTilt = 0
#
#
#         screen.fill('#FFE7BD')
#
#         laserImage = pygame.image.load('laser.png')
#
#         if laserState == 1:
#             shootLaser(playerx,playery,laserAngle)
#
#         if laserAngle < 55:
#             laserAngle = laserAngle + leftTilt
#
#         if laserAngle > -55:
#             laserAngle = laserAngle - rightTilt
#
#         player(playerx,playery,rot_center(laserImage,(laserAngle)))
#
#         if playery > -55:  # user movement logic
#             playery = playery - movetop
#
#         if playery <375:
#             playery = playery + movebottom
#
#         pygame.display.update()
def mirror():
    pygame.draw.rect(screen, black, (850,20, 20, 550))
def reflect():

    userQuit = 0
    laserState = -1
    playerx = -150.5

    playery = display_height/2 -140
    movetop = 0
    movebottom = 0
    # playerCentre = 600
    laserAngle =0

    leftTilt=0
    rightTilt=0

    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                quitMenu(userQuit)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                     movetop = 1

                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                     movebottom = 1

                if event.key == pygame.K_a:
                    leftTilt = 0.2

                if event.key == pygame.K_d:
                    rightTilt = 0.2

                if event.key == pygame.K_RETURN:
                    laserState = laserState * -1

                if event.key == pygame.K_ESCAPE:
                    quitMenu(userQuit)
                    # pygame.quit()
                    # sys.exit()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                     movetop = 0

                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                     movebottom = 0

                if event.key == pygame.K_a:
                    leftTilt = 0

                if event.key == pygame.K_d:
                    rightTilt = 0


        screen.fill('#FFE7BD')
        mirror()

        laserImage = pygame.image.load('laser.png')

        if laserState == 1:
            shootLaser(playerx,playery,laserAngle)

        if laserAngle < 55:
            laserAngle = laserAngle + leftTilt

        if laserAngle > -55:
            laserAngle = laserAngle - rightTilt

        player(playerx,playery,rot_center(laserImage,(laserAngle)))

        if playery > -55:  # user movement logic
            playery = playery - movetop

        if playery <375:
            playery = playery + movebottom

        pygame.display.update()

# reflect()