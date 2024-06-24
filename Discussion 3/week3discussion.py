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
    
def get_int_entry_old(question : str) -> int:
    """
    Prompt the user with a question and retrieve an integer entry.

    Args:
        question (str): The question to prompt the user with.

    Returns:
        int: The integer value entered by the user.
    """

    print(question)
    selection = int(input("Enter Value >> "))

print("The old way without validation")
get_int_entry_old("Please Enter Your Age")


print("Using the new validation with try catch")

while get_int_entry("Please Enter Your Age") is None:
    continue
