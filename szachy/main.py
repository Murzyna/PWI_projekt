import pygame as pg
import numpy as np
from game.board import *
from game.game import *
from game.options import *
from time import *
from game.dumb_bot import *
from game.smart_bot import *


pg.init()

def main():
    menu = Menu()
    selected_option = menu.run()

    screen_size = 800
    screen = pg.display.set_mode((screen_size, screen_size))
    pg.display.set_caption("Szachy")
    white = (220, 230, 255)
    brown = (205, 133, 63)
    board = ChessBoard(screen_size, (white, brown), screen)



    if selected_option == "Player vs Player":

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




    elif "Player vs Bot" in selected_option:

        if "Dumb" in selected_option:

            if "White" in selected_option:
                bot = DumbBot("b", board)

            else:
                bot = DumbBot("w", board)

        else:
            if "White" in selected_option:
                bot = SmartBot("b", board)

            else:
                bot = SmartBot("w", board)


        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    break



            # Bot's turn
            if board.turn == bot.color:
                if "Dumb" in selected_option:
                    bot_move = bot.get_random_move(board.board)

                elif "Smart" in selected_option:
                    bot_move = bot.get_smart_move(board.board)



                if bot_move != None:
                    screen.fill((0, 0, 0))
                    board.draw_board()

                    start_pos, end_pos = bot_move

                    board.move_piece_bot(start_pos, end_pos)
                    board.draw_pieces()

                    pg.display.flip()




            # Player's turn
            else:
                screen.fill((0, 0, 0))
                board.draw_board()
                highlight(screen)
                board.move_piece()
                board.draw_pieces()

                pg.display.flip()


if __name__ == "__main__":
    main()
