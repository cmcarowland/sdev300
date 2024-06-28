"""
"""
import webbrowser
import pandas as pd

import input_base

class PopData():
    """asdf"""
    def __init__(self) -> None:
        self.col = ""
        self.selection = 0
    
    def show(self) -> None:
        print("1) Pop Apr 1")
        print("2) Pop Jul 1")
        print("3) Change Pop")
        print("0) Exit Menu")

    def get_data(self) -> None:
        self.show()
        self.selection = input_base.get_int_entry("")
        match self.selection:
            case 1:
                self.col = "Pop Apr 1"
            case 2:
                self.col = "Pop Jul 1"
            case 3:
                self.col = "Change Pop"

    def calculate(self):
        df = pd.read_csv("src/PopChange.csv")
        print(f"Count: {df.loc[:, self.col].count()}")
        print(f"Mean: {df.loc[:, self.col].mean()}")
        print(f"Standard Deviation: {df.loc[:, self.col].std()}")
        min = df.loc[:, self.col].min()
        print(f"Min: {min}")
        max = df.loc[:, self.col].max()
        print(f"Max: {max}")
        df.plot.hist(column=[self.col], bins=10).get_figure().savefig('HistData.png')
        # webbrowser.open('HistData.png')

def main_menu():
    """asdf"""
    print("1) Population Data")
    print("2) Housing Data")
    print("0) Exit")

def main():
    """asdf"""
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
                    pop_data.get_data()
                    if pop_data.selection == 0:
                        break

                    pop_data.calculate()

    print("*" * 50)
    print("Thanks for using the Data Analysis App")
    print("*" * 50)
                    

if __name__ == "__main__":
    main()
