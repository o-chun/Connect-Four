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
        self.draw_board()

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
            # right
            for i in range(4, 7, 1):
                if self.data[row_num][i] == self.turn_symbol:
                    in_a_row += 1
                else:
                    break
            # left
            for j in range(2, -1, -1):
                if self.data[row_num][j] == self.turn_symbol:
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
                if self.data[x][col_num] == self.turn_symbol:
                    in_a_row += 1
                else:
                    break
            if in_a_row >= 4:
                self.status = 'win'
            else:
                in_a_row = 1
        # Check diagonals
        # \
        if self.status == 'ongoing':
            # up left
            up = row_num - 1
            left = col_num - 1
            while up >= 0 and left >= 0:
                if self.data[up][left] == self.turn_symbol:
                    in_a_row += 1
                    up -= 1
                    left -= 1
                else:
                    break
            # down right
            down = row_num + 1
            right = col_num + 1
            while down <= 5 and right <= 6:
                if self.data[down][right] == self.turn_symbol:
                    in_a_row += 1
                    down += 1
                    right += 1
                else:
                    break
            if in_a_row >= 4:
                self.status = 'win'
            else:
                in_a_row = 1
        # /
        if self.status == 'ongoing':
            # up right
            up = row_num - 1
            right = col_num + 1
            while up >= 0 and right <= 6:
                if self.data[up][right] == self.turn_symbol:
                    in_a_row += 1
                    up -= 1
                    right += 1
                else:
                    break
            # down left
            down = row_num + 1
            left = col_num - 1
            while down <= 5 and left >= 0:
                if self.data[down][left] == self.turn_symbol:
                    in_a_row += 1
                    down += 1
                    left -= 1
                else:
                    break
            if in_a_row >= 4:
                self.status = 'win'
            else:
                in_a_row = 1
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
        p_num = 0
        if self.turn_symbol == self.p1_symbol:
            p_num = 1
        else:
            p_num = 2
        print("Player", p_num)
        while True:
            move = int(input("Enter your next move: (# 0-6)\n"))
            if move < 0 or move > 6:
                print("Invalid column number.")
            elif self.is_column_open(move):
                self.insert_piece(move)
                break
            else:
                print("Column full. Enter a different move.")
        self.draw_board()
        self.check_status()

    def set_settings(self):
        '''Asks player for game settings
        - Face another player or bot
        - Bot difficulty
        - Number of rounds
        - Piece symbols
        '''
        pass



class Player:
    def __init__(self) -> None:
        pass

    def make_move(self):
        pass

class Human(Player):
    def __init__(self):
        super().__init__()

    def make_move(self):
        pass

class Bot(Player):
    def __init__(self):
        super().__init__()

    def make_move(self):
        '''Makes a move depending on bot's difficulty'''
        pass