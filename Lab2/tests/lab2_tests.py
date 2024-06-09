"""
Test module for the lab2 module.

This module contains unit tests for the functions 
implemented in the lab2 module.

Functions:
    test_calculate_percentage: Test the calculate_percentage function.
    test_get_password: Test the get_password function.
    test_calculate_triangle: Test the calculate_triangle function.
    test_calculate_cylinder: Test the 
        calculate_volume_of_cylinder function.
    _menu: Test the _menu function.

Each test function checks different functionalities 
of the lab2 module to ensure they work as expected under various conditions.

Raises:
    AssertionError: If any of the test cases fail, 
    indicating a mismatch between expected and actual outcomes.
"""

import random
import lab2

def tes_menu(monkeypatch):
    """
    Test the _menu function.

    This function tests different inputs for the menu.

    Raises:
        AssertionError: If the returned result from the
         menu does not match the expected value.
    """

    test_cases = {'1':0, '2':0, '3':0, '4':0, '5':0, '6':2, '0':1, 'a':2,'hello':2}
    for k,v in test_cases.items():
        monkeypatch.setattr('builtins.input', lambda _: k)
        assert lab2.menu() == v

def test_calculate_percentage():
    """
    Test the calculate_percentage function.

    The function tests various scenarios of calculate_percentage function.

    Raises:
        AssertionError: If the calculated percentage does 
        not match the expected value.
    """

    test_cases = [
        {(22, 57):0.38596491228070173},
        {(10, 50):0.2},
        {(1, 50):0.02},
        {(-1, 50):-1},
        {(100, -50):-1},
        {(100, 50):2},
    ]

    for case in test_cases:
        for k,v in case.items():
            assert lab2.calculate_percentage(k[0], k[1]) == v

def test_get_password():
    """
    Test the get_password function.

    The function tests various scenarios of the get_password function.

    Raises:
        AssertionError: If the generated password does 
        not match the expected value.
    """

    test_cases = [
        [10, False, False, False, False, None],
        [0, True, False, False, False, None],
        [1, True, False, False, False, "S"],
        [2, True, False, False, False, "BN"],
        [10, True, False, False, False, "PSAGOPIUZF"],
        [15, False, True, False, False, "bqpkchxlbnetlmn"],
        [20, False, False, True, False, "44724527379609032348"],
        [25, False, False, False, True, "&-/$&+)(\'(\"+*&.)#.$'$!!(%"],
        [25, True, False, False, True, "-E)FJY+X-JHG#KMW\"!#PRJ.(L"],
        [25, False, True, False, True, "hr$tkll%wu\"oa)cvupfq#z,ky"],
        [25, False, False, True, True, "&,7.'8'&*&25&,%#4$()\"(#&-"],
        [30, False, True, True, True, "k92g0ca28edwfjg#35i31.62v+q/)3"],
        [50, True, True, True, True, "2q%%TepEZ.,9DOl3flLF/)NkU9Su/zYsXK.Y2aMn7%25*ai/uO"],
    ]

    random.seed(10)
    for case in test_cases:
        assert lab2.get_password(case[0], case[1], case[2], case[3], case[4]) == case[5]

def test_calculate_triangle():
    """
    Test the calculate_triangle function.

    The function tests various scenarios 
    of the calculate_triangle function.

    Raises:
        AssertionError: If the calculated length of the 
        third side does not match the expected value.
    """

    test_cases = [
        [11, 8, 37, 6.666344592929206],
        [None, 5, 20, -1],
        [10, None, 20, -1],
        [10, 20, None, -1],
        [10, 20, 50, 15.584766797273042],
        [-10, 20, 50, -1],
        [10, -20, 50, -1],
        [10, 20, -50, -1],
        [10, 10, 60, 9.999999999999998],
    ]

    random.seed(10)
    for case in test_cases:
        assert lab2.calculate_triangle(case[0], case[1], case[2]) == case[3]

def test_calculate_cylinder():
    """
    Test the calculate_volume_of_cylinder function.

    The function tests various scenarios of the
     calculate_volume_of_cylinder function.

    Raises:
        AssertionError: If the calculated volume 
        of the cylinder does not match the expected value.
    """

    test_cases = [
        [11, 8, 3041.06168867492],
        [None, 8, -1],
        [None, None, -1],
        [200, None, -1],
        [200, 1, 125663.70614359173],
        [2, 2, 25.132741228718345],
    ]

    random.seed(10)
    for case in test_cases:
        assert lab2.calculate_volume_of_cylinder(case[0], case[1]) == case[2]
