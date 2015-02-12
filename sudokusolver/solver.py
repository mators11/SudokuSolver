#!/usr/bin/env python
# encoding: utf-8

# TODO implement this
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
    def from_vals(vals):
        sudoku = []
        for i in range(9):
            line = []
            for j in range(9):
                line.append(int(vals[str(chr(ord('A') + i)) + str(j + 1)]))
            sudoku.append(line)
        return sudoku

    def to_grid(sudoku):
        grid = ''
        for i in range(len(sudoku)):
            for j in range(len(sudoku[i])):
                if sudoku[i][j] == 0:
                    grid = grid + '.'
                else:
                    grid = grid + str(sudoku[i][j])
        return grid

    import sudokusolver.sudoku_inet as inet

    grid = to_grid(sudoku)
    vals = inet.solve(grid)
    #inet.display(vals)
    return from_vals(vals)

