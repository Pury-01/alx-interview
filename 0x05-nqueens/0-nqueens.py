#!/usr/bin/python3
"""
N Queens Problem - Backtracking Algorithm
Solves the N Queens problem for N×N chessboards.
"""
import sys


def print_solution(board):
    """Prints a board's solution as a list of coordinate positions."""
    solution = []
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 1:
                solution.append([row, col])
    print(solution)


def is_safe(board, row, col, n):
    """
    Checks if placing a queen at board[row][col] is safe.
    A position is safe if there is no other queen in the
    same column, diagonal, or row.
    """
    # Check current column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(board, row, n):
    """
    Uses backtracking to find all solutions for the N Queens problem.
    """
    if row == n:
        print_solution(board)
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1  # Place queen
            solve_nqueens(board, row + 1, n)  # Recurse
            board[row][col] = 0  # Backtrack


def main():
    """Main entry point for the N Queens program."""
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

    # Initialize the board
    board = [[0 for _ in range(n)] for _ in range(n)]

    # Solve the NQueens problem
    solve_nqueens(board, 0, n)


if __name__ == "__main__":
    main()
