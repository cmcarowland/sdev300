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
