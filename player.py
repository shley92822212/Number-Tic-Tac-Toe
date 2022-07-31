from board import Board
import copy
import random

class Player:
        move_list = None
        p_type = None

        def __init__(self, p_type):
                self.p_type = p_type
                if p_type == "odd":
                        self.move_list = [1, 3, 5, 7, 9]
                elif p_type == "even":
                        self.move_list = [2, 4, 6, 8]

        def player_type(self):
                pass
        def get_move(self, board):
                pass


class Human(Player):
        def player_type(self):
                return self.p_type
        def get_move(self, board):
                row = int(input("Please input a valid row"))
                col = int(input("Please input a valid col"))
                print("Move list", self.move_list)
                number = int(input("Please input a valid number"))
                self.move_list.remove(number)
                return row, col, number
class RandomPlayer(Player):
        def player_type(self):
                return self.p_type
        def get_move(self, board):
                pos_move = []
                for row in range(3):
                        for col in range(3):
                                if board.board[row][col] == 0:
                                        pos_move.append([row, col])
                move = random.choice(pos_move)
                number = random.choice(self.move_list)
                self.move_list.remove(number)
                return move[0], move[1], number



class MiniMax(Player):
        max_depth = 3
        def player_type(self):
                return self.p_type
        def get_move(self, board):
                row, col, number = self.best_move(board)
                self.move_list.remove(number)
                return row, col, number

        def best_move(self, board):

                opponent_move_list = None
                if self.player_type() == "odd":
                        opponent_move_list = [2,4,6,8]
                else:
                        opponent_move_list = [1,3,5,7,9]

                for row in board.board:
                        for col in row:
                                if col in opponent_move_list:
                                        opponent_move_list.remove(col)
                best = [-1, -1, -1, -10000000]
                for row in range(3):
                        for col in range(3):
                                if board.board[row][col] == 0:
                                        for move in self.move_list:
                                                board2 = copy.copy(board)
                                                game_state = board2.make_move(row, col, move)
                                                temp_move_list = self.move_list.copy()
                                                temp_move_list.remove(move)

                                                if game_state == 1:
                                                        score = self.mini_max(board2, False, temp_move_list.copy(), opponent_move_list.copy(), 0)
                                                        if score > best[3]:
                                                                best = [row, col, move, score]
                                                elif game_state == 2:
                                                        return row, col, move
                                                elif game_state == 0:
                                                        continue
                                                else:
                                                        print(self.move_list)
                                                        print("row", row, "col", col, "move", move)
                                                        print(game_state)
                                                        print("Error, something went wrong seleting a move for minimax")
                                                board2.put_move(row, col, 0)
                return best[0], best[1], best[2]

        def mini_max(self, board, my_turn, temp_move_list, opponent_move_list, depth):
                if depth >= self.max_depth:
                        return 0


                return_score = 0
                if my_turn:
                        for row in range(3):
                                for col in range(3):
                                        if board.board[row][col] == 0:
                                                for move in temp_move_list:
                                                        board2 = copy.copy(board)
                                                        game_state = board2.make_move(row, col, move)
                                                        temp_move_list.remove(move)
                                                        if game_state == 1:
                                                                
                                                                return_score = self.max(return_score, self.mini_max(board2, False, temp_move_list.copy(), opponent_move_list.copy(), depth + 1))

                                                        elif game_state == 2:
                                                                return_score = self.max(return_score, 100 - depth)
                                                        elif game_state == 0:
                                                                return_score = self.max(return_score, 0)
                                                        board2.put_move(row, col, 0)
                                                        temp_move_list.append(move)

                else:
                        for row in range(3):
                                for col in range(3):
                                        if board.board[row][col] == 0:
                                                for move in opponent_move_list:
                                                        board2 = copy.copy(board)
                                                        game_state = board2.make_move(row, col, move)
                                                        opponent_move_list.remove(move)
                                                        if game_state == 1:
                                                                return_score = self.min(return_score, self.mini_max(board2, True, temp_move_list.copy(), opponent_move_list.copy(), depth + 1))

                                                        elif game_state == 2:
                                                                return_score = self.min(return_score, -100 + depth)
                                                        elif game_state == 0:
                                                                return_score = self.min(return_score, 0)
                                                        board2.put_move(row, col, 0)
                                                        opponent_move_list.append(move)
                return return_score


        def max(self, a, b):
                if a > b:
                        return a
                return b
        def min(self, a, b):
                if a < b:
                        return a
                return b