"""Tests for Voter Module"""
import voter

def test_int_inputs(monkeypatch):
    """Tests the function get_int_entry for valid response"""
    test_cases = {'31':31, '0':0, '18':18, '120':120, '17':17, '121':121, 'asdf':None,'':None}
    for case, result in test_cases.items():
        monkeypatch.setattr('builtins.input', lambda _: case)
        x = voter.get_int_entry('')
        assert x == result

def test_string_inputs(monkeypatch):
    """Tests the function get_string_entry for valid response"""
    test_cases = ['Bob', 'Larry', '  ', '    Chuck   ', 'Curly', 'Mo']
    for case in test_cases:
        monkeypatch.setattr('builtins.input', lambda _: case)
        x = voter.get_string_entry('')
        assert x == case

def test_bool_inputs(monkeypatch):
    """Tests the function get_yes_no for valid response"""
    test_cases = {'y':True, 'yes':True, 'YES':True, 'n':False, 'N':False, 'no':False, 'No':False, \
                  'asdf':None, 'Hi':None}
    for case, result in test_cases.items():
        monkeypatch.setattr('builtins.input', lambda _: case)
        x = voter.get_yes_no('')
        assert x == result

def test_is_null_or_whitespace():
    """Tests the is_null_or_whitespace function"""
    test_cases = {"hi":False, "   Hi":False, "Hi.   ":False, "   Hi.  ":False,\
                  "     ":True, None:True, '':True}

    for case, result in test_cases.items():
        x = voter.is_null_or_whitespace(case)
        assert x == result

def test_get_info(monkeypatch):
    """Test all functions used in get_info class method for voter"""
    cases = [ \
        {
            'fName':('Bob',True),'lName':('Denver',True),\
            'age':('31',True),'us':('y',True),\
            'state':('MD',True),'zip':('21122',True),'all':(None,True)
        },
        {
            'fName':(' ',False),'lName':('Denver',True),\
            'age':('31',True),'us':('y',True),\
            'state':('MD',True),'zip':('21122',True),'all':(None,False)
        },
        {
            'fName':('Bob',True),'lName':('   ',False),\
            'age':('31',True),'us':('y',True),\
            'state':('MD',True),'zip':('21122',True),'all':(None,False)
        },
        {
            'fName':('Bob',True),'lName':('Denver',True),\
            'age':('17',False),'us':('y',True),\
            'state':('MD',True),'zip':('21122',True),'all':(None,False)
        },
        {
            'fName':('Bob',True),'lName':('Denver',True),\
            'age':('18',True),'us':('y',True),\
            'state':('MD',True),'zip':('21122',True),'all':(None,True)
        },
        {
            'fName':('Bob',True),'lName':('Denver',True),\
            'age':('120',True),'us':('y',True),\
            'state':('MD',True),'zip':('21122',True),'all':(None,True)
        },
        {
            'fName':('Bob',True),'lName':('Denver',True),\
            'age':('121',False),'us':('y',True),\
            'state':('MD',True),'zip':('21122',True),'all':(None,False)
        },
        {
            'fName':('Bob',True),'lName':('Denver',True),\
            'age':('31',True),'us':('n',False),\
            'state':('MD',True),'zip':('21122',True),'all':(None,False)
        },
        {
            'fName':('Bob',True),'lName':('Denver',True),\
            'age':('31',True),'us':('Q',False),\
            'state':('MD',True),'zip':('21122',True),'all':(None,False)
        },
        {
            'fName':('Bob',True),'lName':('Denver',True),\
            'age':('31',True),'us':('asdflksad',False),\
            'state':('MD',True),'zip':('21122',True),'all':(None,False)
        },
        {
            'fName':('Bob',True),'lName':('Denver',True),\
            'age':('31',True),'us':('y',True),\
            'state':('Pq',False),'zip':('21122',True),'all':(None,False)
        },
        {
            'fName':('Bob',True),'lName':('Denver',True),\
            'age':('31',True),'us':('y',True),\
            'state':('FL',True),'zip':('21122',True),'all':(None,True)
        },
        {
            'fName':('Bob',True),'lName':('Denver',True),\
            'age':('31',True),'us':('y',True),\
            'state':('ZZ',False),'zip':('21122',True),'all':(None,False)
        },
        {
            'fName':('Bob',True),'lName':('Denver',True),\
            'age':('31',True),'us':('y',True),\
            'state':('MD',True),'zip':('   ',False),'all':(None,False)
        },
        {
            'fName':('Bob',True),'lName':('Denver',True),\
            'age':('31',True),'us':('y',True),\
            'state':('MD',True),'zip':('asdfr',False),'all':(None,False)
        },
        {
            'fName':('Bob',True),'lName':('Denver',True),\
            'age':('31',True),'us':('y',True),\
            'state':('MD',True),'zip':('1234',False),'all':(None,False)
        },
        {
            'fName':('Bob',True),'lName':('Denver',True),\
            'age':('31',True),'us':('y',True),\
            'state':('MD',True),'zip':('12345678',False),'all':(None,False)
        }
    ]

    for case in cases:
        new_voter = voter.Voter()
        assert new_voter.set_first(case['fName'][0]) is case['fName'][1]
        assert new_voter.set_last(case['lName'][0]) is case['lName'][1]
        monkeypatch.setattr('builtins.input', lambda _: case['age'][0])
        assert new_voter.set_age(voter.get_int_entry('')) is case['age'][1]
        monkeypatch.setattr('builtins.input', lambda _: case['us'][0])
        assert new_voter.set_us(voter.get_yes_no('')) is case['us'][1]
        monkeypatch.setattr('builtins.input', lambda _: case['state'][0])
        assert new_voter.set_state(voter.get_string_entry('')) is case['state'][1]
        monkeypatch.setattr('builtins.input', lambda _: case['zip'][0])
        assert new_voter.set_zip(voter.get_string_entry('')) is case['zip'][1]

        assert new_voter.validate() is case['all'][1]
        