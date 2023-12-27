import numpy as np
import pygame as pg
from PWI_projekt.szachy.game.base_piece import *


class Rook(Piece):
    w_image = pg.image.load('assets/pieces/wR.png')
    b_image = pg.image.load('assets/pieces/bR.png')
