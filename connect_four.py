import random

# ----- Player Classes -----
class Player:
    def __init__(self, nam, sym):
        self.name = nam
        self.symbol = sym

    def print_info(self):
        print('\tName:', self.name)
        print('\tSymbol:', self.symbol)

class Human(Player):
    def __init__(self, nam = 'Player 1', sym = 'X'):
        super().__init__(nam, sym)

    def print_info(self):
        print('\tType: User')
        super().print_info()

    def make_move(self, my_board):
        while True:
            move = int(input("Enter your next move: (# 0-6)\n"))
            if move < 0 or move > 6:
                print("Invalid column number.")
            elif my_board.is_column_open(move):
                my_board.insert_piece(move)
                break
            else:
                print("Column full. Enter a different move.")
        return move

# ----- Bot Classes -----
class Bot(Player):
    def __init__(self, nam = 'Player 2', sym = 'O'):
        super().__init__(nam, sym)
        self.bad_cols = []

    def print_info(self, dif):
        print('\tType: Bot')
        print('\tDifficulty:', dif)
        super().print_info()

    def could_win(self):
        pass

class Easy(Bot):
    def __init__(self, nam = 'Easy Bot', sym = 'O'):
        super().__init__(nam, sym)

    def print_info(self):
        super().print_info('Easy')

    def make_move(self, my_board):
        while True:
            move = random.randint(0,6)
            if my_board.is_column_open(move):
                print(move)
                my_board.insert_piece(move)
                break
        return move

class Normal(Bot):
    def __init__(self, nam = 'Normal Bot', sym = 'O'):
        super().__init__(nam, sym)

    def print_info(self):
        super().print_info('Normal')

    def make_move(self, my_board):
        moves = [0, 1, 2, 3, 4, 5, 6]

class Hard(Bot):
    def __init__(self, nam = 'Hard Bot', sym = 'O'):
        super().__init__(nam, sym)

    def print_info(self):
        super().print_info('Hard')

    def make_move(self, my_board):
        moves = [0, 1, 2, 3, 4, 5, 6]

# ----- Game Board Class -----
class Board:
    def __init__(self, starter = True):
        self.data = [[' ' for j in range(7)] for i in range(6)]
        self.did_p1_start = starter
        self.player1 = Human()
        self.player2 = Easy()
        self.set_settings()
        self.current = self.player1
        self.status = 'ongoing'
        self.draw_board()
        self.turn_num = 1

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
        if self.data[row_num][3] == self.current.symbol:
            # right
            for i in range(4, 7, 1):
                if self.data[row_num][i] == self.current.symbol:
                    in_a_row += 1
                else:
                    break
            # left
            for j in range(2, -1, -1):
                if self.data[row_num][j] == self.current.symbol:
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
                if self.data[x][col_num] == self.current.symbol:
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
                if self.data[up][left] == self.current.symbol:
                    in_a_row += 1
                    up -= 1
                    left -= 1
                else:
                    break
            # down right
            down = row_num + 1
            right = col_num + 1
            while down <= 5 and right <= 6:
                if self.data[down][right] == self.current.symbol:
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
                if self.data[up][right] == self.current.symbol:
                    in_a_row += 1
                    up -= 1
                    right += 1
                else:
                    break
            # down left
            down = row_num + 1
            left = col_num - 1
            while down <= 5 and left >= 0:
                if self.data[down][left] == self.current.symbol:
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
        self.data[self.find_open_row(col_num)][col_num] = self.current.symbol

    def run_turn(self):
        '''Runs one game turn'''
        print('Turn', self.turn_num)
        print(self.current.name)
        move = self.current.make_move(self)
        self.draw_board()
        self.check_status(move)
        self.turn_num += 1

    def set_settings(self):
        '''Asks player for game settings
        - Face another player or bot
        - Bot difficulty
        - Number of rounds
        - Piece symbols
        '''
        change = 'yes'
        while not (change == 'no' or change == 'n'):
            print('Player 1: ')
            self.player1.print_info()
            print('\nPlayer 2: ')
            self.player2.print_info()
            change = input("Would you like to change these settings? (y/n): ").lower()
            if not (change == 'no' or change == 'n'):
                '''change_p = input("Which player would you like to change? (1/2): ")
                if change_p == '1':
                    c_p = self.player1
                else:
                    c_p = self.player2'''
                human_or_bot = input("Pick a mode (1/2/3):\n1. User vs User\n2. User vs Bot\n3. Bot vs Bot\n")
                if human_or_bot == '1':
                    self.player1 = Human()
                    self.player2 = Human('Player 2', 'O')
                elif human_or_bot == '2':
                    self.player1 = Human()
                    self.player2 = Easy('Bot', 'O')
                else:
                    self.player1 = Easy('Bot 1', 'X')
                    self.player2 = Easy('Bot 2', 'O')
            
    def run_game(self):
        '''Run a full game'''
        while True:
            self.run_turn()
            print()
            if self.status == 'ongoing':
                if self.current == self.player1:
                    self.current = self.player2
                else:
                    self.current = self.player1
            else:
                break
        if self.status == 'win':
            print(self.current.name + " WINS!")
        else:
            print("TIE!")


# run game
my_game = Board()
my_game.run_game()