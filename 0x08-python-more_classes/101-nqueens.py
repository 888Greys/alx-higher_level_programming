#!/usr/bin/python3
"""
Solves the N-queens puzzle.
Determines all possible solutions to placing N
non-attacking queens on an NxN chessboard.
"""

import sys


def init_board(n):
    """Initialize an `n`x`n` sized chessboard with
    empty spaces."""
    board = [[' ' for _ in range(n)] for _ in range(n)]
    return board


def board_deepcopy(board):
    """Return a deepcopy of a chessboard."""
    return [row[:] for row in board]


def get_solution(board):
    """Return the list of lists representation of a
    solved chessboard."""
    solution = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == "Q":
                solution.append([r, c])
                break
    return solution


def xout(board, row, col):
    """X out spots on a chessboard where non-attacking
    queens can't be placed."""
    n = len(board)
    for c in range(col + 1, n):
        board[row][c] = "x"
    for c in range(col - 1, -1, -1):
        board[row][c] = "x"
    for r in range(row + 1, n):
        board[r][col] = "x"
    for r in range(row - 1, -1, -1):
        board[r][col] = "x"
    r, c = row + 1, col + 1
    while r < n and c < n:
        board[r][c] = "x"
        r += 1
        c += 1
    r, c = row - 1, col - 1
    while r >= 0 and c >= 0:
        board[r][c] = "x"
        r -= 1
        c -= 1
    r, c = row - 1, col + 1
    while r >= 0 and c < n:
        board[r][c] = "x"
        r -= 1
        c += 1
    r, c = row + 1, col - 1
    while r < n and c >= 0:
        board[r][c] = "x"
        r += 1
        c -= 1


def recursive_solve(board, row, queens, solutions):
    """Recursively solve an N-queens puzzle."""
    n = len(board)
    if queens == n:
        solutions.append(get_solution(board))
        return solutions

    for col in range(n):
        if board[row][col] == " ":
            tmp_board = board_deepcopy(board)
            tmp_board[row][col] = "Q"
            xout(tmp_board, row, col)
            solutions = recursive_solve(tmp_board, row+1, queens+1, solutions)
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
