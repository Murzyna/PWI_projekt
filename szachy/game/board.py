import pygame as pg
import numpy as np
from pieces.pawn import *
from pieces.rook import *
from pieces.king import *
from pieces.queen import *
from pieces.bishop import *
from pieces.knight import *



class ChessBoard:

    board = np.zeros((8,8), classmethod)

    def __init__(self, size, colors, screen):
        self.size = size
        self.color1 = colors[0]
        self.color2 = colors[1]
        self.screen = screen
        self.square_size = screen.get_width()//8

    def draw_board(self):
        for i in range(8):
            for j in range(8):
                if (i+j)%2 == 0:
                    pg.draw.rect(self.screen, self.color1, (i*self.square_size, j*self.square_size, self.square_size, self.square_size))
                else:
                    pg.draw.rect(self.screen, self.color2, (i * self.square_size, j * self.square_size, self.square_size, self.square_size))
