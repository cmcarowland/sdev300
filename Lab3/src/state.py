"""
Module representing a State class.

This module defines a State class which can be used to 
represent states with attributes such as name, abbreviation, population, and flower.
"""

from state_codes import us_state_codes, us_state_mapping, us_state_names

class State:
    """
    Represents a state with attributes such as name, abbreviation, population, and flower.
    """

    def __init__(self):
        """
        Initializes a State object with default attribute values.
        """

        self.name:str = None
        self.abbreviation:str = None
        self.population:int = 0
        self.flower:str = None
        self.flower_path:str = None

    def __str__(self):
        """
        """

        return f'Name : {self.name}\n' + \
            f'Abbreviation : {self.abbreviation}\n' + \
            f'Population : {self.population:,}\n' + \
            f'Flower : {self.flower}\n'

    def __repr__(self):
        return self.name

    def set_name(self, new_name :str) -> bool:
        if new_name not in us_state_names:
            return False

        self.name = new_name
        self.abbreviation = list(us_state_mapping.keys()) \
            [list(us_state_mapping.values()).index(new_name)]
        self.flower_path = f"images/{self.name}.jpg"

        return True

    def set_abb(self, new_name :str) -> bool:
        if new_name not in us_state_codes:
            return False

        self.abbreviation = new_name
        self.name = us_state_mapping[new_name]
        self.flower_path = f"images/{self.name}.jpg"

        return True

    def set_population(self, new_pop:int) -> bool:
        """
        Set the population of the state to a new value.

        Parameters:
        - new_pop: The new population value.

        Returns:
        - bool: True if the population was successfully set,
          False if the new population value is negative.
        """

        if new_pop < 0:
            return False

        self.population = new_pop
        return True
