#!/usr/bin/python3
"""Solves the N-queens puzzle"""

import sys

def init_board(n):
    """Initialize an `n`x`n` sized chessboard with 0's."""
    return [[' ' for _ in range(n)] for _ in range(n)]

def get_solution(board):
    """Return the list of lists representation of a solved chessboard."""
    return [[r, c] for r in range(len(board)) for c in range(len(board)) if board[r][c] == "Q"]

def mark_attacked(board, row, col):
    """Mark attacked positions on a chessboard."""
    n = len(board)
    for i in range(n):
        board[row][i] = "x"  # Mark horizontally
        board[i][col] = "x"  # Mark vertically

    # Mark diagonals
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if i >= 0 and j >= 0:
            board[i][j] = "x"  # Mark diagonally up-left
    for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
        if i >= 0 and j < n:
            board[i][j] = "x"  # Mark diagonally up-right
    for i, j in zip(range(row+1, n), range(col-1, -1, -1)):
        if i < n and j >= 0:
            board[i][j] = "x"  # Mark diagonally down-left
    for i, j in zip(range(row+1, n), range(col+1, n)):
        if i < n and j < n:
            board[i][j] = "x"  # Mark diagonally down-right

def recursive_solve(board, row, queens, solutions):
    """Recursively solve an N-queens puzzle."""
    n = len(board)
    if queens == n:
        solutions.append(get_solution(board))
        return solutions

    for col in range(n):
        if board[row][col] == ' ':
            tmp_board = [row.copy() for row in board]
            tmp_board[row][col] = 'Q'
            mark_attacked(tmp_board, row, col)
            solutions = recursive_solve(tmp_board, row + 1, queens + 1, solutions)

    return solutions

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(int(sys.argv[1]))
    solutions = recursive_solve(board, 0, 0, [])
    for sol in solutions:
        print(sol)

