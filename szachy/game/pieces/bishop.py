import numpy as np
import pygame as pg
from PWI_projekt.szachy.game.base_piece import *


class Bishop(Piece):
    w_image = pg.image.load('assets/pieces/wB.png')
    b_image = pg.image.load('assets/pieces/bB.png')

    def possible_moves(self, board):
        x = self.pos[1]
        y = self.pos[0]



