Piece Movement Game
This is a Python implementation of a game where pieces ('▲' and '■') move on a board and can jump over each other.

Installation

To use this code, follow these steps:

Clone the repository to your local machine: 
git clone https://MirzaTmr/game.git

Navigate to the repository:
cd game

Run the game.

Usage

This program provides several functions for managing the game board and piece movement:

create_board(n): Creates a new game board with width n.
place_piece(board, p): Places a piece ('▲' or '■') on the board if the original value for that piece is not filled.
check_move(board, starting_square, ending_square): Checks if it's legal to move a piece from one square to another.
move_piece(board, starting_square, ending_square): Moves a piece from one square to another, jumping over other pieces if necessary.
moves(board, player): Finds the first valid move available to a player.
choose_move(board, player): Chooses a move for a player.
To play the game, use these functions to manipulate the board and pieces according to the game rules.

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please open an issue or create a pull request.
