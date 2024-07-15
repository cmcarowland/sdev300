"""
This module provides classes for analyzing and processing different types of data using pandas.

Classes:
- Data: A base class for handling generic data operations.
- PopData: Subclass of Data specifically for population data analysis.
- HousingData: Subclass of Data for housing data analysis.

Functions:
- main_menu: Displays the main menu options for data analysis.
- main: The main function to execute the data analysis application.

Usage:
Run this module to launch the Python Data Analysis App,
which allows users to analyze population and housing data.
"""
import dataclasses
from datetime import datetime
# import webbrowser
import pandas as pd

import input_base

@dataclasses.dataclass
class Stats():
    """
    A dataclass for storing basic statistical values.

    Attributes:
    - count (int): The count of data points.
    - mean (float): The mean (average) value.
    - std_dev (float): The standard deviation.
    - min_val (float): The minimum value.
    - max_val (float): The maximum value.

    Methods:
    - __init__(): Initializes all attributes to zero.
    """

    def __init__(self) -> None:
        self.count = 0
        self.mean = 0
        self.std_dev = 0
        self.min_val = 0
        self.max_val = 0

class Data():
    """
    A base class for data handling and analysis using pandas.

    Attributes:
    - file_name (str): The file path of the CSV file containing the data.
    - col (str or None): The column name selected for analysis.
    - selection (int): User selection for menu options.
    - stats (Stats): An instance of the Stats class to store statistical values.
    - df (pandas.DataFrame or None): The DataFrame holding the loaded CSV data.

    Methods:
    - show(): Placeholder method to display information.
    - process_menu(): Processes user input for menu selections.
    - show_data(): Displays calculated statistical data.
    - open_file(): Opens and loads the CSV file specified by file_name into the df attribute.
    - validate(): Placeholder method for data validation.
    - calculate() -> bool: Calculates statistics for the selected column and saves a histogram plot.

    Usage:
    This class serves as a base for handling and analyzing 
    CSV data using pandas, providing methods to open files, calculate statistics, and display data.
    """

    def __init__(self, fn : str) -> None:
        self.file_name = fn
        self.col = None
        self.selection = 0
        self.stats = Stats()
        self.df = None
        self.open_file()

    def show(self) -> None:
        """
        Placeholder method to display information.
        """

    def process_menu(self) -> None:
        """
        Processes user input for menu selections.
        """

        self.show()
        self.selection = input_base.get_int_entry("")

    def show_data(self) -> None:
        """
        Displays calculated statistical data including 
        count, mean, standard deviation, min, and max values.
        """

        print(f"Count: {self.stats.count:.{2}f}")
        print(f"Mean: {self.stats.mean:.{2}f}")
        print(f"Standard Deviation: {self.stats.std_dev:.{2}f}")
        print(f"Min: {self.stats.min_val:.{2}f}")
        print(f"Max: {self.stats.max_val:.{2}f}")
        print()
        # webbrowser.open('HistData.png')

    def open_file(self):
        """
        Opens and loads the CSV file specified by file_name into the df attribute.
        """

        self.df = pd.read_csv(self.file_name)

    def validate(self):
        """
        Placeholder method for data validation.
        """

    def calculate(self) -> bool:
        """
        Calculates statistics (count, mean, standard deviation, min, max) 
        for the selected column (self.col) in the DataFrame (self.df).
        
        Saves a histogram plot of the column as 'HistData.png'.
        
        Returns:
        - bool: True if calculation was successful, False if self.col is None.
        """

        if self.col is None or self.col not in self.df.columns:
            print("\nInvalid Data Requested\n")
            return False

        self.stats.count = self.df.loc[:, self.col].count()
        self.stats.mean = self.df.loc[:, self.col].mean()
        self.stats.std_dev = self.df.loc[:, self.col].std()
        self.stats.min_val = self.df.loc[:, self.col].min()
        self.stats.max_val = self.df.loc[:, self.col].max()
        self.df.plot.hist(column=[self.col], bins=10).get_figure().savefig('HistData.png')
        # webbrowser.open('HistData.png')
        return True

class PopData(Data):
    """
    Subclass of Data specialized for analyzing population data from the 'PopChange.csv' file.

    Attributes:
    Inherits all attributes from the Data class.

    Methods:
    - show(): Displays menu options specific to population data analysis.
    - process_menu(): Processes user input for menu selections specific to 
    population data, setting the column (self.col) accordingly.
    """

    def __init__(self) -> None:
        super().__init__("src/PopChange.csv")

    def show(self) -> None:
        print("1) Pop Apr 1")
        print("2) Pop Jul 1")
        print("3) Change Pop")
        print("0) Exit Menu")

    def process_menu(self):
        super().process_menu()
        match self.selection:
            case 1:
                self.col = "Pop Apr 1"
            case 2:
                self.col = "Pop Jul 1"
            case 3:
                self.col = "Change Pop"
            case _:
                self.col = None

class HousingData(Data):
    """
    Subclass of Data specialized for analyzing housing data from the 'Housing.csv' file.

    Attributes:
    Inherits all attributes from the Data class.

    Methods:
    - show(): Displays menu options specific to housing data analysis.
    - process_menu(): Processes user input for menu selections specific 
    to housing data, setting the column (self.col) accordingly.
    - validate(): Validates the housing data by checking and correcting 
    invalid 'AGE' values where 'AGE' is less than 0.
    """

    def __init__(self) -> None:
        super().__init__("src/Housing.csv")
        self.validate()

    def show(self) -> None:
        print("1) Age")
        print("2) Bedrooms")
        print("3) Built")
        print("4) Rooms")
        print("5) Utility")
        print("0) Exit Menu")

    def process_menu(self):
        super().process_menu()
        match self.selection:
            case 1:
                self.col = "AGE"
            case 2:
                self.col = "BEDRMS"
            case 3:
                self.col = "BUILT"
            case 4:
                self.col = "ROOMS"
            case 5:
                self.col = "UTILITY"
            case _:
                self.col = None

    def validate(self):
        for i in range(len(self.df.loc[:, "AGE"])):
            if self.df.loc[i, "AGE"] < 0:
                self.df.loc[i, "AGE"] = datetime.now().year - self.df.loc[i, "BUILT"]


def main_menu():
    """
    Displays the main menu options for the data analysis application.

    Options:
    - 1: Population Data
    - 2: Housing Data
    - 0: Exit
    """

    print("1) Population Data")
    print("2) Housing Data")
    print("0) Exit")

def main():
    """
    Main function to execute the Python Data Analysis App.

    This function displays a welcome message and presents a menu 
    for selecting between Population Data, Housing Data, or exiting the application. 
    It continues to prompt the user for selections until they choose to exit. 
    
    Depending on the user's selection, it creates instances of 
    PopData or HousingData classes to perform data analysis. 

    Each data analysis session allows the user to select specific 
    columns for analysis and displays calculated statistical data.

    Upon exiting the application, a thank you message is displayed.

    Usage:
    Run this function to start the Python Data Analysis App.
    """

    print("*" * 50)
    print("Welcome to the Python Data Analysis App")
    print("*" * 50)
    while True:
        main_menu()
        user_selection = input_base.get_int_entry("")
        if user_selection == 0:
            break

        match user_selection:
            case 1:
                pop_data = PopData()
                while True:
                    pop_data.process_menu()
                    if pop_data.selection == 0:
                        break

                    if pop_data.calculate():
                        pop_data.show_data()
            case 2:
                hsg_data = HousingData()
                while True:
                    hsg_data.process_menu()
                    if hsg_data.selection == 0:
                        break

                    if hsg_data.calculate():
                        hsg_data.show_data()
            case _:
                print("\nInvalid Option Selected, Please Try Again\n")

    print("*" * 50)
    print("Thanks for using the Data Analysis App")
    print("*" * 50)

if __name__ == "__main__":
    main()
