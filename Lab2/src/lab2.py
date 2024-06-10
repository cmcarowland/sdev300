""" Lab 2 """
from datetime import datetime
import random
import math

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

def format_percent(value:float, places:int) -> str:
    """
    Formats a percentage value to a string with a specified 
    number of decimal places.

    Parameters:
        value (float): The percentage value to format.
        places (int): The number of decimal places to display.

    Returns:
        str: The formatted percentage string.
    """


    return f'{value * 100:.{places}f}'

def calculate_percentage(a:float, b:float) -> float:
    """
    Calculates the percentage of one number relative to another.

    Parameters:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The percentage of `a` relative to `b`.
            -1 if either `a` or `b` is less than or equal to 0.
    """


    if a <= 0 or b <= 0:
        return -1

    return a / b

def percentage() -> int:
    """
    Calculates the percentage of one number relative to another and prints it.

    This function prompts the user to input two numbers and the number of decimal places
    to display in the result. It then calculates the percentage of the first number relative
    to the second number and prints the result.

    Returns:
        int: 0 if the percentage is successfully calculated and printed.
            3 if there are invalid inputs or errors during the calculation.
    """

    val1 = get_int_entry("Enter the first number")
    val2 = get_int_entry("Enter the second number")
    places = get_int_entry("Enter the number of places to display")
    if val1 is None or val2 is None:
        print("Invalid Inputs.  Please Try Again")
        return 3

    percent = calculate_percentage(val1, val2)
    if percent == -1 or places is None or places < 0:
        print("Invalid Inputs.  Please Try Again")
        return 3

    print(f'\nThe Percentage is : {format_percent(percent, places)}')
    return 0

def get_days():
    """
    Prints the number of days until July 4, 2025.

    This function calculates the number of days remaining until July 4, 2025,
    based on the current date.

    Note:
        This function does not take any parameters.

    Returns:
        None
    """

    date_str = '07-04-2025'

    date_object = datetime.strptime(date_str, '%m-%d-%Y')
    print(f'\nDays until July 4, 2025 : {(date_object - datetime.now()).days}')

def get_password(length:int, has_upper:bool, has_lower:bool,\
     has_digits:bool, has_special:bool) -> str:
    """
    Generates a password based on provided parameters.

    Parameters:
        length (int): The length of the password.
        has_upper (bool): Whether the password should contain uppercase letters.
        has_lower (bool): Whether the password should contain lowercase letters.
        has_digits (bool): Whether the password should contain digits.
        has_special (bool): Whether the password should contain special characters.

    Returns:
        str: The generated password.
            None if unable to generate a password due to invalid input.
    """

    if length == 0 or not (has_upper or has_lower or has_digits or has_special):
        print("Cannot generate a password")
        return None

    possible_characters = []
    if has_upper:
        possible_characters.extend(range(0x41, 0x41+26))
    if has_lower:
        possible_characters.extend(range(0x61, 0x61+26))
    if has_digits:
        possible_characters.extend(range(0x30, 0x3a))
    if has_special:
        possible_characters.extend(range(0x21, 0x30))

    password = []
    for _ in range(length):
        password.append(chr(random.choice(possible_characters)))

    return ''.join(password)

def create_password() -> int:
    """
    Generates a password based on user input and prints it.

    This function prompts the user to input parameters for generating a password, including length,
    whether it should contain uppercase letters, lowercase letters, digits, and special characters.

    Returns:
        int: 0 if a password is successfully generated and printed.
            3 if it's unable to generate a password (either due to invalid input or other errors).
    """

    length = get_int_entry("Enter Password Length")
    has_upper = get_yes_no("Does password have Uppercase letters?")
    has_lower = get_yes_no("Does password have Lowercase letters?")
    has_digits = get_yes_no("Does password have digits?")
    has_special = get_yes_no("Does password have special characters?")

    if length == 0 or not (has_upper or has_lower or has_digits or has_special):
        print("Cannot generate a password")
        return 3

    pw = get_password(length, has_upper, has_lower, has_digits, has_special)
    if pw is None:
        return 3

    print(f"\nThe Password is : {pw}")
    return 0

def calculate_triangle(side_a: int, side_b:int, angle:int) -> float:
    """
    Calculate the length of the third side of a triangle given two sides and the included angle.

    Args:
        side_a (int): Length of the first side of the triangle.
        side_b (int): Length of the second side of the triangle.
        angle (int): Measure of the included angle between the first and second sides, in degrees.

    Returns:
        float: Length of the third side of the triangle.
                Returns -1 if any of the inputs are None or 
                if any side or angle is less than or equal to zero.
    """

    if side_a is None or side_b is None or angle is None:
        return -1

    if side_a <= 0 or side_b <= 0 or angle <= 0:
        return -1

    c = math.sqrt(math.pow(side_a, 2) + math.pow(side_b, 2) - \
         2 * side_a * side_b * math.cos(math.radians(angle)))
    return c

def get_triangle_for_user() -> int:
    """
    Prompt the user to enter the dimensions of a triangle
     and calculate the length of its third side.

    Returns:
        int: 0 if the operation was successful, 3 if 
        invalid parameters were provided.
    """


    side_a = get_int_entry("Enter Length of Side a")
    side_b = get_int_entry("Enter Length of Side b")
    angle = get_int_entry("Enter angle of C")

    if side_a is None or side_b is None or angle is None:
        print("Invalid Parameters for triangle, please try again")
        return 3

    if side_a <= 0 or side_b <= 0 or angle <= 0:
        print("Invalid Parameters for triangle, please try again")
        return 3

    side_c_len = calculate_triangle(side_a, side_b, angle)
    if side_c_len == -1:
        print("Invalid Parameters for triangle, please try again")
        return 3

    print(f"\nThe Length of side c is {side_c_len}")
    return 0

def calculate_volume_of_cylinder(radius:int, height:int) -> float:
    """
    Calculate the volume of a cylinder.

    Args:
        radius (int): Radius of the cylinder.
        height (int): Height of the cylinder.

    Returns:
        float: Volume of the cylinder.
            Returns -1 if either radius or 
            height is None or if either is less than or equal to zero.
    """


    if radius is None or height is None or radius <= 0 or height <= 0:
        return -1

    return math.pi * math.pow(radius, 2) * height

def get_cylinder_volume() -> int:
    """
    Prompt the user to enter the dimensions of a cylinder and calculate its volume.

    Returns:
        int: 0 if the operation was successful, 3 if invalid parameters were provided.
    """

    radius = get_int_entry("Enter Radius of Cylinder")
    height = get_int_entry("Enter Height of Cylinder")

    if radius is None or height is None:
        print("Invalid Parameters for cylinder, please try again")
        return 3

    if radius <= 0 or height <= 0:
        print("Invalid Parameters for cylinder, please try again")
        return 3

    vol = calculate_volume_of_cylinder(radius, height)
    if vol == -1:
        print("Invalid Parameters for cylinder, please try again")
        return 3

    print(f"\nThe Volume of a cylinder with H: {height} R: {radius} is {vol}")
    return 0

def menu() -> int:
    """
    Displays a menu of options and performs the selected action.

    This function displays a menu with various options for the user to choose from.
    Based on the user's selection, it performs the corresponding action.

    Returns:
        int: An integer indicating the status of the menu operation:
            - 0 if the menu operation is successful.
            - 1 if the user chooses to quit.
            - 2 if there is an invalid option selected or other errors occur.
    """

    user_selection = None
    print("")
    print('1) Generate Secure Password')
    print('2) Calculate and Format a percentage')
    print('3) Days until July 4, 2025')
    print('4) Calculate Leg of a Triangle')
    print('5) Calculate Volume of a right circular cylinder')
    print("0) Quit")
    user_selection = get_int_entry("")
    out_value = 1
    match user_selection:
        case 0:
            out_value = 1
        case 1:
            out_value = create_password()
        case 2:
            out_value = percentage()
        case 3:
            get_days()
            out_value = 0
        case 4:
            out_value = get_triangle_for_user()
        case 5:
            #Volume of Circular Cylinder = (πr2) × Height
            return get_cylinder_volume()
        case _:
            print("Invalid Option")
            out_value = 2

    return out_value

def main():
    """
    Main function for the Python Math and Secret Functions application.

    This function controls the flow of the program by repeatedly displaying the menu
    and processing the user's choice until the user chooses to quit. After quitting,
    it prints a thank you message.

    Returns:
        None
    """

    while menu() != 1:
        continue

    print("Thank you for using the Math and Secret Functions application")

if __name__ == "__main__":
    main()
 