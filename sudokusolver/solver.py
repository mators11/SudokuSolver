#!/usr/bin/env python
# encoding: utf-8

import random
import sudokusolver.sudoku_inet as inet
from sudokusolver.common import from_vals, to_grid, to_str, from_grid

def __is_valid(sudoku):
    def squares():
        def check_square(sq, x, y):
            occurences = dict()
            for i in range(3):
                for j in range(3):
                    key = sq[x+i][y+j]
                    if key == 0:
                        continue
                    if key in occurences:
                        return False
                    else:
                        occurences[key] = True
            return True

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                valid = check_square(sudoku, i, j)
                if not valid:
                    return False
        return True


    def rows():
        occurences = dict()
        for i in range(9):
            for j in range(9):
                key = sudoku[i][j]
                if key == 0:
                    continue
                if key in occurences:
                    return False
                else:
                    occurences[key] = True
            occurences.clear()
        return True

    def cols():
        occurences = dict()
        for j in range(9):
            for i in range(9):
                key = sudoku[i][j]
                if key == 0:
                    continue
                if key in occurences:
                    return False
                else:
                    occurences[key] = True
            occurences.clear()
        return True

    #print(rows(), cols(), squares())
    return squares() and rows() and cols()

def __is_complete(sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                return False
    return True

def solve_backtrack(sudoku, debug=False):
    def output(sudoku):
        import copy
        if debug:
            print('Solution:')
            print(to_str(sudoku))
            print('')
        solutions.append(copy.deepcopy(sudoku))

    def rec_solve(sudoku):
        if debug:
            print(to_str(sudoku))
            raw_input()
        if not __is_valid(sudoku):
            return False
        if __is_complete(sudoku):
            output(sudoku) # Valid and complete

        for i in range(len(sudoku)):
            for j in range(len(sudoku[i])):
                if sudoku[i][j] == 0:
                    vals = range(1, 9+1)
                    while vals:
                        val = random.choice(vals)
                        vals.remove(val)
                        sudoku[i][j] = val
                        if rec_solve(sudoku):
                            break
                    if not vals:
                        sudoku[i][j] = 0
                        return False
    solutions = []
    rec_solve(sudoku)
    return solutions[0] # Assume only one solution

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

# Combination of methods
def solve(sudoku):
    sol = solve_inet(sudoku)
    if not sol:
        # TODO faster backtracking
        return False
    return sol

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
    solution = solve_backtrack(easy, debug=True)
    print(to_str(solution))
