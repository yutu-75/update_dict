=====================
update_dict
=====================



A Python module who does recursive update work on 2 dicts.

Usage
=====

Installation
------------



    pip install update_dict


Examples
--------



    # >>> from update_dict import update_dict

    # >>> update_dict({'a':{"b":{"c":{"d"}}},"e":{"e1":{"e5":'qwq'}},"e5": {},"ss":"1111"},
    {"e5":'www',"ss":"ssss",'c':{},'ss1':'ss'})
    {'a': {'b': {'c': {}}}, 'e': {'e1': {'e5': 'www'}}, 'e5': 'www', 'ss': 'ssss'

    # >>> update_dict({'a':{"b":{"c":{"d":'c'}}},"e":{"e1":{"e5":'qwq'}},"e5": {},"ss":"1111"},{"d":'www'})
    {'a': {'b': {'c': {'d': 'www'}}}, 'e': {'e1': {'e5': 'qwq'}}, 'e5': {}, 'ss': '1111'}

    # >>> update_dict({'a': {'c': 1, 'd': {}}, 'b': 4}, {'a': 2})
    {'a': 2, 'b': 4}
    '''

Why?
====

...............
License
=======
`MIT <./LICENSE.txt>`_
