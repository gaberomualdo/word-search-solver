# Word Search Solver

A simple program to solve plaintext word searches. Written in Python2 by [Fred Adams](https://xtrp.io/). Licensed under the [MIT License](https://choosealicense.com/licenses/mit/).

## Overview

The program takes a 2D array of lowercase letters (the word search) and a list of words, and returns the same word search with the words in uppercase.

This repository also includes a Python command line implementation of the program, which can be used to solve word searches easily, without code.

## Download & Usage

### Download with Only ```solveWordSearch``` Function

To download the program with the ```solveWordSearch``` function only, type the following command into your computer's terminal and hit enter:

``` bash
curl https://xtrp.github.io/word_search_solver/word_search_solver.py -o word_search_solver.py
```

Then, to use this function in other Python programs, simply include this line at the top of your programs:

``` bash
execfile("path/to/word_search_solver.py")
```

Note that ```path/to/``` in this command should be replaced with the relative path to the ```word_search_solver.py``` file from your Python program.

### Download with Python Command Line Implementation

To download the program with the ```solveWordSearch``` function as well as the Python command line implementation, type the following command in your computer's terminal and hit enter:

``` bash
curl https://xtrp.github.io/word_search_solver/word_search_solver.py -o word_search_solver.py && curl https://xtrp.github.io/word_search_solver/word_search_solver_app.py -o word_search_solver_app.py && python word_search_solver_app.py
```

Note that this will install the two files ```word_search_solver.py``` and ```word_search_solver_app.py``` in your current working directory. For future use, simple enter the directory that contains both these files, and run the following command:

``` bash
python word_search_solver_app.py
```

## Bugs or Issues

If you find a bug or have an issue with Word Search Solver, feel free to [Submit an Issue](https://github.com/xtrp/word_search_solver/issues/new).
