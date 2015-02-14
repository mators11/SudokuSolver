#!/usr/bin/python
# encoding: utf-8

from sudokusolver import finder, solver, common
import sys

def main():
    if len(sys.argv) <= 1: # TODO print help
        exit()

    # TODO Check if argv[1] is a valid path
    path = sys.argv[1]

    # Find and solve
    print('Detecting...')
    sudoku = finder.find_sudoku(path)

    print('Puzzle:')
    if not sudoku:
        print('None')
        exit()

    print(common.to_str(sudoku))
    print('Solving...')
    solution = solver.solve(sudoku)

    print 'Solution:'
    if not solution:
        print('None')
    else:
        print(common.to_str(solution))

main()

