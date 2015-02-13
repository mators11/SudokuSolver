#!/usr/bin/env python
# encoding: utf-8

from sudokusolver.common import to_str
import sudokusolver.solver as solver

import time
from nose.tools import ok_, eq_

def comparision(list_solverfunc, count):
    for i in range(count):
        print('Puzzle #' + str(i))
        print('')
        sudoku = solver.random_puzzle()
        print(to_str(sudoku))
        print('')
        for j in range(len(list_solverfunc)):
            print('Function #' + str(j))
            print('')
            print('Starting solving...')
            start = time.clock()
            solution = list_solverfunc[j](sudoku)
            dur = time.clock() - start
            print('Stopped solving. Time spent:', dur)
            print('Solution:')
            print(to_str(solution))
            print('')

def benchmark(list_solverfunc, count):
    def test(f, puzzle):
        valid = False
        start = time.clock()
        solution = f(puzzle)
        dur = time.clock() - start
        if solution and (solver.__is_valid(solution) and solver.__is_complete(solution)):
            valid = True
        return dur, valid

    import sys
    print('Starting benchmark')
    bench = []
    for i in range(count):
        if i % 100 == 0:
            sys.stdout.write('.')
            sys.stdout.flush()
        sudoku = solver.random_puzzle()
        res = []
        for j in range(len(list_solverfunc)):
            dur, valid = test(list_solverfunc[j], sudoku)
            res.append((dur, valid))
        bench.append(res)


    print('')
    for i in range(len(list_solverfunc)):
        validCount = 0
        sumTime = 0
        for j in range(len(bench)):
            dur, valid = bench[j][i]
            sumTime = sumTime + dur
            if valid:
                validCount = validCount + 1
        print('Function #' + str(i) + ': Solved ' + str(validCount) + '/' + str(count) + ', total time: ' + str(sumTime) + ', avg time: ' + str(sumTime/count));

def solveAll(list_solverfunc, count):
    for i in range(count):
        print('Puzzle #' + str(i))
        print('')
        sudoku = solver.random_puzzle()
        print(to_str(sudoku))
        print('')
        for j in range(len(list_solverfunc)):
            print('Function #' + str(j))
            start = time.clock()
            solution = list_solverfunc[j](sudoku)
            dur = time.clock() - start
            print('Time spent: '+ str(dur))
            print('Solution:')
            print(to_str(solution))
            print('')
            if solution and (solver.__is_valid(solution) and solver.__is_complete(solution)):
                break
            else:
                print('Function #' + str(j) + ' didn\'t work, resorting to next one...')

if __name__ == '__main__':
    functions = [solver.solve_inet, solver.solve_backtrack]
    #comparision(functions, 1)
    solveAll(functions[:1], 100)
    benchmark(functions[:1], 100)
