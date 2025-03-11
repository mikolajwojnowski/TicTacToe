# Tic-Tac-Toe with Minimax Algorithm and Pygame GUI

![Tic-Tac-Toe](https://img.shields.io/badge/Game-TicTacToe-blue)
![Python](https://img.shields.io/badge/Language-Python-green)
![Minimax](https://img.shields.io/badge/Algorithm-Minimax-orange)
![Pygame](https://img.shields.io/badge/GUI-Pygame-red)

A Python implementation of the classic Tic-Tac-Toe game, featuring an AI opponent that uses the **Minimax algorithm** to make optimal moves in adversarial scenarios. The game includes a **Pygame-based GUI** for an interactive and visually appealing experience.

---

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [How It Works](#how-it-works)
- [Installation](#installation)



---

## Overview

This project is a Python implementation of Tic-Tac-Toe where:
- The game is played on a 3x3 grid.
- The player can choose to play as **X** or **O**.
- The AI opponent uses the **Minimax algorithm** to make optimal moves, ensuring it never loses (it either wins or forces a draw).
- The game features a **Pygame-based GUI** for an interactive and visually appealing experience.

The Minimax algorithm is a decision-making strategy used in two-player games. It evaluates all possible moves, assuming the opponent will also play optimally, and chooses the move that maximizes the player's chances of winning while minimizing the opponent's chances.

---

## Features

- **Interactive Gameplay**: Play against an AI opponent with a graphical interface.
- **Minimax Algorithm**: The AI uses the Minimax algorithm to make optimal decisions.
- **Adversarial Scenario**: The AI is unbeatable and will either win or force a draw.
- **Pygame GUI**: A visually appealing and user-friendly interface for the game.
- **Simple and Clean Code**: The code is modular, well-documented, and easy to understand.

---

## How It Works

### Minimax Algorithm
The Minimax algorithm works by:
1. **Recursively exploring** all possible moves from the current game state.
2. **Evaluating** the game state for terminal conditions (win, lose, or draw).
3. **Assigning a score** to each terminal state:
   - `+1` if the AI wins.
   - `-1` if the player wins.
   - `0` for a draw.
4. **Choosing the move** that maximizes the AI's score while minimizing the player's score.

### Pygame GUI
The Pygame library is used to:
- Render the game board and pieces.
- Handle user input (mouse clicks for moves).
- Display game status (e.g., whose turn it is, win/draw messages).

### Game Flow
1. The player chooses to play as **X** or **O**.
2. The game alternates turns between the player and the AI.
3. The AI uses the Minimax algorithm to determine the best move.
4. The game ends when a player wins or the board is full (draw).

---

## Installation

1. **Clone the repository**:
   ```bash
   git clone 
  
