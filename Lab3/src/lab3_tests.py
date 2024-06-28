import json
import lab3
from state import State


states = []
j_data = {}
with open('../state_data.json', 'r', encoding="utf-8") as i_file:
    j_data = json.load(i_file)

for s in j_data:
    state = State()
    state.set_name(s['state'])
    state.population = int(s['population'])
    state.flower = s['flower']
    states.append(state)

del j_data

def test_sort_by_name():
    """
    Sorts the state list and checks to make sure they are sorted by name
    """
    sorted_states = lab3.sort_by_name(states)
    i = 0
    j = 1
    while j < len(sorted_states):
        k = 0
        while sorted_states[i].name[k] == sorted_states[j].name[k]:
            k += 1

        assert sorted_states[i].name[k] < sorted_states[j].name[k]
        i += 1
        j += 1

def test_sort_by_pop():
    """
    Sorts the state list and checks to make sure they are sorted by population
    """
    sorted_states = lab3.sort_by_pop(states)
    i = 0
    j = 1
    while j < len(sorted_states):
        assert sorted_states[i].population > sorted_states[j].population

        i += 1
        j += 1

def test_set_state_population():
    """
    Tests setting the population to various values
    """
    sorted_states = lab3.sort_by_pop(states)
    test_cases = [[100, True], [-1, False],[-100, False],[200,True], [600000, True]]
    for test in test_cases:
        assert sorted_states[0].set_population(test[0]) is test[1]


def test_int_inputs(monkeypatch):
    """Tests the function get_int_entry for valid response"""
    test_cases = {'31':31, '0':0, '18':18, '120':120, '17':17, '121':121, 'asdf':None,'':None}
    for case, result in test_cases.items():
        monkeypatch.setattr('builtins.input', lambda _: case)
        x = lab3.get_int_entry('')
        assert x == result

def test_string_inputs(monkeypatch):
    """Tests the function get_string_entry for valid response"""
    test_cases = ['Bob', 'Larry', '  ', '    Chuck   ', 'Curly', 'Mo']
    for case in test_cases:
        monkeypatch.setattr('builtins.input', lambda _: case)
        x = lab3.get_string_entry('')
        assert x == case

def test_bool_inputs(monkeypatch):
    """Tests the function get_yes_no for valid response"""
    test_cases = {'y':True, 'yes':True, 'YES':True, 'n':False, 'N':False, 'no':False, 'No':False, \
                  'asdf':None, 'Hi':None}
    for case, result in test_cases.items():
        monkeypatch.setattr('builtins.input', lambda _: case)
        x = lab3.get_yes_no('')
        assert x == result

def test_is_null_or_whitespace():
    """Tests the is_null_or_whitespace function"""
    test_cases = {"hi":False, "   Hi":False, "Hi.   ":False, "   Hi.  ":False,\
                  "     ":True, None:True, '':True}

    for case, result in test_cases.items():
        x = lab3.is_null_or_whitespace(case)
        assert x == result

def test_find_first():
    """Tests the find first function"""
    test_cases = [["MD","Maryland", True],
                  ["asdf", None, False],
                  ["Vermont", "Vermont", True],
                  ["200",None,False],
                  ["600000",None, False],
                  ["", None, False]]
    for case in test_cases:
        print(case)
        state_name = case[0]
        s = lab3.find_first(x for x in states \
                if x.name == state_name or x.abbreviation == state_name.upper())

        assert isinstance(s, lab3.State) == case[2]
        if s is not None:
            assert s.name == case[1]
