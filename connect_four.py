'''Second commit: At least one feature'''

import random

class Board:
    def __init__(self, starter = True, p1_sym = 'X', p2_sym = 'O'):
        self.board_data = [[' ' for j in range(7)] for i in range(6)]
        self.did_p1_start = starter
        self.is_p1_turn = self.did_p1_start
        self.p1_symbol = p1_sym
        self.p2_symbol = p2_sym

    def draw_board(self):
        '''Draws board to terminal'''
        for row in self.board_data:
            print('|'.join(row))
            #print('-' * 13)
        print('0 1 2 3 4 5 6')

    def check_status(self):
        '''Checks the status of the game:
        Player 1 win, Player 2/Bot win, Tie, or Ongoing'''
        pass
    
    def is_column_open(self, col_num):
        return self.board_data[0][col_num] != ' '

    def find_open_row(self, col_num):
        '''Finds the lowest open row in the column'''
        for i in range(5,-1,-1):
            if self.board_data[i][col_num] == ' ':
                return i

    def insert_piece(self, col_num):
        '''Insert a piece into the supplied column of the board'''
        if self.is_p1_turn:
            piece = self.p1_symbol
        else:
            piece = self.p2_symbol
        self.board_data[self.find_open_row(col_num)][col_num] = piece

    def run_turn(self):
        '''Runs one game turn
        - Takes a player or bot move
        - is_column_open()
        - insert_piece()
        - draw_board()
        - check_status()
        '''
        pass

    def change_settings(self):
        '''Asks player for game settings
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