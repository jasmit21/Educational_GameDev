import pygame
import time
import math

pygame.init()

displayWidth = 1200  # display width variable
displayHeight = 600  # display height variable

black = (0, 0, 0)  # colours
white = (255, 255, 255)

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))  # create window
pygame.display.set_caption("Laser Simulation")  # create title
clock = pygame.time.Clock()  # set clock

font14 = pygame.font.SysFont("monospace", 14)  # create font size 14
font20 = pygame.font.SysFont("monospace", 20)  # create font size 20

laserImage = pygame.image.load('laser.png')


def rot_center(image, angle):
    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image


def screen():  # draw screen overlay
    pygame.draw.rect(gameDisplay, black, (10, 10, 780, 600), 1)
    pygame.draw.rect(gameDisplay, black, (12, 12, 776, 600), 1)


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

        pygame.draw.rect(gameDisplay, black, (300, 265, 200, 70))
        pygame.draw.rect(gameDisplay, white, (302, 267, 196, 66))

        quitPrompt = font14.render("Would you like to quit?", 1, black)
        quitYes = font20.render("YES", 1, black)
        quitNo = font20.render("NO", 1, black)

        if userQuit == 1:  # user selection box
            pygame.draw.rect(gameDisplay, black, (333, 301, 40, 20), 1)

        if userQuit == 0:
            pygame.draw.rect(gameDisplay, black, (431, 301, 31, 20), 1)

        gameDisplay.blit(quitPrompt, (309, 273))  # print user prompt quit?(Y/N)
        gameDisplay.blit(quitYes, (335, 300))
        gameDisplay.blit(quitNo, (435, 300))

        pygame.display.update()


def player(playerx, playery, playerCentre, rot_image):  # player's laser
    gameDisplay.blit(rot_image, (playerx, playery))


def refractLaser(endx, playery, laserAngle):
    pygame.draw.line(gameDisplay, green, (endx, (playery - 125)), (
    (endx - (250 * math.tan(math.radians(math.asin((math.sin(laserAngle)) / 1.33))))), (playery - 225)), 2)
    ##pygame.draw.line (gameDisplay,green,((endx + 170 -(620 * math.tan(math.radians(laserAngle)))),(playery -225)),((playerx + 139 - (620 * math.tan(math.radians(laserAngle)))),(playery - 480)),2)


def shootLaser(playerx, playery, laserAngle):
    endx = playerx + 139 - (465 * math.tan(math.radians(laserAngle)))

    if endx > 100 and endx < 700:
        pygame.draw.line(gameDisplay, green, ((playerx + 139), (playery + 140)), (endx, (playery - 125)), 2)
        refractLaser(endx, playery, laserAngle)
        print(endx - ((250 * math.tan(math.asin((math.sin(math.radians(laserAngle))))))))
        print(endx)
        print(math.asin((math.sin(laserAngle)) / 1.33))
    else:
        pygame.draw.line(gameDisplay, green, ((playerx + 139), (playery + 140)),
                         ((playerx + 139 - (620 * math.tan(math.radians(laserAngle)))), (playery - 480)), 2)


def refract():  # gameloop

    exitGame = False  # game loop variable

    userQuit = 0  # detect quit variable

    laserState = -1  # laser on/off

    laserAngle = 0

    playerx = displayWidth / 2 - 140
    playery = 475  # y

    moveLeft = 0  # player movement variable
    moveRight = 0

    leftTilt = 0
    rightTilt = 0

    cord_x = 100
    cord_y = 250

    size_width = 600
    size_height = 100

    cord_xm = 0
    cord_ym = 0

    playerCentre = displayWidth / 2 - 140  # player centre variable used for laser

    while not exitGame:

        for event in pygame.event.get():  # gets all events and user input

            if event.type == pygame.QUIT:
                quitMenu(userQuit)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    moveLeft = 5

                if event.key == pygame.K_RIGHT:
                    moveRight = 5

                if event.key == pygame.K_DOWN:
                    cord_ym = 5

                if event.key == pygame.K_UP:
                    cord_ym = -5

                if event.key == pygame.K_COMMA:
                    cord_xm = -5

                if event.key == pygame.K_PERIOD:
                    cord_xm = 5

                if event.key == pygame.K_RETURN:
                    laserState = laserState * -1

                if event.key == pygame.K_a:
                    leftTilt = 1

                if event.key == pygame.K_d:
                    rightTilt = 1

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    moveLeft = 0

                if event.key == pygame.K_RIGHT:
                    moveRight = 0

                if event.key == pygame.K_DOWN:
                    cord_ym = 0

                if event.key == pygame.K_UP:
                    cord_ym = 0

                if event.key == pygame.K_COMMA:
                    cord_xm = 0

                if event.key == pygame.K_PERIOD:
                    cord_xm = 0

                if event.key == pygame.K_a:
                    leftTilt = 0

                if event.key == pygame.K_d:
                    rightTilt = 0

        cord_x += cord_xm
        cord_y += cord_ym

        gameDisplay.fill(white)
        pygame.draw.rect(gameDisplay, blue, [cord_x, cord_y, size_width, size_height])
        if laserAngle < 70:
            laserAngle = laserAngle + leftTilt

        if laserAngle > -70:
            laserAngle = laserAngle - rightTilt

        if laserState == 1:
            shootLaser(playerx, playery, laserAngle)

        player(playerx, playery, playerCentre, rot_center(laserImage, (laserAngle)))

        if playerx > -115:  # user movement logic
            playerx = playerx - moveLeft
            playerCentre = playerCentre - moveLeft

        if playerx < 630:
            playerx = playerx + moveRight
            playerCentre = playerCentre + moveRight

        pygame.display.update()  # refresh
        clock.tick(59)
        print(laserAngle)
