import pygame
import sys 
from scripts import add_XO, mark_draws, small_win_board_change
from variables import SCREEN, FONT, O_IMG, X_IMG, BG_COLOR, board, graphical_board



if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("Super Tic Tac Toe!")

    BOARD = pygame.image.load("SuperTicTacToe/assets/board.png").convert()
    BOARD = pygame.transform.scale(BOARD, (600, 600))
    BOARD.set_colorkey((255,255,255))
    
    SCREEN.fill(BG_COLOR)
    SCREEN.blit(BOARD, (0,200))

    pygame.display.update()

    to_move = "X"

    textX = FONT.render('X TO MOVE', True, (44, 143, 192))
    textRectX = textX.get_rect()
    textRectX.center = (300,100)
    textO = FONT.render('O TO MOVE', True, (223, 0, 39), BG_COLOR)
    textRectO = textO.get_rect()
    textRectO.center = (300,100)
    SCREEN.blit(textX, textRectX)
    game_finished = False
    next_move = (None, None)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                SCREEN.fill(BG_COLOR)
                SCREEN.blit(BOARD, (0,200))
                board, to_move, next_move = add_XO(board, graphical_board, to_move, next_move)
                if to_move=="X":
                    SCREEN.blit(textX, textRectX)
                else:
                    SCREEN.blit(textO, textRectO)
                small_win_board_change()
                mark_draws(board) #we want the red square to stay in its place until end of the game, thats why this function is called in the main game loop
        pygame.display.flip()
        