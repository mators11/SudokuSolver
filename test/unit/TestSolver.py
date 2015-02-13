#!/usr/bin/env python
# encoding: utf-8

import sudokusolver.solver as solver
from test.unit.common import *

from nose.tools import ok_, eq_

# CONSTANTS

inputList = [
        #EASY
        [
            [1, 2, 0, 0, 0, 9, 0, 8, 0],
            [3, 0, 4, 8, 0, 0, 9, 0, 2],
            [0, 8, 9, 0, 0, 0, 7, 0, 0],
            [0, 4, 0, 0, 1, 5, 8, 0, 0],
            [8, 1, 0, 0, 0, 0, 3, 0, 9],
            [7, 0, 0, 0, 3, 8, 0, 0, 4],
            [4, 0, 0, 7, 0, 0, 5, 3, 0],
            [2, 0, 0, 0, 0, 0, 0, 4, 1],
            [0, 0, 5, 0, 8, 0, 2, 0, 7]
        ],
        #MEDIUM
        [
            [6, 0, 0, 0, 4, 0, 0, 0, 0],
            [0, 0, 3, 0, 0, 1, 0, 4, 0],
            [0, 0, 4, 3, 7, 0, 0, 9, 2],
            [7, 0, 0, 0, 0, 0, 3, 0, 0],
            [1, 0, 0, 7, 3, 4, 0, 0, 8],
            [0, 0, 5, 0, 0, 0, 0, 0, 1],
            [8, 5, 0, 0, 9, 2, 6, 0, 0],
            [0, 6, 0, 8, 0, 0, 2, 0, 0],
            [0, 0, 0, 0, 5, 0, 0, 0, 7]
        ],
        #HARD
        [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]
        ]

solutionList = [
        #EASY
        [
            [1, 2, 7, 3, 6, 9, 4, 8, 5],
            [3, 6, 4, 8, 5, 7, 9, 1, 2],
            [5, 8, 9, 1, 4, 2, 7, 6, 3],
            [9, 4, 3, 2, 1, 5, 8, 7, 6],
            [8, 1, 2, 6, 7, 4, 3, 5, 9],
            [7, 5, 6, 9, 3, 8, 1, 2, 4],
            [4, 9, 1, 7, 2, 6, 5, 3, 8],
            [2, 7, 8, 5, 9, 3, 6, 4, 1],
            [6, 3, 5, 4, 8, 1, 2, 9, 7]
        ],
        #MEDIUM
        [
            [6, 7, 1, 2, 4, 9, 8, 3, 5],
            [9, 2, 3, 5, 8, 1, 7, 4, 6],
            [5, 8, 4, 3, 7, 6, 1, 9, 2],
            [7, 4, 8, 1, 2, 5, 3, 6, 9],
            [1, 9, 6, 7, 3, 4, 5, 2, 8],
            [2, 3, 5, 9, 6, 8, 4, 7, 1],
            [8, 5, 7, 4, 9, 2, 6, 1, 3],
            [3, 6, 9, 8, 1, 7, 2, 5, 4],
            [4, 1, 2, 6, 5, 3, 9, 8, 7]
        ],
        #HARD
        [
            [5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9]
        ]
        ]




def solutions(solverfunc):
    for i in range(len(inputList)):
        eq_(solverfunc(inputList[i]), solutionList[i])

def randomTests(solverfunc):
    for i in range(100):
        sudoku = solver.random_puzzle()
        eq_(solverfunc(sudoku), solver.solve_inet(sudoku)) # Compare with reference implementation

#def test_solve_backtrack():
#    solutions(solver.solve_backtrack)
#    randomTests(solver.solve_backtrack)

def test_solve_inet():
    solutions(solver.solve_inet)
    randomTests(solver.solve_inet) # TODO obviously true

