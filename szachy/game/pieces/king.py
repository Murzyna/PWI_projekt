import numpy as np
import pygame as pg
from PWI_projekt.szachy.game.base_piece import *


class King(Piece):
    w_image = pg.image.load('assets/pieces/wK.png')
    b_image = pg.image.load('assets/pieces/bK.png')

    def possible_moves_f(self, board):
        pass
