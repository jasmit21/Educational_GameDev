import math
import sys

import pygame
pygame.init()
screen = pygame.display.set_mode((1200,600))
green =(0,255,0)
black = (0,0,0)
white = (255,255,255)

font14 = pygame.font.SysFont("font.otf" , 22)
font20 = pygame.font.SysFont("monospace", 20)

def player(playerx,playery,rot_image):
    screen.blit(rot_image,(playerx,playery))
    
def quitMenu(userQuit):  # quit menu options

    while True:

        for event in pygame.event.get():  # get user events

            if event.type == pygame.KEYDOWN:
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

        pygame.draw.rect(screen, black, (300, 265, 200, 70))
        pygame.draw.rect(screen, white, (302, 267, 196, 66))

        quitPrompt = font14.render("Would you like to quit?", 1, black)
        quitYes = font20.render("YES", 1, black)
        quitNo = font20.render("NO", 1, black)

        if userQuit == 1:  # user selection box
            pygame.draw.rect(screen, black, (333, 301, 40, 20), 1)

        if userQuit == 0:
            pygame.draw.rect(screen, black, (431, 301, 31, 20), 1)

        screen.blit(quitPrompt, (309, 280))  # print user prompt quit?(Y/N)
        screen.blit(quitYes, (335, 300))
        screen.blit(quitNo, (435, 300))

        pygame.display.update()


def rot_center(image, angle):
    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image


def reflectLaser(endy, playery, laserAngle):
    pygame.draw.line(screen, green, (endy, (playery - 325)),
                     (endy - (465 * math.tan(math.radians(laserAngle))), (playery + 140)), 2)

    pygame.draw.line(screen, black, (endy, (playery - 325)), (endy, (playery - 275)), 1)
    pygame.draw.line(screen, black, (endy, (playery - 250)), (endy, (playery - 200)), 1)
    pygame.draw.line(screen, black, (endy, (playery - 175)), (endy, (playery - 125)), 1)

def shootLaser(playerx,playery,laserAngle):

    x = -145.5
    endy = playery + 800 + (x * math.tan(math.radians(laserAngle)))

    if  endy > 27 and endy < 773:
        pygame.draw.line(screen,green,((playerx + 139),(playery + 140)),(endy,(playery - 325)),2)
        reflectLaser(endy,playerx,laserAngle)

def reflect():

    userQuit = 0
    laserState = -1
    playerx = -150.5
    # playery = -115
    playery = 0
    movetop = 0
    movebottom = 0
    playerCentre = 600
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
                    leftTilt = 1

                if event.key == pygame.K_d:
                    rightTilt = 1

                if event.key == pygame.K_RETURN:
                    laserState = laserState * -1

                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

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

#mini proj