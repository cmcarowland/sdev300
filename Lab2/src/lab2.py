""" Lab 2 """

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

def menu() -> int:
    """asdf
    """

    user_selection = None
    print("Current Information")
    print('1) Generate Secure Password')
    print('2) Calculate and Format a percentage')
    print('3) Days until July 4, 2025')
    print('4) Calculate Leg of a Triangle')
    print('5) Calculate Volume of a right circulat cylinder')
    print("0) Quit")
    while user_selection is None:
        user_selection = get_int_entry("")

    match user_selection:
        case 0:
            return 1
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
        case 5:
            pass

def main():
    """
    Main function for the Python Voter Registration Application.

    This function runs the voter registration process. It prompts the user to
    continue with the registration, creates a new voter instance, allows the user to
    review and edit the entered information, and provides a confirmation message.

    Returns:
        None
    """

    while menu() == 0:
        continue

if __name__ == "__main__":
    main()
 