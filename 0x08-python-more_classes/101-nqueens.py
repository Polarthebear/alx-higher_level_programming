#!/usr/bin/python3
import sys

def is_safe(board, row, col, n):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # Check if there is a queen in the same row
    for i in range(n):
        if board[row][i] == 'Q':
            return False

    # Check upper left diagonal
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j] == 'Q':
            return False

    # Check upper right diagonal
    for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
        if board[i][j] == 'Q':
            return False

    return True

def solve_nqueens(board, row, n, solutions):
    if row == n:
        solutions.append([''.join(row) for row in board])
        return

    new_board = [row.copy() for row in board]

    for col in range(n):
        if is_safe(new_board, row, col, n):
            new_board[row][col] = 'Q'
            solve_nqueens(new_board, row + 1, n, solutions)
            new_board[row][col] = ' '

def print_solutions(n):
    board = [[' ' for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_nqueens(board, 0, n, solutions)

    for solution in solutions:
        for row in solution:
            print(row)
        print()

def print_solutions(n):
    board = [[' ' for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_nqueens(board, 0, n, solutions)

    for solution in solutions:
        for row in solution:
            print(row)
        print()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        if n < 4:
            raise ValueError("N must be at least 4")
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    print_solutions(n)
