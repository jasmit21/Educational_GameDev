import math

import pygame

screen = pygame.display.set_mode((1200,600))
green =(0,255,0)
black = (0,0,0)
white = (255,255,255)

def player(playerx,playery,rot_image):
    screen.blit(rot_image,(playerx,playery))

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
                pygame.quit()

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

