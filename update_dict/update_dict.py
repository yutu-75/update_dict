
def update_dict(d1,d2):
    '''
    :param d1: Default nested dictionary,默认嵌套字典;
    :param d2: Updated dictionary 需要更新的字典;
    :return d1:
    Return a dict merged from default and custom

    # >>> recursive_update('a', 'b')
    Traceback (most recent call last):
        ...
    TypeError: Params of update_dict should be dicts

    # >>> update_dict({'a':{"b":{"c":{"d"}}},"e":{"e1":{"e5":'qwq'}},"e5": {},"ss":"1111"},
    {"e5":'www',"ss":"ssss",'c':{},'ss1':'ss'})
    {'a': {'b': {'c': {}}}, 'e': {'e1': {'e5': 'www'}}, 'e5': 'www', 'ss': 'ssss'

    # >>> update_dict({'a':{"b":{"c":{"d":'c'}}},"e":{"e1":{"e5":'qwq'}},"e5": {},"ss":"1111"},{"d":'www'})
    {'a': {'b': {'c': {'d': 'www'}}}, 'e': {'e1': {'e5': 'qwq'}}, 'e5': {}, 'ss': '1111'}

    # >>> update_dict({'a': {'c': 1, 'd': {}}, 'b': 4}, {'a': 2})
    {'a': 2, 'b': 4}
    '''

    if not isinstance(d1, dict) or not isinstance(d2, dict):
        raise TypeError('Params of update_dict should be dicts')
    for i in d1:
        if d2.get(i, None) is not None:
            d1[i] = d2[i]
        if isinstance(d1[i], dict):
            update_dict(d1[i],d2)
            print(d1[i])
    return d1



