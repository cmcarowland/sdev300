import lab2
import random

def _menu(monkeypatch):
    """This function tests different inputs for the menu.

        test_cases:
            Contains the case and expected result
    """
    test_cases = {'1':0, '2':0, '3':0, '4':0, '5':0, '6':2, '0':1, 'a':2,'hello':2}
    for k,v in test_cases.items():
        monkeypatch.setattr('builtins.input', lambda _: k)
        assert lab2.menu() == v

def test_calculate_percentage():
    """
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
