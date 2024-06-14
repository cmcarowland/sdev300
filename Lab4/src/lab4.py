"""
Python Matrix Application

This script provides functionalities for interacting with matrices, 
including entering phone numbers, zip codes, playing a matrix game,
and performing matrix operations.

It includes functions for input validation, matrix operations, matrix manipulation, and a main menu
to navigate through different functionalities.

Dependencies:
    - re
    - numpy
    - input_base (custom module)

Usage:
    Run this script to launch the Python Matrix Application.

    Options:
        1. Enter Phone Number
        2. Enter Zip Code + 4
        3. Matrix Game
        0. Exit
"""

import re
import numpy as np

from input_base import get_int_entry

def get_phone_number() -> str:
    """
    Prompt the user to enter a phone number in the format XXX-XXX-XXXX and returns it.

    Returns:
        str: The phone number entered by the user.
    """

    print("Enter your phone number (XXX-XXX-XXXX): ")

    while True:
        user_number = input()
        if re.match(r'^(\d{3}-){2}\d{4}', user_number) is None or len(user_number) != 12:
            print("Your phone number is not in the correct format. Please Try Again:")
        else:
            break

    return user_number

def get_zip_code() -> str:
    """
    Prompt the user to enter a zip code in the format XXXXX-XXXX and returns it.

    Returns:
        str: The zip code entered by the user.
    """

    print("Enter your Zip code + 4 (XXXXX-XXXX): ")

    while True:
        user_number = input()
        if re.match(r'^\d{5}-\d{4}', user_number) is None or len(user_number) != 10:
            print("Your zip code is not in the correct format. Please Try Again:")
        else:
            break

    return user_number

def matrix_math(matrix1:np.matrix, matrix2:np.matrix, operation) -> np.matrix:
    """
    Perform a mathematical operation on two matrices.

    Args:
        matrix1 (np.matrix): The first matrix.
        matrix2 (np.matrix): The second matrix.
        operation (str): The operation to perform:
            - 'a' for addition
            - 'b' for subtraction
            - 'c' for matrix multiplication
            - 'd' for element-wise multiplication

    Returns:
        np.matrix: The result of the operation on the matrices.
    """

    if operation == 'a':
        return matrix1 + matrix2
    if operation == 'b':
        return matrix1 - matrix2
    if operation == 'c':
        return np.matmul(matrix1, matrix2)
    if operation == 'd':
        return np.multiply(matrix1, matrix2)

    return None

def get_matrix(number:str)-> np.matrix:
    """
    Prompt the user to enter a 3x3 matrix.

    Args:
        number (str): A string indicating the type of matrix (e.g., 'first', 'second').

    Returns:
        np.matrix: A 3x3 matrix entered by the user.
    """

    print(f"Enter your {number} 3x3 matrix one line at a time separated by space (1 2 3)")
    lines = []
    while len(lines) < 3:
        while True:
            line = input()
            if len(line.split()) != 3:
                print("Incorrect format, enter 3 numbers separated with a space")
            else:
                try:
                    lines.append([int(x) for x in line.split()])
                except ValueError:
                    print("Incorrect format, enter 3 numbers separated with a space")

                break

    return np.matrix(lines)

def limit_places(f:float, places:int) -> str:
    """
    Format a float number to limit the decimal places.

    Args:
        f (float): The float number to be formatted.
        places (int): The number of decimal places to limit the float to.

    Returns:
        str: The formatted string representation of the float number with limited decimal places.
    """

    return f'{f:.{places}f}'

def pretty_print_matrix(matrix:np.matrix):
    """
    Print a numpy matrix in a visually pleasing format.

    Args:
        matrix (np.matrix): The matrix to be printed.
    """

    for l in matrix.A:
        for i in l:
            print(i, end=" ")
        print()
    print()

def pretty_print_mean(a:np.ndarray) -> str:
    """
    Generate a string representation of the mean values of a numpy array, 
    formatted with limited decimal places.

    Args:
        a (np.ndarray): The numpy array for which mean values will be calculated and formatted.

    Returns:
        str: A string representation of the mean values of the array, 
        formatted with limited decimal places.
    """

    s = ""
    for l in a:
        for i in l:
            s += limit_places(i, 2) + ", "
    return s[:-2]

def matrix_menu():
    """
    Display the menu options for matrix operations.

    Prints the options for matrix operations, including addition, subtraction,
    matrix multiplication, and element-wise multiplication.
    """

    print("Select a Matrix Operation from the list below:\n")
    print("a) Addition")
    print("b) Subtraction")
    print("c) Matrix Multiplication")
    print("d) Element by element multiplication")

def matrix_game():
    """
    Play a matrix game.

    Prompts the user to input two 3x3 matrices, then displays them and asks the user to select
    an operation (addition, subtraction, matrix multiplication, or element-wise multiplication).
    Displays the result of the selected operation along with its transpose and the mean values
    of rows and columns in the result matrix.
    """

    matrix1 = get_matrix("First")
    print("Your first 3x3 matrix is:")
    pretty_print_matrix(matrix1)
    matrix2 = get_matrix("Second")
    print("Your Second 3x3 matrix is:")
    pretty_print_matrix(matrix2)
    #matrix1 = np.matrix([[1,2,4],[4,2,1],[3,8,9]])
    #matrix2 = np.matrix([[3,2,1],[7,2,5],[5,2,1]])
    # Get operation
    matrix_menu()
    op = ''
    while True:
        if (i := input()) not in ['a', 'b', 'c', 'd']:
            print("Invalid option please select from the list.")
            continue

        match i:
            case 'a':
                op = 'Addition'
            case 'b':
                op = 'Subtraction'
            case 'c':
                op = 'Multiplication'
            case 'd':
                op = 'Hadamard product'
        break

    print(f'You selected {op}. The results are:')
    matrix_result = matrix_math(matrix1, matrix2, i)
    pretty_print_matrix(matrix_result)
    print("The transpose is:")
    pretty_print_matrix(np.transpose(matrix_result))
    print("The row and column mean values of the results are:")
    print(f"Row    : {pretty_print_mean(np.mean(matrix_result, axis=1).tolist())}")
    print(f"Column : {pretty_print_mean(np.mean(matrix_result, axis=0).tolist())}")
    print()

def main_menu():
    """
    Display the main menu options.
    
    Prints the options for the main menu, 
        - including entering a phone number, 
        - entering a zip code + 4,
        - playing the Matrix game, 
        - and exiting the program.
    """

    print('1) Enter Phone Number')
    print('2) Enter Zip Code + 4')
    print('3) Matrix Game')
    print('0) Exit')

def main():
    """
    Entry point for the Python Matrix Application.

    Displays a welcome message and a main menu. Continuously prompts the user
    to select an option from the main menu until the user chooses to exit.

    Options:
        1. Enter Phone Number
        2. Enter Zip Code + 4
        3. Matrix Game
        0. Exit

    After selecting an option, performs the corresponding action.

    Returns:
        None
    """

    print(f'{"*" * 15} Welcome to the Python Matrix Application {"*" * 15}')
    while True:
        main_menu()
        match get_int_entry(""):
            case 1:
                user_number = get_phone_number()
                print(user_number)
            case 2:
                user_zip = get_zip_code()
                print(user_zip)
            case 3:
                matrix_game()
            case 0:
                break

    print(f'\n{"*" * 15} Thanks for playing Python Numpy {"*" * 15}')

if __name__ == "__main__":
    main()
