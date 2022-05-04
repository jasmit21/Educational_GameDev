# import  pygame,sys
# import  math
#
# pygame.init()
#
#
# pygame.display.set_caption("Reflection")
#
#
#
# #colours
# black = (0,0,0)
# white = (255,255,255)
#
# red = (255,0,0)
# green = (0,255,0)
# blue = (0,0,255)
#
#
# def reflectLaser(endx,playery,laserAngle):
#     pygame.draw.line(screen,green,(endx,(playery - 325)),(endx - (465 * math.tan(math.radians(laserAngle))),(playery + 140)),2)
#
#     pygame.draw.line(screen,black,(endx,(playery - 325)),(endx,(playery - 275)),1)
#     pygame.draw.line(screen,black,(endx,(playery - 250)),(endx,(playery - 200)),1)
#     pygame.draw.line(screen,black,(endx,(playery - 175)),(endx,(playery - 125)),1)
#
# while True:
#     screen.fill('#FFE7BD')
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#
#     pygame.display.update()
#

#

import pygame


screen = pygame.display.set_mode((1200,600))

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


def reflect():

    playerx = -150.5
    # playery = -115
    playery = 0
    movetop = 0
    movebottom = 0
    playerCentre = 600
    laserAngle =0

    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                     movetop = 1

                if event.key == pygame.K_DOWN:
                     movebottom = 1

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                     movetop = 0

                if event.key == pygame.K_DOWN:
                     movebottom = 0


        screen.fill('#FFE7BD')

        laserImage = pygame.image.load('laser.png')

        player(playerx,playery,rot_center(laserImage,(laserAngle)))

        if playery > -115:  # user movement logic
            playery = playery - movetop

        if playery <435:
            playery = playery + movebottom

        pygame.display.update()

