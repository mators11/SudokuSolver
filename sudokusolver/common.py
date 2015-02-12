#!/usr/bin/env python
# encoding: utf-8

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

def from_vals_to_grid(vals):
    return to_grid(from_vals(vals))

def to_str_vals(vals):
    return to_str(from_vals(vals))

def to_str(sudoku):
    out = ''
    for i in range(9):
        for j in range(9):
            out = out + str(sudoku[i][j])
            out = out + ' '
            if ((j + 1) % 3 == 0) and ((j + 1) / 3 < 3):
                out = out + '|'
        out = out + '\n'
        if ((i + 1) % 3 == 0) and ((i + 1) / 3 < 3):
            for j in range(2 * 9 + 2):
                if ((j + 1) % 7 == 0) and ((j + 1) / 7 < 3):
                    out = out + '+'
                else:
                    out = out + '-'
            out = out + '\n'
    return out

