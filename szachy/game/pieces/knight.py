import numpy as np
import pygame as pg
from PWI_projekt.szachy.game.base_piece import *


class Knight(Piece):
    w_image = pg.image.load('assets/pieces/wN.png')
    b_image = pg.image.load('assets/pieces/bN.png')
