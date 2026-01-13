# Connect neccessary libraries and scripts
import sys
import os
import helpers
from colorama import Fore
import constants as const

# Handle command line arguments


def command_line_arguments():
    CLI_number = len(sys.argv)
    CLI_arguments = sys.argv
    if CLI_number == 1:
        pass
    else:
        if CLI_number > 2:
            print("\nOnly one command line argument is allowed. Use -h or --help for more information\n")
            exit()
        if CLI_arguments[1] not in const.acceptable_flags:
            print("\nInvalid command line argument. Use -h or --help for more information\n")
            exit()

        flag = CLI_arguments[1]
        if flag == "-h" or flag == "--help":
            helpers.help()
            exit()
        if flag == "-r" or flag == "--rules":
            helpers.game_rules()
            exit()

# String parsing


def user_input():
    continue_input = True
    while continue_input:
        expression = input()
        expression = expression.upper()

        if expression == "Q":
            continue_input = False
            quit()
        if expression == "DONE":
            continue_input = False
            break

        inputted_position = expression[0:2]

        if inputted_position not in const.positions:
            print("Invalid input. Please try again")
            print("Remember that it's column|row. E.g., BF means column B and row F")
            continue

        try:
            value = expression[3:4]
        except:
            print("Invalid input. Please try again \nMust provide a value along with it's position")

        # Just to make sure that value is indeed a number
        try:
            value = int(value)
        except:
            print("Invalid input. Please try again \nValue must be an integer number in range 1-9")
            continue

        # Integer like 3
        value_for_calculation = value
        # String like '\x1b[36m3\x1b[39m' for nice text formating
        value_for_render = Fore.CYAN + str(value) + Fore.RESET

        for position, index in const.position_to_index.items():
            if position == inputted_position:
                # In case user made a mistake and wants to put placeholder, zero, back to the cell
                if value_for_calculation == 0:
                    const.markings_for_rendering[index] = ' '
                    const.markings_for_calculation[index] = value_for_calculation
                    const.constant_markings_indexes.pop(index)
                else:
                    const.markings_for_rendering[index] = value_for_render
                    const.markings_for_calculation[index] = value_for_calculation
                    # Indexes must be unique
                    if index not in const.constant_markings_indexes:
                        const.constant_markings_indexes.append(index)

        os.system('cls' if os.name == 'nt' else 'clear')
        helpers.render_board(const.markings_for_rendering)


# # # # # # # # # # # # #
# # MAIN GAME FUNCTION # #
# # # # # # # # # # # # #
def SUDOKU():

    # Deal with command line arguments
    command_line_arguments()

    # Draw initial sudoku board with blank markings
    helpers.render_board(const.markings_for_rendering)

    # Get user input and draw board with actual markings
    user_input()

    # Solve sudoku
    solved_markings = helpers.solve_sudoku(
        const.markings_for_calculation, const.constant_markings_indexes)

    # Update markings for rendering
    final_rendering = helpers.update_render_markings(solved_markings, const.markings_for_rendering)

    # Draw final solution
    helpers.render_board(final_rendering)


if __name__ == "__main__":
    SUDOKU()
