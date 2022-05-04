
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

