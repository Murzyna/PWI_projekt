import pygame as pg
import numpy as np
from pieces.pawn import *
from pieces.rook import *
from pieces.king import *
from pieces.queen import *
from pieces.bishop import *
from pieces.knight import *


class Piece:

    def __init__(self, color, pos, size):
        self.color = color
        self.pos = pos
        self.size = size

    def draw_piece(self, screen):
        pass
