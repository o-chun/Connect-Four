'''First commit: Skeleton Code'''

import random

class Board:
    def __init__(self):
        pass

    def draw_board(self):
        '''Draws board to terminal'''
        pass

    def check_status(self):
        '''Checks the status of the game:
        Player 1 win, Player 2/Bot win, Tie, or Ongoing'''
        pass

    def insert_piece(self, column_num):
        '''Insert a piece into the supplied column of the board'''
        pass

    def run_turn(self):
        '''Runs one game turn
        - Takes a player or bot move
        - insert_piece()
        - draw_board()
        - check_status()
        '''
        pass

    def change_settings(self):
        '''Asks player for gam settings
        - Face another player or bot
        - Bot difficulty
        - Number of rounds
        - Piece symbols
        '''
        pass

class Bot:
    def __init__(self):
        pass

    def make_move(self):
        '''Makes a move depending on bot's difficulty'''
        pass