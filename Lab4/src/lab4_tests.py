"""
"""
from io import StringIO

import numpy as np
import pytest

import lab4
import input_base

def test_get_phone_num():
    """Tests the function get_phone_num for valid response"""
    test_cases = [['123-456-7890',True],
                  ['asd-123-4567',False],
                  ['1234-456-789', False],
                  ['123-4566-789', False],
                  ['927-341-6602', True]]
    for case in test_cases:
        assert case[1] == lab4.validate_phone_number(case[0])

def test_get_zip_code(monkeypatch):
    """Tests the function get_zip_code for valid response"""

    # Valid inputs
    valid_cases = [
        ('12345-6789', '12345-6789'),
        ('11111-1111', '11111-1111'),
        ('00000-0000', '00000-0000'),
        ('99999-9999', '99999-9999'),
    ]

    for input_str, expected_output in valid_cases:
        mock_input = StringIO(input_str + '\n')
        monkeypatch.setattr('sys.stdin', mock_input)
        assert lab4.get_zip_code() == expected_output

    # Invalid inputs
    invalid_cases = [
        ('123456789', 'Your zip code is not in the correct format. Please Try Again:'),
        ('12345', 'Your zip code is not in the correct format. Please Try Again:'),
        ('abcdef-1234', 'Your zip code is not in the correct format. Please Try Again:'),
        ('12345-678', 'Your zip code is not in the correct format. Please Try Again:'),
        ('12345-67890', 'Your zip code is not in the correct format. Please Try Again:'),
        ('12345-67890', 'Your zip code is not in the correct format. Please Try Again:')
    ]

    for input_str, expected_output in invalid_cases:
        mock_input = StringIO(input_str + '\n')
        monkeypatch.setattr('sys.stdin', mock_input)
        with pytest.raises(EOFError):
            assert lab4.get_zip_code() != input_str

def test_get_matrix(monkeypatch):
    # Valid inputs
    valid_cases = [
        ('first', '1 2 3\n4 5 6\n7 8 9\n', np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])),
        ('second', '9 8 7\n6 5 4\n3 2 1\n', np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])),
        ('third', '0 0 0\n0 0 0\n0 0 0\n', np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])),
    ]

    for number, input_str, expected_matrix in valid_cases:
        mock_input = StringIO(input_str)
        monkeypatch.setattr('sys.stdin', mock_input)
        assert np.array_equal(lab4.get_matrix(number), expected_matrix)

    # Invalid inputs
    invalid_cases = [
        # Incorrect number of elements in one line
        ('first', '1 2\n4 5 6\n7 8 9\n', EOFError,
         "Incorrect format, enter 3 numbers separated with a space"),  
        # Non-numeric character in input
        ('second', '9 8 7\n6 x 4\n3 2 1\n', EOFError,
         "Incorrect format, enter 3 numbers separated with a space"),  
        # Incomplete input (not enough lines)
        ('third', '1 2 3\n4 5 6\n', EOFError,
         "Enter your third 3x3 matrix one line at a time separated by space (1 2 3)"),  
    ]

    for number, input_str, error_type, _ in invalid_cases:
        mock_input = StringIO(input_str)
        monkeypatch.setattr('sys.stdin', mock_input)
        print(mock_input)
        with pytest.raises(error_type):
            lab4.get_matrix(number)

def test_int_inputs(monkeypatch):
    """Tests the function get_int_entry for valid response"""
    test_cases = {'31':31, '0':0, '18':18, '120':120, '17':17, '121':121, 'asdf':None,'':None}
    for case, result in test_cases.items():
        monkeypatch.setattr('builtins.input', lambda _: case)
        x = input_base.get_int_entry('')
        assert x == result

def test_string_inputs(monkeypatch):
    """Tests the function get_string_entry for valid response"""
    test_cases = ['Bob', 'Larry', '  ', '    Chuck   ', 'Curly', 'Mo']
    for case in test_cases:
        monkeypatch.setattr('builtins.input', lambda _: case)
        x = input_base.get_string_entry('')
        assert x == case

def test_bool_inputs(monkeypatch):
    """Tests the function get_yes_no for valid response"""
    test_cases = {'y':True, 'yes':True, 'YES':True, 'n':False, 'N':False, 'no':False, 'No':False, \
                  'asdf':None, 'Hi':None}
    for case, result in test_cases.items():
        monkeypatch.setattr('builtins.input', lambda _: case)
        x = input_base.get_yes_no('')
        assert x == result

def test_is_null_or_whitespace():
    """Tests the is_null_or_whitespace function"""
    test_cases = {"hi":False, "   Hi":False, "Hi.   ":False, "   Hi.  ":False,\
                  "     ":True, None:True, '':True}

    for case, result in test_cases.items():
        x = input_base.is_null_or_whitespace(case)
        assert x == result
