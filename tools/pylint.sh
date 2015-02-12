#!/bin/bash

clear
clear
pylint --rcfile=tools/rc_pylint sudokusolver/ $1
