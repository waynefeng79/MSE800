class Board:
    """Represents the Tic-Tac-Toe game board."""

    def __init__(self):
        """Initialize an empty 3x3 board."""
        self.cells = [" "] * 9

    def display(self):
        """Render the current state of the board to the CLI."""
        print("\n")
        print(f" {self.cells[0]} | {self.cells[1]} | {self.cells[2]} ")
        print("---|---|---")
        print(f" {self.cells[3]} | {self.cells[4]} | {self.cells[5]} ")
        print("---|---|---")
        print(f" {self.cells[6]} | {self.cells[7]} | {self.cells[8]} ")
        print("\n")

    def is_position_free(self, position):
        """Check if a specific board cell is available.

        Args:
            position (int): The 0-indexed position on the board.

        Returns:
            bool: True if the position is free, False otherwise.
        """
        return self.cells[position] == " "

    def update(self, position, marker):
        """Place a player's marker on the board.

        Args:
            position (int): The 0-indexed position on the board.
            marker (str): The player's marker ('X' or 'O').
        """
        self.cells[position] = marker

    def is_full(self):
        """Check if all positions on the board are filled.

        Returns:
            bool: True if no empty spaces remain, False otherwise.
        """
        return " " not in self.cells

    def check_win(self, marker):
        """Check if the given marker has achieved a winning combination.

        Args:
            marker (str): The player's marker ('X' or 'O').

        Returns:
            bool: True if the marker won, False otherwise.
        """
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]
        for condition in win_conditions:
            if (self.cells[condition[0]] == self.cells[condition[1]] ==
                    self.cells[condition[2]] == marker):
                return True
        return False
