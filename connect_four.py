'''Second commit: At least one feature'''

import random

class Board:
    def __init__(self, starter = True, p1_sym = 'X', p2_sym = 'O'):
        self.data = [[' ' for j in range(7)] for i in range(6)]
        self.did_p1_start = starter
        self.p1_symbol = p1_sym
        self.p2_symbol = p2_sym
        if self.did_p1_start:
            self.turn_symbol = self.p1_symbol
        else:
            self.turn_symbol = self.p2_symbol
        self.status = 'ongoing'

    def draw_board(self):
        '''Draws board to terminal'''
        for row in self.data:
            print('|'+'|'.join(row)+'|')
        print(' 0 1 2 3 4 5 6')

    def check_status(self,col_num):
        '''Checks the status of the game:
            Player 1 win, Player 2/Bot win, Tie, or Ongoing
        Input the column number of the last played piece'''
        in_a_row = 1
        row_num = self.find_open_row(col_num) + 1
        # Check horizontal
        if self.data[row_num][3] == self.turn_symbol:
            for i in range(4, 7, 1):
                if self.data[row_num][3] == self.data[row_num][i]:
                    in_a_row += 1
                else:
                    break
            for j in range(2, -1, -1):
                if self.data[row_num][3] == self.data[row_num][j]:
                    in_a_row += 1
                else:
                    break
            if in_a_row >= 4:
                self.status = 'win'
            else:
                in_a_row = 1
        # Check vertical
        if self.find_open_row(col_num) < 2 and self.status == 'ongoing':
            for x in range(row_num+1, 6, 1):
                if self.data[row_num][col_num] == self.data[x][col_num]:
                    in_a_row += 1
                else:
                    break
            if in_a_row >= 4:
                self.status = 'win'
            else:
                in_a_row = 1
        # Check diagnols
        # Check tie
        if self.status == 'ongoing' and not ' ' in self.data[0]:
            self.status = 'tie'

    def is_column_open(self, col_num):
        return self.data[0][col_num] == ' '

    def find_open_row(self, col_num):
        '''Finds the lowest open row in the column'''
        for i in range(5,-1,-1):
            if self.data[i][col_num] == ' ':
                return i
        return -1

    def insert_piece(self, col_num):
        '''Insert a piece into the supplied column of the board'''
        self.data[self.find_open_row(col_num)][col_num] = self.turn_symbol

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