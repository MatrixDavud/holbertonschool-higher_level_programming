#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    new_dict = {k: value if key in a_dictionary else value for k in a_dictionary}
    return new_dict
