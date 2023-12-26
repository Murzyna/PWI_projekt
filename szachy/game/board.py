import numpy as np


class ChessBoard:

    board = np.zeros((8,8))

    def __init__(self, size, colors):
        self.size = size
        self.color1 = colors[0]
        self.color2 = colors[1]
