import numpy as np
import pygame as pg
from PWI_projekt.szachy.game.base_piece import *


class Pawn(Piece):
    w_image = pg.image.load('assets/pieces/wP.png')
    b_image = pg.image.load('assets/pieces/bP.png')

    def possible_moves_f(self, board):
        pass