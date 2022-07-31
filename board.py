class Board:
        board = [[0,0,0], [0,0,0], [0,0,0]]
        save_board = None

        def __init__(self):
                pass
        def is_valid_move(self, row, col, number):
                if self.board[row][col] is not 0:
                        return False                      

                for r in self.board:
                        for c in r:
                                if c == number:
                                        return False
                return True

        def game_status(self):
                empty_space = False
                for row in self.board:
                        for col in row:
                                if col == 0:
                                        empty_space = True
                #check down/across
                for i in range(3):
                        if self.board[i][0] is not 0 and self.board[i][1] is not 0 and self.board[i][2] is not 0:
                                if self.board[i][0] + self.board[i][1] + self.board[i][2] == 15:
                                        # two for win
                                        return 2
                        if self.board[0][i] is not 0 and self.board[1][i] is not 0 and self.board[2][i] is not 0:
                                if self.board[0][i] + self.board[1][i] + self.board[2][i] == 15:
                                        return 2
                #check diagonal left to right
                if self.board[0][0] is not 0 and self.board[1][1] is not 0 and self.board[2][2] is not 0:
                        if self.board[0][0] + self.board[1][1] + self.board[2][2] == 15:
                                        return 2
                if self.board[0][2] is not 0 and self.board[1][1] is not 0 and self.board[2][0] is not 0:
                        if self.board[0][2] + self.board[1][1] + self.board[2][0] == 15:
                                        return 2

                # if no one won and there are no empty spaces left on the board it is a draw
                if not empty_space:
                        # 0 for draw
                        return 0
                else:
                        # 1 for continue
                        return 1


        def make_move(self, row, col, number):
                if(self.is_valid_move(row, col, number)):
                        self.board[row][col] = number
                        return self.game_status()
                # 4 for invalid move
                return 4
        def put_move(self, row, col, number):
                self.board[row][col] = number

        def display_board(self):
                print(self.board[0])
                print(self.board[1])
                print(self.board[2])
                print()

        def simulating(self, b):
                if b:
                        self.save_board = self.board
                else:
                        self.board = self.save_board



