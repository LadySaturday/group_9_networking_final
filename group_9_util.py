'''
Group 9 - Lab 13
'''
import time
from os import system
import random
#



__colorful = True






def ok(data) -> dict:
    '''Wraps data as OK'''
    return response(data)

def response(data, code=200, msg='OK') -> dict:
    '''wraps data in a payload with a message & code'''
    payload = {
        'meta': { 'code': code, 'msg': msg },
        'data': data
    }
    return payload

def __wrap_var(var, colorful):
    '''Wraps a variable in a color (and quotes if it's a string)'''
    t = type(var)
    if t is str:
        # wraps string in quotes and makes green
        if colorful:
            return f'\x1b[32m"{var}"\x1b[0m'
        else: return f'{var}'

    if colorful:
        if (t is int) or (t is float):
            # makes number orange
            return f'\x1b[33m{var}\x1b[0m'
        elif t is bool:
            # makes boolean blue
            return f'\x1b[34m{var}\x1b[0m'
    
    return f'{var}'


def __print_dict(d: dict, indent=2, colorful=True):
    '''Iters through all elements in a dict and prints the key/value.
    is Recursive, and will call __print_dict or __print_list if needed
    '''

    spaces = ' ' * indent  # creates a standard set of
    for key, val in d.items(): # loops through all items
        k = __wrap_var(key, colorful)
        t = type(val)

        # checks if val is dict/list and recursively calls __print_dict/__print_list
        if t is dict:
            print(f'{spaces}{k}: {{')  # opens dict
            __print_dict(val, indent=indent+2, colorful=colorful) # recursive call inwards
            print(f'{spaces}}},')  # closes dict
        elif t is list:
            print(f'{spaces}{k}: [')  # opens list
            __print_list(val, indent=indent+2, colorful=colorful) # recursive call inwards
            print(f'{spaces}],')  # closes list
        else:
            print(f'{spaces}{k}: {__wrap_var(val, colorful)},')  # prints the key standard


def __print_list(ls: list, indent=2, colorful=True):
    '''Iters through all list items and prints the them.
    is Recursive, and will call __print_dict or __print_list if needed
    '''
    spaces = ' ' * indent
    for i in ls:
        if isinstance(i, list):
            print(f'{spaces}[')  # opens list
            __print_list(i, indent=indent+2, colorful=colorful)
            print(f'{spaces}],')  # closes list
        elif isinstance(i, dict):
            print(f'{spaces}{{')  # opens dict
            __print_dict(i, indent=indent+2, colorful=colorful)  # recursive call inwards
            print(f'{spaces}}},')  # closes dict
        else:
            print(f"{spaces}{__wrap_var(i, colorful)},")


def print_data(payload: dict, colorful=True):
    '''
    Could have printed the data using print(payload),
    Will crash with a circular structure.
    When colorful is set to True the variables will be color coded.
    Colors don't work on all consoles, unfortunately.
    VSCode is a great example to show it off
    '''
    # print(payload)
    if colorful:
        # calls color on system to make sure colors work
        system('color')
    print('{')
    __print_dict(payload, colorful=colorful)
    print('}')





def main():
    print_data({'r': 3, 'rrrrrr': {3: 22, 44: True}, 432444: [3433, 4324, "String"], 'g': [{3:33, 4:44}]})


if __name__ == '__main__':
    main()
