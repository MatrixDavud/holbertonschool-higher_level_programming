#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = list(my_list)
    if idx < 0 or idx >= len(my_list):
        return new_list
    else:
        new_list.pop(idx)
        new_list.insert(idx, element)
        return new_list
