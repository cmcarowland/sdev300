"""
Module: user_input

This module provides functions for interacting with the user via command-line input.

Functions:
    - get_string_entry(question: str) -> str: 
        Prompt the user with a question and retrieve a string entry.
        
    - get_int_entry(question: str) -> int: 
        Prompt the user with a question and retrieve an integer entry.
        
    - is_null_or_whitespace(value: str) -> bool: 
        Checks if a string is None or consists only of whitespace characters.
        
    - get_yes_no(question: str) -> bool: 
        Prompt the user with a question and return True if the user responds with 'yes' or 'y', False if 'no' or 'n'.
"""

def get_string_entry(question : str) -> str:
    """
    Prompt the user with a question and retrieve a string entry.

    Args:
        question (str): The question to prompt the user with.

    Returns:
        str: The string value entered by the user.
    """

    print(question)
    return input("Enter Selection >> ")

def get_int_entry(question : str) -> int:
    """
    Prompt the user with a question and retrieve an integer entry.

    Args:
        question (str): The question to prompt the user with.

    Returns:
        int: The integer value entered by the user.

    Raises:
        ValueError: If the user does not input a valid integer.
    """

    print(question)
    try:
        selection = int(input("Enter Value >> "))
        return selection
    except ValueError:
        print("Invalid entry.  Please specify a number.")
        return None

def is_null_or_whitespace(value : str) -> bool:
    """
    Checks if a string is None or consists only of whitespace characters.

    Args:
        value (str): The string to be checked.

    Returns:
        bool: True if the string is None or consists only of whitespace characters, False otherwise.
    """

    if value is None or len(value.strip()) == 0:
        return True

    return False

def get_yes_no(question : str) -> bool:
    """
    Prompt the user with a question and 
    return True if the user responds with 'yes' or 'y', False if 'no' or 'n'.

    Args:
        question (str): The question to prompt the user with.

    Returns:
        bool: True if the user answers affirmatively ('yes' or 'y'), False otherwise ('no' or 'n').
    """

    print(question)
    valid_options = ['yes', 'y', 'n', 'no']
    user_selection = input("Enter Selection >> ").lower()
    if user_selection in valid_options[:2]:
        return True
    if user_selection in valid_options[2:]:
        return False

    print("Invalid Selection")
    return None
