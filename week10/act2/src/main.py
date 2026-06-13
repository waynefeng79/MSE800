"""A command-line interface (CLI) Object-Oriented Tic-Tac-Toe game.

This module implements Tic-Tac-Toe using Object-Oriented Programming (OOP)
principles, ensuring strict compliance with PEP 8 and Pylint standards.
"""

from board import Board
from player import Player

class TicTacToeGame:
    """Manages the gameplay logic and flow."""

    def __init__(self):
        """Set up the board and the two players."""
        self.board = Board()
        self.player_x = Player("X")
        self.player_o = Player("O")
        self.current_player = self.player_x

    @staticmethod
    def display_instructions():
        """Print the initial setup instructions and grid layout."""
        print("Welcome to Object-Oriented CLI Tic-Tac-Toe!")
        print("Positions are numbered 1 through 9 as follows:")
        print(" 1 | 2 | 3 ")
        print("---|---|---")
        print(" 4 | 5 | 6 ")
        print("---|---|---")
        print(" 7 | 8 | 9 ")

    def switch_player(self):
        """Alternate the active player turn."""
        if self.current_player == self.player_x:
            self.current_player = self.player_o
        else:
            self.current_player = self.player_x

    def handle_turn(self):
        """Process a single turn for the current player.

        Returns:
            int: A valid 0-indexed move position.
        """
        while True:
            move = self.current_player.get_move()

            if move < 0 or move > 8:
                print("Out of bounds! Choose a position between 1 and 9.")
                continue

            if not self.board.is_position_free(move):
                print("That spot is already taken! Try again.")
                continue

            return move

    def play(self):
        """Start and run the core game loop."""
        self.display_instructions()

        while True:
            self.board.display()
            move = self.handle_turn()

            # Execute move
            self.board.update(move, self.current_player.marker)

            # Check game over states
            if self.board.check_win(self.current_player.marker):
                self.board.display()
                print(f"🎉 Congratulations! Player {self.current_player.marker} wins! 🎉")
                break

            if self.board.is_full():
                self.board.display()
                print("🤝 It's a tie game!")
                break

            self.switch_player()


if __name__ == "__main__":
    game = TicTacToeGame()
    game.play()
