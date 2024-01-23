import pygame

pygame.init()
WIDTH, HEIGHT = 600, 800
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
BG_COLOR = (245, 233, 200)
FONT = pygame.font.Font("assets/Roboto-Regular.ttf", 100)
X_IMG = pygame.image.load("assets/X.png")
X_IMG = pygame.transform.scale(X_IMG, (50, 50))
O_IMG = pygame.image.load("assets/O2.png")
O_IMG = pygame.transform.scale(O_IMG, (50, 50))
O_IMG.set_colorkey((255,255,255))

board = [[[[1,2,3], [4,5,6], [7,8,9]], [[1,2,3], [4,5,6], [7,8,9]], [[1,2,3], [4,5,6], [7,8,9]]], 
         [[[1,2,3], [4,5,6], [7,8,9]], [[1,2,3], [4,5,6], [7,8,9]], [[1,2,3], [4,5,6], [7,8,9]]], 
         [[[1,2,3], [4,5,6], [7,8,9]], [[1,2,3], [4,5,6], [7,8,9]], [[1,2,3], [4,5,6], [7,8,9]]]]

graphical_board = [[[[[None, None],[None,None],[None,None]], [[None, None],[None,None],[None,None]], [[None, None],[None,None],[None,None]]], [[[None, None],[None,None],[None,None]], [[None, None],[None,None],[None,None]], [[None, None],[None,None],[None,None]]], [[[None, None],[None,None],[None,None]], [[None, None],[None,None],[None,None]], [[None, None],[None,None],[None,None]]]], 
                   [[[[None, None],[None,None],[None,None]], [[None, None],[None,None],[None,None]], [[None, None],[None,None],[None,None]]], [[[None, None],[None,None],[None,None]], [[None, None],[None,None],[None,None]], [[None, None],[None,None],[None,None]]], [[[None, None],[None,None],[None,None]], [[None, None],[None,None],[None,None]], [[None, None],[None,None],[None,None]]]], 
                   [[[[None, None],[None,None],[None,None]], [[None, None],[None,None],[None,None]], [[None, None],[None,None],[None,None]]], [[[None, None],[None,None],[None,None]], [[None, None],[None,None],[None,None]], [[None, None],[None,None],[None,None]]], [[[None, None],[None,None],[None,None]], [[None, None],[None,None],[None,None]], [[None, None],[None,None],[None,None]]]]]