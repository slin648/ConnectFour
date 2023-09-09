# Connect Four Game in Python

## Overview
This project is a text-based implementation of the classic board game, Connect Four. Players take turns to drop a disk into one of the columns in a 6x7 grid. The objective is to connect four of one's own discs in a row, either vertically, horizontally, or diagonally, before the opponent does.

## Features
- A simple text-based interface for gameplay.
- Ability to choose from seven columns to drop the disk.
- Checks for horizontal, vertical, and diagonal wins.
- Automatic detection of invalid or out-of-bounds input with error messages.
- The game loop continues until there's a winner or the board is full.

## How to Play
1. Run the program.
2. Players take turns to input a number between 0-6, representing the column where they wish to drop their disk.
3. The board updates after every move, showing the current state.
4. The game announces the winner once a winning move is detected.

### Note
Ensure your inputs are integers between 0 and 6. Incorrect inputs will prompt you to restart the game.
