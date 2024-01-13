import pygame
import math
import time, sys
from variables import SCREEN, O_IMG, X_IMG

#list that specifies whether you can put any more X's or O's to the specific sub_board, it states False if there is a winner there or a draw
is_playable = [[True, True, True], [True, True, True], [True, True, True]]

is_draw = [[False, False, False], [False, False, False], [False, False, False]]

small_board_wins = [[None, None, None], [None, None, None], [None, None, None]]


def check_small_win(board, small_board_coords):
    # 'small_board_coords' variable is a tuple (main_board_x - 1, main_board_y - 1)

    for i in range(3):
    #same verse
        if board[small_board_coords[1]][small_board_coords[0]][i][0] == \
           board[small_board_coords[1]][small_board_coords[0]][i][1] == \
           board[small_board_coords[1]][small_board_coords[0]][i][2]:
            small_board_wins[small_board_coords[1]][small_board_coords[0]] = \
            board[small_board_coords[1]][small_board_coords[0]][i][0]
            return True

    for j in range(3):
    #same column
        if board[small_board_coords[1]][small_board_coords[0]][0][j] == \
           board[small_board_coords[1]][small_board_coords[0]][1][j] == \
           board[small_board_coords[1]][small_board_coords[0]][2][j]:
            small_board_wins[small_board_coords[1]][small_board_coords[0]] = \
            board[small_board_coords[1]][small_board_coords[0]][0][j]
            return True

    #diagonal
    if (board[small_board_coords[1]][small_board_coords[0]][0][0] ==
       board[small_board_coords[1]][small_board_coords[0]][1][1] ==
       board[small_board_coords[1]][small_board_coords[0]][2][2]) or \
       (board[small_board_coords[1]][small_board_coords[0]][0][2] ==
       board[small_board_coords[1]][small_board_coords[0]][1][1] ==
       board[small_board_coords[1]][small_board_coords[0]][2][0]):
        small_board_wins[small_board_coords[1]][small_board_coords[0]] = \
        board[small_board_coords[1]][small_board_coords[0]][1][1]
        return True

    return False
    

def winning_text(text, color):
    background = pygame.Surface((600,800))
    background.set_alpha(200)
    background.fill((245, 233, 200))
    SCREEN.blit(background, (0,0))

    FONT = pygame.font.SysFont("georgia", 60, False, True)
    win_text = FONT.render(text, True, color)
    wint_text_rec = win_text.get_rect()
    wint_text_rec.center = (300,400)
    SCREEN.blit(win_text, wint_text_rec)
    pygame.display.update()
    time.sleep(2)


def small_win_board_change():
    for i in range(3):
        for j in range(3):
        
            if small_board_wins[j][i] is None:
                continue

            elif small_board_wins[j][i] == 'X':
                X_IMG = pygame.image.load("SuperTicTacToe/assets/X.png")
                X_IMG = pygame.transform.scale(X_IMG, (190, 190))

                draw_rect = pygame.Surface((190, 190))
                draw_rect.set_alpha(200)
                draw_rect.fill((245, 233, 200))

                SCREEN.blit(draw_rect, (i * 200 + 6, j * 200 + 200 + 5))
                SCREEN.blit(X_IMG, (i * 200 + 5, j * 200 + 200 + 4))

            else:
                O_IMG = pygame.image.load("SuperTicTacToe/assets/O2.png")
                O_IMG = pygame.transform.scale(O_IMG, (190, 190))
                O_IMG.set_colorkey((255, 255, 255))

                draw_rect = pygame.Surface((190, 190))
                draw_rect.set_alpha(200)
                draw_rect.fill((245, 233, 200))

                SCREEN.blit(draw_rect, (i * 200 + 6, j * 200 + 200 + 5))
                SCREEN.blit(O_IMG, (i * 200 + 5, j * 200 + 200 + 4))
                

def check_major_win(small_board_wins):
    for i in range(3):
        if small_board_wins[i][0] == small_board_wins[i][1] == small_board_wins[i][2]:
            winner = small_board_wins[i][0]
            if winner is None: continue
            return winner

    for j in range(3):
        if small_board_wins[0][j] == small_board_wins[1][j] == small_board_wins[2][j]:
            winner = small_board_wins[0][j]
            if winner is None: continue
            return winner

    if (small_board_wins[0][0] == small_board_wins[1][1] == small_board_wins[2][2]) or \
       (small_board_wins[0][2] == small_board_wins[1][1] == small_board_wins[2][0]):
        winner = small_board_wins[1][1]
        if winner is None: return 'None'
        return winner

    return 'None'
    

def check_draw(board, small_board_coords):
    for i in range(3):
        for j in range(3):
            if board[small_board_coords[1]][small_board_coords[0]][i][j]!="X" and board[small_board_coords[1]][small_board_coords[0]][i][j]!="O":
                return False
    return True


def mark_draws(board):
    for i in range(3):
        for j in range(3):
            if is_draw[j][i]:
                draw_rect = pygame.Surface((180, 180))
                draw_rect.set_alpha(80)
                draw_rect.fill((255,0,0))
                SCREEN.blit(draw_rect, ((i)*200 + 10, (j)*200+200 + 10))
                is_playable[j][i]=False


def render_board(board, graphical_board, next_move):
    for m_y in range(3):
        for m_x in range(3):
            
            if small_board_wins[m_y][m_x] is not None:
                continue
                
            for s_y in range(3):
                for s_x in range(3):
                    if board[m_y][m_x][s_y][s_x]=="X":
                        graphical_board[m_y][m_x][s_y][s_x][0] = X_IMG
                        graphical_board[m_y][m_x][s_y][s_x][1] = X_IMG.get_rect(center = (m_x*200 + (s_x/3)*200 + (1/6)*200, m_y*200 + (s_y/3)*200 + (1/6)*200 + 200))
                    elif board[m_y][m_x][s_y][s_x]=="O":
                        graphical_board[m_y][m_x][s_y][s_x][0] = O_IMG
                        graphical_board[m_y][m_x][s_y][s_x][1] = O_IMG.get_rect(center = (m_x*200 + (s_x/3)*200 + (1/6)*200, m_y*200 + (s_y/3)*200 + (1/6)*200 + 200))
    if next_move[0] is not None:
        next_move_rect = pygame.Surface((180, 180))
        next_move_rect.set_alpha(80)
        next_move_rect.fill((0,255,0))
        SCREEN.blit(next_move_rect, (next_move[0]*200 + 10, next_move[1]*200+200 + 10))


def add_XO(board, graphical_board, to_move, next_move): 
#function that gets mouse input to place an X or O on the chosen spot
    current_pos = pygame.mouse.get_pos()
    main_board_x = math.floor(current_pos[0]/200)+1
    main_board_y = math.floor((current_pos[1]-200)/200)+1
    sub_board_x = math.floor((current_pos[0]%200)/(200/3))+1
    sub_board_y = math.floor(((current_pos[1]-200)%200)/(200/3))+1
    if main_board_x>0 and main_board_y>0:

        if board[main_board_y-1][main_board_x-1][sub_board_y-1][sub_board_x-1] != 'X' \
            and board[main_board_y-1][main_board_x-1][sub_board_y-1][sub_board_x-1] != 'O'\
            and is_playable[main_board_y-1][main_board_x-1] and ((main_board_x-1 == next_move[0] and main_board_y-1 == next_move[1]) or next_move[0] is None):

            board[main_board_y-1][main_board_x-1][sub_board_y-1][sub_board_x-1]=to_move

            if to_move == "X": to_move = "O"
            else: to_move = "X"

            if is_playable[sub_board_y-1][sub_board_x-1]:
                next_move = (sub_board_x-1, sub_board_y-1)
            else:
                next_move = (None, None)

            if check_small_win(board, (main_board_x - 1, main_board_y - 1)):
                is_playable[main_board_y - 1][main_board_x - 1] = False
                sub_winner = small_board_wins[main_board_y - 1][main_board_x - 1]
                win_text = f'{sub_winner} WON THIS FIELD!'
                screen_look = SCREEN.copy()
                if sub_winner == 'X':
                    color = (44, 143, 192)
                else:
                    color = (223, 0, 39)
                winning_text(win_text, color)
                SCREEN.blit(screen_look, (0, 0))
                pygame.display.update()
                next_move = (None, None)
            
            if check_major_win(small_board_wins) != 'None':
                winner = check_major_win(small_board_wins)
                win_text = f'{winner} WON THIS GAME!'
                screen_look = SCREEN.copy()
                SCREEN.blit(screen_look, (0, 0))
                if winner == 'X':
                    color = (44, 143, 192)
                else:
                    color = (223, 0, 39)
                winning_text(win_text, color)
                SCREEN.blit(screen_look, (0, 0))

                winning_text('CONGRATS!', color)
                pygame.display.update()
                pygame.quit()
                sys.exit()            
            
            if check_draw(board, (main_board_x - 1, main_board_y - 1)) and \
               not(check_small_win(board, (main_board_x - 1, main_board_y - 1))):
                is_draw[main_board_y - 1][main_board_x - 1] = True
                next_move = (None, None)

        #adding new X or O to the graphical_board
        render_board(board, graphical_board, next_move)
        
        #bliting the board to the screen:
        for m_y in range(3):
            for m_x in range(3):
            
                if small_board_wins[m_y][m_x] is not None:
                    continue
                    
                for s_y in range(3):
                    for s_x in range(3):
                        if graphical_board[m_y][m_x][s_y][s_x][0] is not None:
                            SCREEN.blit(graphical_board[m_y][m_x][s_y][s_x][0], graphical_board[m_y][m_x][s_y][s_x][1])
        
    return board, to_move, next_move