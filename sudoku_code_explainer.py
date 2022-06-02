# Helper Functions

def find_next_empty(puzzle):
    # Finds the next row, column in the puzzle that is not yet assigned a digit
    # The unfilled row or column is represented by -1
    # Function returns a row, column tuple (or(None, None) if there is none)
    pass


def is_valid(puzzle, guess, row, column):
    # Determines whether guess at the row/column of the puzzle is a valid guess
    # The return is either True or False
    pass

# Implementing the solver


def solve_sudoku(puzzle):
    # The puzzle is solved by backtracking.
    # The puzzle is a list of lists whereby each inner list is a row
    # This function returns the solution

    # Steps:
    # 1: Choose a point in the puzzle where the guess would be made
    # 1.1: If there is no point left it means the puzzle is already solved.
    # 2: If there is a place to be assigned a number, a guess is made between 1 and 9
    # 3: The guess made is validated to determine whether or not it is a valid guess
    # 3.1: If the guess is valid, the guess is placed at the point whete the guess is made in the puzzle
    # 4: The solver s then called recursively
    # 5: If the guess is not valid or if nothing gets returned as true, then there is a need for backtracking to try a new number
    # 6: If none of the numbers guessed works, then the puzzle is deemed unsolvable
    pass
