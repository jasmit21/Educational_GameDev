import math
import sys

import pygame
pygame.init()
display_widhth = 1200
display_height = 600
screen = pygame.display.set_mode((display_widhth,display_height))
green =(0,255,0)
black = (0,0,0)
white = (255,255,255)

font14 = pygame.font.SysFont("font.otf" , 22)
font20 = pygame.font.SysFont("font.otf", 22)

def player(playerx,playery,rot_image):
    screen.blit(rot_image,(playerx,playery))
    
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
                        quit()

                    else:
                        return

        pygame.draw.rect(screen, black, (500, 265, 200, 70))
        pygame.draw.rect(screen, white, (502, 267, 196, 66))


        quitPrompt = font14.render("Would you like to quit?", 1, black)
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

    # pygame.draw.line(screen, green, (endy, (playery - 325)),
    #                  (endy - (465 * math.tan(math.radians(laserAngle))), (playery + 140)), 2)

    pygame.draw.line(screen, green, ((playerx + 140),endy),((playerx+140),endy - (400 * math.tan(math.radians(laserAngle)))), 2)

    pygame.draw.line(screen, black, ( (playerx + 1000.5),endy), ( (playerx + 950.5),endy), 1)
    pygame.draw.line(screen, black, ( (playerx + 925.5),endy), ( (playerx + 875.5),endy), 1)
    pygame.draw.line(screen, black, ( (playerx + 850.5),endy), ( (playerx + 800.5),endy), 1)
    # pygame.draw.line(screen, black, (endy, (playery - 325)), (endy, (playery - 275)), 1)
    # pygame.draw.line(screen, black, (endy, (playery - 250)), (endy, (playery - 200)), 1)
    # pygame.draw.line(screen, black, (endy, (playery - 175)), (endy, (playery - 125)), 1)

def shootLaser(playerx,playery,laserAngle):

    x = 1020  #-150.5
    endy = playery + 140 - (x * math.tan(math.radians(laserAngle)))

    if  endy > 22 and endy < 570:
        pygame.draw.line(screen,green,((playerx + 150),(playery + 140)),((playerx + 1000),endy,),2)
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