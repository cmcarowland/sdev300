"""
Module to collect and display favorite artists.

This module allows users to input their favorite artists and
 display them.

Usage:
    - Run the module, and it will prompt the user to enter their name.
    - Then, the user can input their favorite artists one by one.
    - Once the user is done inputting artists 
        (by entering an empty string), 
        the module will display the list of favorite artists.
"""

artists:list = []
yourName = input("What is your name?")
print("Enter your favorite artists:")
while True:
    if len(artist := input()) == 0:
        break
    artists.append(artist)
print("Your favorite artists are:")
for art in artists:
    print(f'{art}')
