import pygame, sys, os
from buttonExtra import Button
import main2
import main

pygame.init()

screen = pygame.display.set_mode((1280, 720))

soundtracks = ["assets/soundtrack1.mp3", "assets/soundtrack2.mp3", "assets/soundtrack3.mp3", "assets/soundtrack4.mp3"]
background_paths = ["assets/uno.png", "assets/dos.jpg", "assets/tres.jpg", "assets/quatro.jpg", "assets/sth.jpg", "assets/forest.jpg"]
mini_backgrounds = []

for path in background_paths:
    bg_image = pygame.image.load(path)
    mini_bg = pygame.transform.scale(bg_image, (1280/4, 720/4))
    mini_backgrounds.append(mini_bg)

BG = pygame.image.load("assets/dos.jpg")
BG = pygame.transform.scale(BG, (screen.get_width(), screen.get_height()))

current_volume = 0.5
slider_length = 200
slider_height = 20
slider_x = (screen.get_width() - slider_length) // 2
slider_y = 600
slider_bg_rect = pygame.Rect(slider_x, slider_y, slider_length, slider_height)
slider_btn_width = 20
slider_btn_height = slider_height
slider_btn_x = slider_x + (current_volume * (slider_length - slider_btn_width))
slider_btn_rect = pygame.Rect(slider_btn_x, slider_y, slider_btn_width, slider_btn_height)

dragging = False

pygame.mixer.music.set_volume(current_volume)
pygame.mixer.music.load("assets/soundtrack1.mp3")
pygame.mixer.music.play(-1)

game_paused = False

font = pygame.font.Font("assets/font.ttf", 36)

TEXT_COL = (255, 255, 255)

def get_font(size):
    return pygame.font.Font("assets/fontdos.ttf", size)

def change_soundtrack():
    pygame.display.set_caption("Soundtrack")
    global current_volume, dragging
    while True:
        screen.blit(BG, (0,0))
        CHANGE_MOUSE_POS = pygame.mouse.get_pos()

        buttons = []
        titles = ["Solve The Game", "Energy Inflow", "Smoke The Joint", "Party Mood"]
        for i, track in enumerate(soundtracks):
            track_title = titles[i]
            button = Button(image=None, pos=(640, 100 + i * 100), text_input=f"{track_title}", font=get_font(40), base_color="Black", hovering_color="White")
            buttons.append(button)

        BACK_BUTTON = Button(image=None, pos=(640, 100 + len(soundtracks) * 100), text_input="BACK", font=get_font(30), base_color="Black", hovering_color="White")

        for button in buttons + [BACK_BUTTON]:
            button.changeColor(CHANGE_MOUSE_POS)
            button.update(screen)
        
        pygame.draw.rect(screen, (100, 100, 100), slider_bg_rect)  # Draw slider background
        pygame.draw.rect(screen, (200, 200, 200), slider_btn_rect)  # Draw slider button

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK_BUTTON.checkForInput(CHANGE_MOUSE_POS):
                    options()
                for i, button in enumerate(buttons):
                    if button.checkForInput(CHANGE_MOUSE_POS):
                        pygame.mixer.music.load(soundtracks[i])
                        pygame.mixer.music.play(-1)
                if slider_btn_rect.collidepoint(event.pos):
                    dragging = True
            elif event.type == pygame.MOUSEMOTION:
                if dragging:
                    # Update slider button and volume
                    slider_btn_rect.x = min(max(event.pos[0], slider_x), slider_x + slider_length - slider_btn_width)
                    current_volume = (slider_btn_rect.x - slider_x) / (slider_length - slider_btn_width)
                    pygame.mixer.music.set_volume(current_volume)
            elif event.type == pygame.MOUSEBUTTONUP:
                dragging = False
        
        slider_btn_rect.x = slider_x + (current_volume * (slider_length - slider_btn_width))

        pygame.display.update()

def change_background():
    pygame.display.set_caption("Background")
    mini_per_row = 3
    miniature_width = 1280 // 5
    miniature_height = 720 // 5
    spacing = 60  # Spacing between miniatures

    while True:
        screen.fill("#fff2cc")
        BG_MOUSE_POS = pygame.mouse.get_pos()

        BACK_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 650), text_input="BACK", font=get_font(50), base_color="Black", hovering_color="#6fa8dc")
        BACK_BUTTON.changeColor(BG_MOUSE_POS)
        BACK_BUTTON.update(screen)

        for i, mini_bg in enumerate(mini_backgrounds):
            row = i // mini_per_row
            col = i % mini_per_row

            x = 150 + col * (miniature_width + spacing)
            y = 100 + row * (miniature_height + spacing * 2)

            screen.blit(mini_bg, (x, y))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if BACK_BUTTON.checkForInput(BG_MOUSE_POS):
                    options()
                else:
                    for i in range(len(mini_backgrounds)):
                        row = i // mini_per_row
                        col = i % mini_per_row
                        x = 100 + col * (miniature_width + spacing)
                        y = 100 + row * (miniature_height + spacing * 2)
                        mini_bg_rect = pygame.Rect(x, y, miniature_width, miniature_height)
                        if mini_bg_rect.collidepoint(event.pos):
                            global BG
                            BG = pygame.image.load(background_paths[i])
                            BG = pygame.transform.scale(BG, (screen.get_width(), screen.get_height()))
                            return

        pygame.display.update()

def game_chess():
    pygame.display.set_caption("Chess")
    while True:
        screen.blit(BG, (0,0))
        GAME_CHESS_MOUSE_POS = pygame.mouse.get_pos()
        BACK_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400), 
                                    text_input="BACK", font=get_font(50), base_color="Black", hovering_color="WHITE")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 500), 
                                    text_input="QUIT", font=get_font(50), base_color="Black", hovering_color="RED")
        MULTIPLAYED_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 300), 
                                    text_input="PLAY", font=get_font(50), base_color="Black", hovering_color="WHITE")
        #SINGLEPLAYER_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 300), 
                                    #text_input="SINGLEPLAYER", font=get_font(50), base_color="Black", hovering_color="WHITE")

        for button in [BACK_BUTTON, QUIT_BUTTON, MULTIPLAYED_BUTTON]:
            button.changeColor(GAME_CHESS_MOUSE_POS)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK_BUTTON.checkForInput(GAME_CHESS_MOUSE_POS):
                    main_menu()
                if QUIT_BUTTON.checkForInput(GAME_CHESS_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
                if MULTIPLAYED_BUTTON.checkForInput(GAME_CHESS_MOUSE_POS):
                    main.main()
                ##if SINGLEPLAYER_BUTTON.checkForInput(GAME_CHESS_MOUSE_POS):
                   ## main.main()

        pygame.display.update()

def game_super_tic_tac_toe():
    pygame.display.set_caption("TicTacToe")
    while True:
        screen.blit(BG, (0,0))
        GAME_TTT_MOUSE_POS = pygame.mouse.get_pos()
        BACK_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400), 
                                    text_input="BACK", font=get_font(50), base_color="Black", hovering_color="WHITE")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 500), 
                                    text_input="QUIT", font=get_font(50), base_color="Black", hovering_color="RED")
        MULTIPLAYED_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 300), 
                                    text_input="PLAY", font=get_font(50), base_color="Black", hovering_color="WHITE")
        #SINGLEPLAYER_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 300), 
                                    #text_input="SINGLEPLAYER", font=get_font(50), base_color="Black", hovering_color="WHITE")

        for button in [BACK_BUTTON, QUIT_BUTTON, MULTIPLAYED_BUTTON]:
            button.changeColor(GAME_TTT_MOUSE_POS)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK_BUTTON.checkForInput(GAME_TTT_MOUSE_POS):
                    main_menu()
                if QUIT_BUTTON.checkForInput(GAME_TTT_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
                if MULTIPLAYED_BUTTON.checkForInput(GAME_TTT_MOUSE_POS):
                    main2.main2()
                ##if SINGLEPLAYER_BUTTON.checkForInput(GAME_TTT_MOUSE_POS):
                   ## main2.main2()

        pygame.display.update()

def options():
    pygame.display.set_caption("Options")
    while True:
        screen.blit(BG, (0,0))
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        BACK_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400), 
                                    text_input="BACK", font=get_font(50), base_color="Black", hovering_color="WHITE")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 500), 
                                    text_input="QUIT", font=get_font(50), base_color="Black", hovering_color="RED")
        CH_BG_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 300), 
                                    text_input="BACKGROUND", font=get_font(50), base_color="Black", hovering_color="WHITE")
        CH_SOUNDTRACK_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 200), 
                                    text_input="SOUNDTRACK", font=get_font(50), base_color="Black", hovering_color="WHITE")


        for button in [BACK_BUTTON, QUIT_BUTTON, CH_BG_BUTTON, CH_SOUNDTRACK_BUTTON]:
            button.changeColor(OPTIONS_MOUSE_POS)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()
                if QUIT_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
                if CH_SOUNDTRACK_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    change_soundtrack()
                if CH_BG_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    change_background()

        pygame.display.update()

def main_menu():
    pygame.display.set_caption("Menu")
    run = True
    global current_volume, dragging
    while run:
        screen.blit(BG, (0,0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 500), 
                                text_input="QUIT", font=get_font(50), base_color="Black", hovering_color="RED")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400), 
                                text_input="OPTIONS", font=get_font(50), base_color="Black", hovering_color="White")
        CHESS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 300), 
                            text_input="CHESS", font=get_font(50), base_color="Black", hovering_color="White")
        SUPER_TIC_TAC_TOE_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 200), 
                            text_input="SUPER TIC TAC TOE", font=get_font(50), base_color="Black", hovering_color="White")
        
        for button in [QUIT_BUTTON, CHESS_BUTTON, SUPER_TIC_TAC_TOE_BUTTON, OPTIONS_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if SUPER_TIC_TAC_TOE_BUTTON.checkForInput(MENU_MOUSE_POS):
                    game_super_tic_tac_toe()
                if CHESS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    game_chess()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
                
        pygame.display.update()

main_menu()
pygame.mixer.music.stop()
pygame.quit()