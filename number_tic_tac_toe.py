from board import Board
from player import Player
from player import Human
from player import MiniMax
import copy

class NumberTicTacToe:
        player1 = None
        player2 = None
        board = None
        p1_turn = False


        def __init__(self, player1, player2, board):
                self.player1 = player1
                self.player2 = player2
                self.board = board

        def play(self):
                game_status = self.board.game_status()
                player = self.player2
                while game_status == 1:
                        if self.p1_turn:
                                self.p1_turn = False
                                player = self.player2
                        else:
                                self.p1_turn = True
                                player = self.player1
                        print(player.player_type(), "turn")
                        self.board.display_board()
                        while True:
                                row, col, number = player.get_move(copy.copy(self.board))
                                game_status = self.board.make_move(row, col, number)
                                if game_status is not 3:
                                        break
                print("Game over!")
                self.board.display_board()

                
                if game_status == 0:
                        print("The game was a draw!")
                else:
                        print("Congratulations", player.player_type(), "you win!")

