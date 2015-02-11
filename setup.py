#!/usr/bin/env python
# encoding: utf-8

from setuptools import setup, find_packages

setup(
    name = 'SudokuSolver',
    version = '0.1.0dev',
    author = 'SudokuSolver Contributors',
    author_email = 'mators11@gmail.com',
    packages = find_packages(exclude=['tests']),
    scripts = ['main.py'],
    url = 'http://pypi.python.org/pypi/SudokuSolver/',
    license = 'MIT License',
    description = 'A sudoku solver',
    keywords = 'sudoku solver',
    test_suite = 'nose.collector',
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python',
    ],
    long_description = open('README').read(),
    install_requires = [
        'nose >= 1.3.0',
        'nose-exclude >= 0.2.0',
        'python-coveralls >= 2.4.2',
    ],
)
