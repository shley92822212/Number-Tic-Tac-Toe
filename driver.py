from board import Board
from player import Player
from player import Human
from player import MiniMax
from player import RandomPlayer
from number_tic_tac_toe import NumberTicTacToe

def main():
        player1 = None
        player2 = None
        user_input = input("Odd player ai or human? (a/h/r)").lower()
        if user_input == "a":
                player1 = MiniMax("odd")
        elif user_input == "h":
                player1 = Human("odd")
        elif user_input == "r":
                player1 = RandomPlayer("odd")
        else:
                print("something went wrong selecting a player")
        user_input = input("Even player ai or human? (a/h/r)").lower()
        if user_input == "a":
                player2 = MiniMax("even")
        elif user_input == "h":
                player2 = Human("even")
        elif user_input == "r":
                player2 = RandomPlayer("even")
        else:
                print("something went wrong selecting a player")
        board = Board()
        game = NumberTicTacToe(player1, player2, board)
        game.play()

if __name__ == '__main__':
        main()