"""
This module provides functionality for user account management with password validation and storage.

Imports:
    - sha256_crypt from passlib.hash: For hashing and verifying passwords using SHA-256.
    - os: For file system operations.
    - json: For handling JSON data serialization and deserialization.

Classes:
    Password:
        A class for handling and validating passwords.

        Attributes:
            password (str): The plaintext password.

        Methods:
            __init__(pw):
                Initializes the Password instance with the given password.

            has_upper():
                Checks if the password contains at least one uppercase letter.

            has_lower():
                Checks if the password contains at least one lowercase letter.

            has_digit():
                Checks if the password contains at least one digit.

            has_special():
                Checks if the password contains at least 
                one special character from a predefined set.

            valid_password():
                Validates the password based on criteria: must contain uppercase, lowercase, digit, 
                special character, and be at least 12 characters long.

            get_pw_hash():
                Returns the hashed version of the password using SHA-256.

    Users:
        A class for managing user accounts with password storage and validation.

        Attributes:
            FILENAME (str): The name of the file where user data is stored.

        Methods:
            __init__():
                Initializes the Users instance and loads user data from the file if it exists.

            save():
                Saves the current user data to the file.

            user_exist(user_name):
                Checks if a user with the given username exists.

            add_user(user_name, pw):
                Adds a new user with the given username 
                and password if the user does not already exist
                and the password is valid.

            login(user_name, pw):
                Verifies if the provided username and password are correct for login.

Example:
    If this module is executed as a script, it demonstrates the usage of the Password class
    by creating instances with various passwords and printing the results of validation checks.
"""

import os
import json

from passlib.hash import sha256_crypt

class Password:
    """
    A class for handling and validating passwords.

    Attributes:
        password (str): The plaintext password.

    Methods:
        __init__(pw):
            Initializes the Password instance with the given password.

        has_upper():
            Checks if the password contains at least one uppercase letter.

        has_lower():
            Checks if the password contains at least one lowercase letter.

        has_digit():
            Checks if the password contains at least one digit.

        has_special():
            Checks if the password contains at least one special character from a predefined set.

        valid_password():
            Validates the password based on criteria: must contain uppercase, lowercase, digit, 
            special character, and be at least 12 characters long.

        get_pw_hash():
            Returns the hashed version of the password using SHA-256.
    """

    def __init__(self, pw: str):
        """
        Initializes the Password instance with the given password.

        Args:
            pw (str): The plaintext password.
        """

        self.password : str = pw

    def has_upper(self) -> bool:
        """
        Checks if the password contains at least one uppercase letter.

        Returns:
            bool: True if the password contains an uppercase letter, False otherwise.
        """

        for c in self.password:
            if c.isupper():
                return True

        return False

    def has_lower(self) -> bool:
        """
        Checks if the password contains at least one lowercase letter.

        Returns:
            bool: True if the password contains a lowercase letter, False otherwise.
        """

        for c in self.password:
            if c.islower():
                return True

        return False

    def has_digit(self) -> bool:
        """
        Checks if the password contains at least one digit.

        Returns:
            bool: True if the password contains a digit, False otherwise.
        """

        for c in self.password:
            if c.isdigit():
                return True

        return False

    def has_special(self) -> bool:
        """
        Checks if the password contains at least one special character from a predefined set.

        Returns:
            bool: True if the password contains a special character, False otherwise.
        """

        special = ['@', '_', '!', '#', '$', '%', '^', '&', '*', '(', ')', '<', '>', '?', '~' ]
        for c in self.password:
            if c in special:
                return True

        return False

    def valid_password(self) -> bool:
        """
        Validates the password based on criteria: must contain uppercase, lowercase, digit, 
        special character, and be at least 12 characters long.

        Returns:
            bool: True if the password meets all criteria, False otherwise.
        """

        return self.has_upper() and self.has_lower() and \
            self.has_digit() and self.has_special() and len(self.password) >= 12

    def get_pw_hash(self) -> str:
        """
        Returns the hashed version of the password using SHA-256.

        Returns:
            str: The hashed password.
        """

        sha256 = sha256_crypt.hash(self.password)
        return sha256

class Users:
    """
    A class for managing user accounts with password storage and validation.

    Attributes:
        FILENAME (str): The name of the file where user data is stored.

    Methods:
        __init__():
            Initializes the Users instance and loads user data from the file if it exists.

        save():
            Saves the current user data to the file.

        user_exist(user_name):
            Checks if a user with the given username exists.

        add_user(user_name, pw):
            Adds a new user with the given username and password if the user does not already exist
            and the password is valid.

        login(user_name, pw):
            Verifies if the provided username and password are correct for login.
    """

    FILENAME : str = 'passwords.json'

    def __init__(self):
        """
        Initializes the Users instance and loads user data from the file if it exists.
        """

        self.users = {}
        self.authenticated = {}
        if os.path.exists(Users.FILENAME):
            with open(Users.FILENAME, 'r', encoding='utf-8') as ifile:
                self.users = json.load(ifile)

    def save(self):
        """
        Saves the current user data to the file.
        """

        with open(Users.FILENAME, 'w', encoding='utf-8') as ofile:
            json.dump(self.users, ofile, indent=4)

    def user_exist(self, user_name) -> bool:
        """
        Checks if a user with the given username exists.

        Args:
            user_name (str): The username to check.

        Returns:
            bool: True if the user exists, False otherwise.
        """

        if user_name in self.users.keys():
            return True

        return False

    def add_user(self, user_name : str, pw : str) -> bool:
        """
        Adds a new user with the given username and password if the user does not already exist
        and the password is valid.

        Args:
            user_name (str): The username of the new user.
            pw (str): The password of the new user.

        Returns:
            bool: True if the user was added successfully, False otherwise.
        """

        if self.user_exist(user_name):
            return False

        password = Password(pw)
        if not password.valid_password():
            return False

        self.users[user_name] = password.get_pw_hash()
        self.save()
        return True

    def login(self, user_name : str, pw : str) -> bool:
        """
        Verifies if the provided username and password are correct for login.

        Args:
            user_name (str): The username of the user trying to log in.
            pw (str): The password of the user trying to log in.

        Returns:
            bool: True if the username and password are correct, False otherwise.
        """

        if not self.user_exist(user_name):
            return False

        if not sha256_crypt.verify(pw, self.users[user_name]):
            return False

        return True

if __name__ == "__main__":
    # u = Users()
    # print(u.add_user("testez", "Hello"))
    # print(u.login("test", "ASDF"))
    # print(u.login("test", "Hello"))
    # print(u.login("testes", "Hello"))
    # print(u.login("testes", "Helloasdf"))
    p = Password("Password!1234")
    print(f'Pass: {p.password}')
    print(f'Upper: {p.has_upper()}')
    print(f'Lower: {p.has_lower()}')
    print(f'Digit: {p.has_digit()}')
    print(f'Special: {p.has_special()}')
    print(f'Valid: {p.valid_password()}')

    p = Password("1234asdf!")
    print(f'Pass: {p.password}')
    print(f'Upper: {p.has_upper()}')
    print(f'Lower: {p.has_lower()}')
    print(f'Digit: {p.has_digit()}')
    print(f'Special: {p.has_special()}')
    print(f'Valid: {p.valid_password()}')


    p = Password("1234ASDa!")
    print(f'Pass: {p.password}')
    print(f'Upper: {p.has_upper()}')
    print(f'Lower: {p.has_lower()}')
    print(f'Digit: {p.has_digit()}')
    print(f'Special: {p.has_special()}')
    print(f'Valid: {p.valid_password()}')
