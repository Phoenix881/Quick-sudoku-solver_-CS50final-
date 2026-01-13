# Sudoku solver

Hi everyone! This is my final project for Harvard's CS50's Introduction to Computer Science course.\
The project is implemented as a command line tool using Python. This tool solves a real world problem - solve almost any sudoku puzzle out there, that is any sudoku puzzle that can be solved with logicical reasoing without having to guess.\
This is version 1.0, and I am having plans to expand and add more functionality to this project later.\
Programming does not stop at CS50!

### 30sec demo
https://github.com/user-attachments/assets/cffbb391-d79c-4ed5-94d8-a44e308c6454

## Functionality
### Command line arguments
You can run "main.py", which is, well, the main script of this program.\
Running just "python main.py" will run the default behaviour which is to promt user on sudoku grid and return it's solution.\
Running program with "-h" or "--help" will print a short help text with acceptable command line arguments and how to input values. This is where a short user manual on Sudoku Grid Encoding system can be found.\
Running program with "-r" or "--rules" will print a short summary of game rules, a few advices, and an example of a solved sudoku puzzle.\

### About Sudoku Grid Encoding system (SGE)
There are 81 cells in sudoku grid. Each encoded with it's own position based on it's column and row.\
Each column and row has a letter assigned to it, from A to I. So, if some cell's position is BD, that means that this cell located in the column B and in the row D.\
In the program all cell values are stored in one big list of size 81. Cell values are stored from left to right from the upper row to the lower.\
In constants.py there is a dictionary that stores index and position pairs. For example the value at index 0 in the list is the value of the cell AA, index 8 - IA, ..., index 80 - II.

### Files in the project
Project Sudoku consists of three .py text files - main.py, helpers.py, constants.py.

In main.py there are functions that have to be there, all other functions and constants are in other two files. This was an intended design desicion to have as less code in the main file as possible. The idea was that a person who has never seen this code before could look up at the main file and immediately guess how it works.

In main.py there is a function that handles command line input, a function that promts user until is done, and most important, actual sudoku game function.\
SUDOKU is representing high level structure of the program:
1. Command line arguments.
2. Draw an empty sudoku grid.
3. Promt user for given values in his/her sudoku.
4. Solve sudoku and get solution.
5. Prepare for rendering solution.
6. Render solution.

In helpers.py is where all other functions are. There are functions that render sudoku board, render help and rules texts, help to prepare solution for rendering, a few function that needed for solving sudoku, and sudoku solving function.

In constants.py are constants that are commonly used in two previous files.

### How input works
So, there are three lists in play here. List of 81 integers, values inputted by user - markings_for_calculation, placeholder is 0. Another list of integers, indexes of those values from the first list - constant_markings_indexes. List of 81 strings, values to show user - markings_for_rendering, placeholders is ' '.
The action sequence is as follows:
1. User runs the program.
2. Program renders a board with initial markings_for_rendering with placeholders everywhere.
3. User inputs position and value.
4. Value's integer copy goes to markings_for_calculation on the appropriate index.
5. Value's another copy is colored in blue and goes to markings_for_rendering on the appropriate index.
6. That appropriate index, constant, is appended to constant_markings_indexes.
7. Program draws an update board with markings_for_rendering.
7. Program repeats steps 3-7 until user inputs the word 'done'.
8. All integer values are in one list, all their locations in the other. And the values that are used for rendering the board is conveniently in yet other list.

### Triple Match Algorithm
And that is Alpha and Omega of this project. The result of some time spending thinking. The Triple Match Algorithm. How it works? It works on the basic property of any solved sudoku puzzle. In each square, column, and row there are 9 numbers from 1 to 9, each occuring only once.
1. Look through each cell, if it is user inputted value, skip and go to the next cell.
2. If the cell is empty then create three lists. Missing numbers in the cell's square, column, and row. Remember, the basic property of sudoku.
3. Look at the intersections of these three lists. Add all common members of them into one new list.
4. If there is only one item in the common members list, then we found what number should go into that cell. Move to the next cell. Repeat steps 2 and 3.
5. If there are more than one items, skip and go to the next cell. Repeat steps 2 and 3.
6. Repeat while there are empty cells in sudoku.

Each iteration shoul reveal some sudoku cell, which will help on the next iteration reveal even more values, and so on. On my short experience of testing, it usually takes around 10 iteration at max.

At first, I tried to implement solving sudoku with brute force, but likely I was lazy enough to came up with the algorithm above.
