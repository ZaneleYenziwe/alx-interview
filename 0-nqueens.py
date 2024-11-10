#!/usr/bin/python3
import sys

def is_safe(board, row, col, n):
    """Check if a queen can be placed at (row, col) on the board."""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_n_queens(n, row, board, result):
    """Solve the N Queens problem using backtracking."""
    if row == n:
        result.append(board[:])
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve_n_queens(n, row + 1, board, result)

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    result = []
    board = [-1] * n
    solve_n_queens(n, 0, board, result)

    for solution in result:
                                      