"""Py tests for Lab 5"""

import lab5

import input_base

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

def test_data_calaulate():
    """Tests the calculate function for population data
    1) Tests the None type
    2) Tests a valid column
    3) Tests a nonsense column
    """
    pop_data = lab5.PopData()
    assert pop_data.calculate() is False
    pop_data.col = "Pop Apr 1"
    assert pop_data.calculate() is True
    pop_data.col = "ASDFAS"
    assert pop_data.calculate() is False

def test_data_calaulate_housing():
    """Tests the calculate function for housing data
    1) Tests the None type
    2) Tests a valid column
    3) Tests a nonsense column
    """
    h_data = lab5.HousingData()
    assert h_data.calculate() is False
    h_data.col = "BUILT"
    assert h_data.calculate() is True
    h_data.col = "ASDFAS"
    assert h_data.calculate() is False
