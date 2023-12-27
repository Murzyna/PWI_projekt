import pygame as pg
import numpy as np
from game.board import *

pg.init()

screen_size = 800

screen = pg.display.set_mode((screen_size, screen_size))
pg.display.set_caption("Szachy")
white = (220, 230, 255)
brown = (135, 206, 250)
board = ChessBoard(screen_size, (white, brown), screen)


def main():

    board.draw_board()
    board.draw_pieces()


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
    screen.fill((0, 0, 0))

    main()

    pg.display.flip()
