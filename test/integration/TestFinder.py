#!/usr/bin/env python
# encoding: utf-8

import sudokusolver.finder as finder
from test.unit.common import *

from nose.tools import ok_, eq_

# TODO Finish test for finder
def test_images():
    image1 = 'img/test_sudoku1.jpg'
    img = finder.pre_process(image1)
    #square = finder.find_square(img)
    ok_(True)

