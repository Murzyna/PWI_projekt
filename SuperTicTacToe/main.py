import pygame
import sys 
from scripts import add_XO



if __name__ == "__main__":
    pygame.init()
    WIDTH, HEIGHT = 600, 800
    FONT = pygame.font.Font("SuperTicTacToe/assets/Roboto-Regular.ttf", 100)
    SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("Super Tic Tac Toe!")

    BOARD = pygame.image.load("SuperTicTacToe/assets/board.png").convert()
    BOARD = pygame.transform.scale(BOARD, (600, 600))
    BOARD.set_colorkey((255,255,255))
    X_IMG = pygame.image.load("SuperTicTacToe/assets/X.png")
    X_IMG = pygame.transform.scale(X_IMG, (50, 50))
    O_IMG = pygame.image.load("SuperTicTacToe/assets/O2.png")
    O_IMG = pygame.transform.scale(O_IMG, (50, 50))
    O_IMG.set_colorkey((255,255,255))

    BG_COLOR = (245, 233, 200)
    SCREEN.fill(BG_COLOR)
    SCREEN.blit(BOARD, (0,200))

    pygame.display.update()
    board = [[[[1,2,3], [4,5,6], [7,8,9]], [[1,2,3], [4,5,6], [7,8,9]], [[1,2,3], [4,5,6], [7,8,9]]], 
                    [[[1,2,3], [4,5,6], [7,8,9]], [[1,2,3], [4,5,6], [7,8,9]], [[1,2,3], [4,5,6], [7,8,9]]], 
                    [[[1,2,3], [4,5,6], [7,8,9]], [[1,2,3], [4,5,6], [7,8,9]], [[1,2,3], [4,5,6], [7,8,9]]]]

    graphical_board = [[[[[None, None],[None,None],[None,None]], [[None, None],[None,None],[None,None]], [[None, None],[None,None],[None,None]]], [[[None, None],[None,None],[None,None]], [[None, None],[None,None],[None,None]], [[None, None],[None,None],[None,None]]], [[[None, None],[None,None],[None,None]], [[None, None],[None,None],[None,None]], [[None, None],[None,None],[None,None]]]], 
                                [[[[None, None],[None,None],[None,None]], [[None, None],[None,None],[None,None]], [[None, None],[None,None],[None,None]]], [[[None, None],[None,None],[None,None]], [[None, None],[None,None],[None,None]], [[None, None],[None,None],[None,None]]], [[[None, None],[None,None],[None,None]], [[None, None],[None,None],[None,None]], [[None, None],[None,None],[None,None]]]], 
                                [[[[None, None],[None,None],[None,None]], [[None, None],[None,None],[None,None]], [[None, None],[None,None],[None,None]]], [[[None, None],[None,None],[None,None]], [[None, None],[None,None],[None,None]], [[None, None],[None,None],[None,None]]], [[[None, None],[None,None],[None,None]], [[None, None],[None,None],[None,None]], [[None, None],[None,None],[None,None]]]]]
    to_move = "X"

    textX = FONT.render('X TO MOVE', True, (44, 143, 192))
    textRectX = textX.get_rect()
    textRectX.center = (300,100)
    textO = FONT.render('O TO MOVE', True, (223, 0, 39), BG_COLOR)
    textRectO = textO.get_rect()
    textRectO.center = (300,100)
    SCREEN.blit(textX, textRectX)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                SCREEN.fill(BG_COLOR)
                SCREEN.blit(BOARD, (0,200))
                board, to_move = add_XO(board, graphical_board, to_move, X_IMG, O_IMG, SCREEN)
                if to_move=="X":
                    SCREEN.blit(textX, textRectX)
                else:
                    SCREEN.blit(textO, textRectO)
                
        pygame.display.flip()
        