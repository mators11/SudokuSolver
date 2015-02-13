#!/usr/bin/env python
# encoding: utf-8

import sudokusolver.sudoku_inet as inet
from sudokusolver.common import from_vals, to_grid, to_str, from_grid

def __is_valid(sudoku):
    return None

def __is_complete(sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                return False
    return True

def solve_backtrack(sudoku):
    for i in range(len(sudoku)):
        for j in range(len(sudoku[i])):
            if sudoku[i][j] == 0:
                for val in range(1, 9+1):
                    sudoku[i][j] = val
                    solve_backtrack(sudoku)
                    return sudoku

# Reference implementation
# See: http://norvig.com/sudoku.html
def solve_inet(sudoku):
    grid = to_grid(sudoku)
    vals = inet.solve(grid)
    #inet.display(vals)
    return from_vals(vals)

# Norvig
def random_puzzle():
    return from_grid(inet.random_puzzle())

if __name__ == '__main__':
    easy = [
                [1, 2, 0, 0, 0, 9, 0, 8, 0],
                [3, 0, 4, 8, 0, 0, 9, 0, 2],
                [0, 8, 9, 0, 0, 0, 7, 0, 0],
                [0, 4, 0, 0, 1, 5, 8, 0, 0],
                [8, 1, 0, 0, 0, 0, 3, 0, 9],
                [7, 0, 0, 0, 3, 8, 0, 0, 4],
                [4, 0, 0, 7, 0, 0, 5, 3, 0],
                [2, 0, 0, 0, 0, 0, 0, 4, 1],
                [0, 0, 5, 0, 8, 0, 2, 0, 7]
            ]
    solution = solve_inet(easy)
    print(to_str(solution))
