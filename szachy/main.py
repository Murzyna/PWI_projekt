import pygame as pg
import numpy as np
from game.board import *
from game.game import *
from game.options import Menu


pg.init()

def main():
    menu = Menu()
    selected_option = menu.run()

    if selected_option == "Player vs Player":

        screen_size = 800
        screen = pg.display.set_mode((screen_size, screen_size))
        pg.display.set_caption("Szachy")
        white = (220, 230, 255)
        brown = (205, 133, 63)
        board = ChessBoard(screen_size, (white, brown), screen)




        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    break

            screen.fill((0, 0, 0))
            board.draw_board()
            highlight(screen)
            board.move_piece()
            board.draw_pieces()

            pg.display.flip()




    elif (selected_option == "Bot vs Bot" or selected_option == "Player vs Bot - White - Dumb Bot"      #Nie działa dla tych opcji
        or selected_option == "Player vs Bot - White - Smart Bot"
        or selected_option == "Player vs Bot - Black - Dumb Bot"
        or selected_option == "Player vs Bot - White - Dumb Bot"):

        print(selected_option)

if __name__ == "__main__":
    main()
