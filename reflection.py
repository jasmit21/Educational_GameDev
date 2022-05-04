import  pygame,sys


pygame.init()

screen = pygame.display.set_mode((1200,600))
pygame.display.set_caption("Reflection")

laserImage = pygame.image.load('laser.png')

while True:
    screen.fill('#FFE7BD')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()