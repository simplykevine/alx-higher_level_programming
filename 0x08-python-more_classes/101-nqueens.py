#!/usr/bin/python3
"""calculates and return the area of the rectangle
"""
import sys

'''
File_name: 101-nqueens.py
Created: 30-OCT-2023
Author: UMUTONI Kevine (simplykevine)
Size: undefined
Project: 0x08-python-more_classes
Status: not yet submitted.
'''


def is_safe(board, row, col):
    """
    # Chess grandmaster Judit Polgár, the strongest female chess...
    # player of all time...The N queens puzzle is the challenge of....
    # ....placing N non-attacking queens on an N×N chessboard...
    # Write a program that solves the N queens problem.....
    # VARIABLE(" "):
    # Return: Always 0, (Success).
    """
    """ Check if it's safe to place a queen at board[row][col]
    """

    # Check row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check lower diagonal on the left side
    i, j = row, col
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def solve_nqueens(board, col):
    """ Solve the N-Queens problem using backtracking
    """

    # Base case: If all queens are placed
    if col >= N:
        print_solution(board)
        return True

    # Consider this column and try placing a queen in all rows
    for i in range(N):
        if is_safe(board, i, col):
            board[i][col] = 1
            """Place the queen"""

        # Recur to place the rest of the queens
        solve_nqueens(board, col + 1)

        # Backtrack and remove the queen from this cell
        board[i][col] = 0


def print_solution(board):
    """ Print the solution in the required format
    """

    solution = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                solution.append([i, j])
    print(solution)


if __name__ == "__main__":
    # Check if the number of arguments is correct
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check if N is at least 4
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize an empty chessboard
    board = [[0 for _ in range(N)] for _ in range(N)]

    # Solve the N-Queens problem
    solve_nqueens(board, 0)
