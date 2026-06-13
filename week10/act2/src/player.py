class Player:
    """Represents a player in the game."""

    def __init__(self, marker):
        """Initialize a player with a distinct marker.

        Args:
            marker (str): The player's marker ('X' or 'O').
        """
        self.marker = marker

    def get_move(self):
        """Prompt the player to enter their move.

        Returns:
            int: The 0-indexed position on the board, or -1 if input is invalid.
        """
        try:
            user_input = input(f"Player {self.marker}, choose your move (1-9): ")
            return int(user_input) - 1
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")
            return -1
