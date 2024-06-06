"""This script prompts allows a user to register to vote in the United States"""
#!/usr/bin/env python
from state_codes import us_state_codes, us_state_names

class Voter:
    """
    Class representing a voter.

    Attributes:
        first_name (str): The first name of the voter.
        last_name (str): The last name of the voter.
        age (int): The age of the voter.
        us_citizen (bool): Indicates whether the voter is a U.S. citizen.
        state (str): The state of residence of the voter (2-letter abbreviation).
        zip_code (str): The zip code of the voter's residence.

    Methods:
        __str__: Return a string representation of the voter's information.
        get_info: Get voter information including first name, 
        last name, age, citizenship status, state, and zip code.
        get_first: Prompt the user to provide their first name.
        get_last: Prompt the user to provide their last name.
        get_age: Prompt the user to provide their age and validate it.
        get_us: Prompt the user to specify if they are a U.S. citizen.
        get_state: Prompt the user to enter their state as a 2-letter abbreviation and validate it.
        get_zip: Prompt the user to enter their zip code and validate its length.
    """
    def __init__(self) -> None:
        self.first_name:str = None
        self.last_name:str = None
        self.age:int = None
        self.us_citizen:bool = None
        self.state:str = None
        self.zip_code:str = None

    def __str__(self):
        out_string = f"Name (first, last) : {self.first_name} {self.last_name}\n"
        out_string += f"Age : {self.age}\n"
        out_string += f"U.S. Citizen : {self.us_citizen}\n"
        out_string += f"State : {us_state_names[self.state]}\n"
        out_string += f"Zipcode : {self.zip_code}\n"
        return out_string

    def validate(self) -> bool:
        """
        Validates the attributes of an instance of a class.

        This method checks if all required attributes
        (first_name, last_name, age, us_citizen, state, zip_code)
        are not None.

        Returns:
            bool: True if all required attributes are not None, False otherwise.
        """

        return self.first_name is not None and self.last_name is not None and self.age is not None \
            and self.us_citizen is not None and self.state is not None and self.zip_code is not None

    def get_info(self) -> int:
        """
        Get voter information including first name, 
        last name, age, citizenship status, state, and zip code.

        Returns:
            int:0 if all information is successfully obtained, 
                1 if the user chooses to stop the process at any point,
                2 if the user's age is not eligible for voter registration.
        """

        for i in range(6):
            match i:
                case 0:
                    self.get_string(self.set_first, "Please Enter Your First Name")
                case 1:
                    self.get_string(self.set_last, "Please Enter Your Last Name")
                case 2:
                    if self.get_age() is False:
                        return 2
                case 3:
                    self.get_us()
                    if self.us_citizen is False:
                        return 2
                case 4:
                    self.get_state()
                case 5:
                    self.get_zip()
            if i < 5:
                if continue_process() is False:
                    return 1
        return 0

    def get_string(self, set_string_function, question : str):
        """
        Prompt the user to provide a string value

        Returns:
            None
        """

        while set_string_function(get_string_entry(question).strip()) is False:
            continue

    def set_first(self, new_name) -> bool:
        """
        Sets the first name attribute of the instance 
        to the provided new name.

        Args:
            new_name (str): The new first name value to be set.

        Returns:
            bool: True if the new name is not null or 
            whitespace and successfully set, False otherwise.
        """

        if is_null_or_whitespace(new_name):
            print("Invalid Name.  Please Provide a valid name")
            return False

        self.first_name = new_name
        return True

    def set_last(self, new_name):
        """
        Sets the last name attribute of the instance 
        to the provided new name.

        Args:
            new_name (str): The new last name value to be set.

        Returns:
            bool: True if the new name is not null or 
            whitespace and successfully set, False otherwise.
        """

        if is_null_or_whitespace(new_name):
            print("Invalid Name.  Please Provide a valid name")
            return False

        self.last_name = new_name
        return True

    def get_age(self) -> bool:
        """
        Prompt the user to provide their age and validate it.

        Returns:
            bool: True if the user's age is valid and 
            eligible for voter registration, False otherwise.
        """
        while self.set_age(get_int_entry("Please provide age")) is False:
            continue

    def set_age(self, new_value : int) -> bool:
        """
        Sets the age attribute of the instance to the provided new value.

        Args:
            new_value (int): The new age value to be set.

        Returns:
            bool: True if the new age value is within the valid range
              and successfully set, False otherwise.
        """

        if new_value < 18:
            print(f"You are not yet elegible to register as a voter." \
                    f"Try again in {18-new_value} years.")
            return False
        if new_value > 120:
            print("You are dead.  Sorry you can no longer vote.")
            return False

        self.age = new_value
        return True

    def get_us(self):
        """
        Prompt the user to specify if they are a U.S. citizen.

        Returns:
            None
        """
        while self.us_citizen is None:
            self.us_citizen = get_yes_no("Are you a U.S. Citizen?")

    def set_us(self, is_us : bool) -> bool:
        """
        Sets the US citizen attribute of the instance.

        Args:
            is_us (bool): True if the individual is a US citizen, False otherwise.

        Returns:
            bool: True if the US citizen attribute is successfully set, False if the input is None.
        """

        if is_us is None or is_us is False:
            return False

        self.us_citizen = is_us
        return True

    def get_state(self):
        """
        Prompt the user to enter their state as a 2-letter abbreviation and validate it.

        Returns:
            None
        """

        while self.set_state(get_string_entry(\
        "Please Enter Your State as 2 letter abbreviation").upper()) is False:
            continue

    def set_state(self, new_state : str) -> bool:
        """
        Sets the state attribute of the instance.

        Args:
            new_state (str): The new state value to be set (2-letter abbreviation).

        Returns:
            bool: True if the new state value is a valid 
            US state abbreviation and successfully set, False otherwise.
        """

        if len(new_state) == 2 and new_state in us_state_codes:
            self.state = new_state
            return True

        print("State is not a valid US state")
        return False

    def get_zip(self):
        """
        Prompt the user to enter their zip code and validate its length.

        Returns:
            None
        """

        while self.set_zip(get_string_entry("Please Enter Your Zip Code")) is False:
            continue

    def set_zip(self, new_value : str) -> bool:
        """
        Sets the ZIP code attribute of the instance.

        Args:
            new_value (str): The new ZIP code value to be set.

        Returns:
            bool: True if the new ZIP code value is valid and successfully set, False otherwise.
        """

        if len(new_value) == 5 and new_value.isdigit():
            self.zip_code = new_value
            return True

        print("Invalid Zip Code")
        return False

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

def edit_voter(new_voter : Voter) -> bool:
    """
    Edit the information of a voter.

    Args:
        new_voter (Voter): The voter whose information is being edited.

    Returns:
        None
    """

    while True:
        user_selection = None
        print("Current Information")
        print(new_voter)
        print("1) Edit First Name")
        print("2) Edit Last Name")
        print("3) Edit Age")
        print("4) Edit State")
        print("5) Edit Zip Code")
        print("0) Complete")
        while user_selection is None:
            user_selection = get_int_entry("")

        match user_selection:
            case 0:
                return True
            case 1:
                new_voter.get_first()
            case 2:
                new_voter.get_last()
            case 3:
                cached_age = new_voter.age
                new_voter.get_age()
                if new_voter.age < 18 or new_voter.age > 120:
                    print("Invalid Age. Age has not been modified!!")
                    new_voter.age = cached_age
            case 4:
                new_voter.get_state()
            case 5:
                new_voter.get_zip()

def continue_process() -> bool:
    """
    Prompt the user to continue with the voter registration process.

    Returns:
        bool: True if the user wants to continue, False otherwise.
    """
    answer = None
    while answer is None:
        answer = get_yes_no("Do you want to continue with the voter Registration?")

    return answer

def main():
    """
    Main function for the Python Voter Registration Application.

    This function runs the voter registration process. It prompts the user to
    continue with the registration, creates a new voter instance, allows the user to
    review and edit the entered information, and provides a confirmation message.

    Returns:
        None
    """

    print("Welcome to the Python Voter Registration Application.")
    if continue_process() is False:
        return

    new_voter = Voter()
    match new_voter.get_info():
        case 2:
            print("Invalid Registration")
            return
        case 1:
            print("Registration Aborted")
            return
    if new_voter.validate() is False:
        print("Invalid Registration")

    print("Thanks for registering to vote. Here is the information we received:")
    print(new_voter)
    # while True:
    #     if get_yes_no("Is this information correct?") is False:
    #         edit_voter(new_voter)
    #     else:
    #         break

    print("Thanks for trying the Voter Registration Application.")
    print("Your voter registration card should be shipped within 3 weeks.")


if __name__ == "__main__":
    main()
 