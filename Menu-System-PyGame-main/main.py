
import pygame ,sys
from button import Button
from reflection import reflect
from pyvidplayer import Video

pygame.init()

SCREEN = pygame.display.set_mode((1200, 600))
pygame.display.set_caption("RJSS Games")

Bg = pygame.image.load("assets/Cool Sky.png")

vid = Video("assets/vid.mp4")
vid.set_size((1200, 600))


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.otf", size)



def Refraction():
    while True:
        Refraction_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("Cyan")

        Refraction_TEXT = get_font(45).render("Yaha Refraction hoga", True, "Black")
        Refraction_RECT = Refraction_TEXT.get_rect(center=(600, 260))
        SCREEN.blit(Refraction_TEXT, Refraction_RECT)

        Refraction_BACK = Button(image=None, pos=(600, 460),
                              text_input="BACK", font=get_font(40), base_color="Black", hovering_color="Green")

        Refraction_BACK.changeColor(Refraction_MOUSE_POS)
        Refraction_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Refraction_BACK.checkForInput(Refraction_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def intro():

    while True:
        vid.draw(SCREEN, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                vid.close()
                reflect()

def help():
        while True:
            Refraction_MOUSE_POS = pygame.mouse.get_pos()

            SCREEN.fill("Cyan")

            Help_TEXT = get_font(45).render("Yaha Refraction hoga", True, "Black")
            Help_RECT = Help_TEXT.get_rect(center=(600, 260))
            SCREEN.blit(Help_TEXT, Help_RECT)

            Help_BACK = Button(image=None, pos=(600, 460),
                                     text_input="BACK", font=get_font(40), base_color="Black", hovering_color="Green")

            Help_BACK.changeColor(Refraction_MOUSE_POS)
            Help_BACK.update(SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if Help_BACK.checkForInput(Refraction_MOUSE_POS):
                        main_menu()

            pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(Bg, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(120).render("RJSS Games", True, "#ffb700")
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
                    reflect()
                if Refraction_BUTTON.checkForInput(MENU_MOUSE_POS):
                    Refraction()
                if HELP_BUTTON.checkForInput(MENU_MOUSE_POS):
                    help()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()
