#!/usr/bin/env python
# encoding: utf-8

from sudokusolver.common import to_str
import sudokusolver.solver as solver
from test.unit.common import *

from nose.tools import ok_, eq_, nottest

@nottest
def random_tests(solverfunc):
    for i in range(10):
        sudoku = solver.random_puzzle()
        eq_(solverfunc(sudoku), solver.solve_inet(sudoku), to_str(sudoku)) # Compare with reference implementation

# TOO SLOW!
#def test_solve_backtrack_random():
#    random_tests(solver.solve_backtrack)

def test_solve_inet_random():
    random_tests(solver.solve_inet) # obviously true

