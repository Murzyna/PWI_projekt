import numpy as np
import pygame as pg
from PWI_projekt.szachy.game.base_piece import *


class Bishop(Piece):
    w_image = pg.image.load('assets/pieces/wB.png')
    b_image = pg.image.load('assets/pieces/bB.png')

    #def can_move(self, new_pos):