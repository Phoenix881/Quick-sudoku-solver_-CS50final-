import constants as const
import collections


# Short summary of acceptable command line arguments
# Terminal output
def help():
    help = f"""Usage main.py [OPTION]

{" " * 3}-h, --help{" " * 40}Print this help text and options
{" " * 3}-r, --rules{" " * 39}Print sudoku game rules

About inputting values
Each cell in a sudoku board here has it's position identifier consisting of two letters.
First letter is this cell's column, and the second is it's row.
To input value all you need is to specify the location and after the column the value you want to put.
For example, if we want to put 8 in cell BD, we would write BD:8.
If you made a mistake and did not want a value there, just assign it to be zero.
Typing BD:0 will reset that cell.
    """
    print(help)


# Short summary of game rules, a few advices, and a nice solved sudoku
# Terminal output
def game_rules():
    rules = """SUDOKU Game Rules And Recommendations

Rule #1.
Sudoku is a logical puzzle based on numbers. It is played on a 9 x 9 grid. Within the grid there are 9 smaller square each containing 9 spaces. For solving the puzzle, each row, column and square must be filled out with the numbers 1-9, without repeating any numbers within the row, column or square.
Rule #2.
Don't repeat any numbers. In each row, line, square each numbers from 1 to 9 must occur only once.
Rule #3.
Number zero is not used in sudoku. (In this program it is used only as a placeholder)

Advice #1.
It is highly recommended to use pen and paper while doing sudoku. That's especially true for digital sudokus like this one.
Advice #2.
Since numbers from 1 to 9 must be repeated the sum of each row, column, and square is 45. You can prove this by summing each number from 1 to 9.
Advice #3.
Don't guess. Guessing can make later stage of the game a total mess.


Here's an example of a solved sudoku puzzle
++-+-+-++-+-+-++-+-+-++
||8|2|7||1|5|4||3|9|6||
||9|6|5||3|2|7||1|4|8||
||3|4|1||6|8|9||7|5|2||
++-+-+-++-+-+-++-+-+-++
||5|9|3||4|6|8||2|7|1||
||4|7|2||5|1|3||6|8|9||
||6|1|8||9|7|2||4|3|5||
++-+-+-++-+-+-++-+-+-++
||7|8|6||2|3|5||9|1|4||
||1|5|4||7|9|6||8|2|3||
||2|3|9||8|4|1||5|6|7||
++-+-+-++-+-+-++-+-+-++
"""
    print(rules)


# Used to render the sudoku grid with values in each cell
# Number zero is used as a safe placeholder since it's usage is not allowed by sudoku rules
# Terminal output
def render_board(markings):

    board = f"""
\t\t\t\t\tSUDOKU\n
\t     A       B       C        D       E       F        G       H       I  \n
\t +-------+-------+-------++-------+-------+-------++-------+-------+-------+
\t |       |       |       ||       |       |       ||       |       |       |
    A    |   {markings[0]}   |   {markings[1]}   |   {markings[2]}   ||   {markings[3]}   |   {markings[4]}   |   {markings[5]}   ||   {markings[6]}   |   {markings[7]}   |   {markings[8]}   |
\t |       |       |       ||       |       |       ||       |       |       |
\t +-------+-------+-------++-------+-------+-------++-------+-------+-------+
\t |       |       |       ||       |       |       ||       |       |       |
    B    |   {markings[9]}   |   {markings[10]}   |   {markings[11]}   ||   {markings[12]}   |   {markings[13]}   |   {markings[14]}   ||   {markings[15]}   |   {markings[16]}   |   {markings[17]}   |
\t |       |       |       ||       |       |       ||       |       |       |
\t +-------+-------+-------++-------+-------+-------++-------+-------+-------+
\t |       |       |       ||       |       |       ||       |       |       |
    C    |   {markings[18]}   |   {markings[19]}   |   {markings[20]}   ||   {markings[21]}   |   {markings[22]}   |   {markings[23]}   ||   {markings[24]}   |   {markings[25]}   |   {markings[26]}   |
\t |       |       |       ||       |       |       ||       |       |       |
\t +-------+-------+-------++-------+-------+-------++-------+-------+-------+
\t +-------+-------+-------++-------+-------+-------++-------+-------+-------+
\t |       |       |       ||       |       |       ||       |       |       |
    D    |   {markings[27]}   |   {markings[28]}   |   {markings[29]}   ||   {markings[30]}   |   {markings[31]}   |   {markings[32]}   ||   {markings[33]}   |   {markings[34]}   |   {markings[35]}   |
\t |       |       |       ||       |       |       ||       |       |       |
\t +-------+-------+-------++-------+-------+-------++-------+-------+-------+
\t |       |       |       ||       |       |       ||       |       |       |
    E    |   {markings[36]}   |   {markings[37]}   |   {markings[38]}   ||   {markings[39]}   |   {markings[40]}   |   {markings[41]}   ||   {markings[42]}   |   {markings[43]}   |   {markings[44]}   |
\t |       |       |       ||       |       |       ||       |       |       |
\t +-------+-------+-------++-------+-------+-------++-------+-------+-------+
\t |       |       |       ||       |       |       ||       |       |       |
    F    |   {markings[45]}   |   {markings[46]}   |   {markings[47]}   ||   {markings[48]}   |   {markings[49]}   |   {markings[50]}   ||   {markings[51]}   |   {markings[52]}   |   {markings[53]}   |
\t |       |       |       ||       |       |       ||       |       |       |
\t +-------+-------+-------++-------+-------+-------++-------+-------+-------+
\t +-------+-------+-------++-------+-------+-------++-------+-------+-------+
\t |       |       |       ||       |       |       ||       |       |       |
    G    |   {markings[54]}   |   {markings[55]}   |   {markings[56]}   ||   {markings[57]}   |   {markings[58]}   |   {markings[59]}   ||   {markings[60]}   |   {markings[61]}   |   {markings[62]}   |
\t |       |       |       ||       |       |       ||       |       |       |
\t +-------+-------+-------++-------+-------+-------++-------+-------+-------+
\t |       |       |       ||       |       |       ||       |       |       |
    H    |   {markings[63]}   |   {markings[64]}   |   {markings[65]}   ||   {markings[66]}   |   {markings[67]}   |   {markings[68]}   ||   {markings[69]}   |   {markings[70]}   |   {markings[71]}   |
\t |       |       |       ||       |       |       ||       |       |       |
\t +-------+-------+-------++-------+-------+-------++-------+-------+-------+
\t |       |       |       ||       |       |       ||       |       |       |
    I    |   {markings[72]}   |   {markings[73]}   |   {markings[74]}   ||   {markings[75]}   |   {markings[76]}   |   {markings[77]}   ||   {markings[78]}   |   {markings[79]}   |   {markings[80]}   |
\t |       |       |       ||       |       |       ||       |       |       |
\t +-------+-------+-------++-------+-------+-------++-------+-------+-------+
    """
    print(board)



#
# Function for solve_sudoku function
#
# If the square has only numbers 1, 7, 2, 5, and 6
# This will return 3, 4, 8, 9
def missing_numbers(markings, sequence):
    sequence_copy = []
    for position in sequence:
        position_temp = markings[position]
        sequence_copy.append(position_temp)

    missing = []
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for num in numbers:
        if num not in sequence_copy:
            missing.append(num)

    return missing

# Input: two lists
# Output: one list with common members from input
def common_member(a, b):
    result = collections.Counter(a) & collections.Counter(b)
    return list(result.keys())

# Three lists -> one list with common members
def common_member_three_lists(a, b, c):
    result = collections.Counter(a) & collections.Counter(b) & collections.Counter(c)
    return list(result.keys())

# Returns a list of indexes in a row
def get_row(c, position):
    row_A = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    row_B = [9, 10, 11, 12, 13, 14, 15, 16, 17]
    row_C = [18, 19, 20, 21, 22, 23, 24, 25, 26]
    row_D = [27, 28, 29, 30, 31, 32, 33, 34, 35]
    row_E = [36, 37, 38, 39, 40, 41, 42, 43, 44]
    row_F = [45, 46, 47, 48, 49, 50, 51, 52, 53]
    row_G = [54, 55, 56, 57, 58, 59, 60, 61, 62]
    row_H = [63, 64, 65, 66, 67, 68, 69, 70, 71]
    row_I = [72, 73, 74, 75, 76, 77, 78, 79, 80]

    row_number = position[1]
    if row_number == 'A':
        return row_A
    if row_number == 'B':
        return row_B
    if row_number == 'C':
        return row_C
    if row_number == 'D':
        return row_D
    if row_number == 'E':
        return row_E
    if row_number == 'F':
        return row_F
    if row_number == 'G':
        return row_G
    if row_number == 'H':
        return row_H
    if row_number == 'I':
        return row_I

# Returns a list of indexes in a column
def get_column(c, position):
    column_A = [0, 9, 18, 27, 36, 45, 54, 63, 72]
    column_B = [1, 10, 19, 28, 37, 46, 55, 64, 73]
    column_C = [2, 11, 20, 29, 38, 47, 56, 65, 74]
    column_D = [3, 12, 21, 30, 39, 48, 57, 66, 75]
    column_E = [4, 13, 22, 31, 40, 49, 58, 67, 76]
    column_F = [5, 14, 23, 32, 41, 50, 59, 68, 77]
    column_G = [6, 15, 24, 33, 42, 51, 60, 69, 78]
    column_H = [7, 16, 25, 34, 43, 52, 61, 70, 79]
    column_I = [8, 17, 26, 35, 44, 53, 62, 71, 80]

    column_number = position[0]
    if column_number == 'A':
        return column_A
    if column_number == 'B':
        return column_B
    if column_number == 'C':
        return column_C
    if column_number == 'D':
        return column_D
    if column_number == 'E':
        return column_E
    if column_number == 'F':
        return column_F
    if column_number == 'G':
        return column_G
    if column_number == 'H':
        return column_H
    if column_number == 'I':
        return column_I

# Input: 28
# Output: 'BD'
def index_to_position(index):
    position = ''
    for key, value in const.position_to_index.items():
        if value == index:
            position = key
    return position


# Solve sudoku
def solve_sudoku(markings, constants):
    # To make each element unique we convert list to set
    # To not bother with sets not supporting index slicing we convert set back to list
    # And sort it for convinience
    # print(markings)
    # print(constants)

    constants = set(constants)
    constants = list(constants)
    constants.sort()


    squares = [const.square_one, const.square_two, const.square_three,
               const.square_four, const.square_five, const.square_six,
               const.square_seven, const.square_eight, const.square_nine]

    # This tuple is needed to check if we have a brute force required sudoku
    # That is sudoku that cannot be solved only be logical decision and require randomization
    test = tuple(markings)

    # While there are empty cells in sudoku

    placeholder = 0
    while placeholder in markings:
        # Look at one square at a time
        for square in squares:
            # Look at each cell in that square
            for cell in square:
                # If we cannot change the value of the cell we are currently looking at
                # Then that's the user inputted value and we go the the next iteration, next cell
                if cell in constants:
                    continue

                # We have a cell index
                # We need to find this cell's column and row
                # Knowing index we can look up it's position like BD
                # Knowing BD we can get column and row
                # I already wrote two funcions that will help me
                # get_row and get_column
                # I only need to pass index in letter notation and markings list
                # Each of two functions will return list of values of the corresponding column and row
                cell_position = index_to_position(cell)
                cell_column = get_column(markings, cell_position)
                cell_row = get_row(markings, cell_position)

                # Triple match alg
                # Find what numbers are needed to complete column, row, and square
                # If there is one same number in each of these, then write that number to that cell
                # If not, then skip and go the next empty cell
                # In that way, cell by cell, square by square every space will be filled (i hope)

                square_missing = missing_numbers(markings, square)
                column_missing = missing_numbers(markings, cell_column)
                row_missing = missing_numbers(markings, cell_row)

                # Triple match pairs
                # Square and column
                # Square and row
                # Column and row

                column_and_row_common = common_member(column_missing, row_missing)
                square_and_column_common = common_member(square_missing, column_missing)
                square_and_row_common = common_member(square_missing, row_missing)

                # Now we need to match three lists
                final_match = common_member_three_lists(column_and_row_common,
                                                        square_and_column_common, square_and_row_common)

                # If there is only one match, add that match to markings
                if len(final_match) == 1:
                    markings[cell] = final_match[0]
                # Else, go to the next cell
                else:
                    continue
        # If there is no changes then this requires brute force, ain't dealing with that
        if tuple(markings) == test:
            print("Sorry. It appears that you inputted ", end="")
            print("either incorrect sudoku puzzle or your sudoku puzzle requires ", end="")
            print("guessing in order to solve it. Either way, I am afraid I cannot help you")
            quit()

    # Outside sudoku solving loop
    return markings



# Update markings for rendering with solved markings
def update_render_markings(solved, render):
    # Iterate throw every item in markings_for_render
    # markings_for_render is str list with ' ' being a placeholder
    # In that list user inputted values are colored with ASCII codes throw colorama
    for i in range(0, 81):
        # If placeholder then we can add found value
        if render[i] == ' ':
            render[i] = str(solved[i])

    return render

