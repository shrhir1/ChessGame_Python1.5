# Chess Game

## Overview
This program allows users to input a chess piece and its position on the board to see all its possible valid moves. The board is displayed in the console, and valid move positions are marked.

## Features
- Supports **King, Queen, Rook, Bishop, and Knight**.
- Displays an 8x8 chessboard with move positions.
- Takes user input for a chess piece and its position.
- Prints possible moves directly onto the board.
- Allows the user to keep entering pieces or exit the program.

## How to Use
1. Run the program.
2. Enter a chess piece and its position in the format:

- Example: `Qd4` (Queen at d4) or `Nf3` (Knight at f3).
3. The program will display the board with valid move positions marked as `x`.
4. Enter another piece or type `X` to exit.

## Supported Pieces
| Piece | Symbol | Movement |
|--------|--------|-----------|
| King | `K` | One square in any direction |
| Queen | `Q` | Any number of squares vertically, horizontally, or diagonally |
| Rook | `R` | Any number of squares vertically or horizontally |
| Bishop | `B` | Any number of squares diagonally |
| Knight | `N` | Moves in "L" shape (2 squares in one direction, then 1 perpendicular) |

## Running the Program
To run the program, simply execute:
```bash
python chess.py
