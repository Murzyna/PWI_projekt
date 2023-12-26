import numpy as np
import pygame as pg
from PWI_projekt.szachy.game.base_piece import *


class Queen(Piece):
    w_image = pg.image.load('assets/pieces/wQ.png')
    b_image = pg.image.load('assets/pieces/bQ.png')
