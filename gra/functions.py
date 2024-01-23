import pygame, sys
from buttonExtra import Button
from launch import *

pygame.init()

screen = pygame.display.set_mode((1280, 720))
BG = pygame.image.load("assets/dos.jpg")
BG = pygame.transform.scale(BG, (screen.get_width(), screen.get_height()))

def pause_menu():
    while True:
        screen.blit(BG, (0,0))
        GAME_PAUSE_MOUSE_POS = pygame.mouse.get_pos()

        CONTINUE_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 250),
                                 text_input="CONTINUE", font=get_font(50), base_color="Black", hovering_color="WHITE")
        BACK_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 350),
                             text_input="BACK", font=get_font(50), base_color="Black", hovering_color="WHITE")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 450),
                             text_input="QUIT", font=get_font(50), base_color="Black", hovering_color="RED")

        for button in [CONTINUE_BUTTON, BACK_BUTTON, QUIT_BUTTON]:
            button.changeColor(GAME_PAUSE_MOUSE_POS)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if CONTINUE_BUTTON.checkForInput(GAME_PAUSE_MOUSE_POS):
                    return  # Wznowienie gry
                if BACK_BUTTON.checkForInput(GAME_PAUSE_MOUSE_POS):
                    main_menu()
                if QUIT_BUTTON.checkForInput(GAME_PAUSE_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()