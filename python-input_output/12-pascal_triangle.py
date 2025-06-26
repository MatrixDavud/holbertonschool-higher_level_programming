#!/usr/bin/python3
"""Pascal triangle module."""


def pascal_triangle(n):
    """Return list of lists for n size pascal triangle."""
    final_pscl_lst = []
    for i in range(n):
        crrnt_pscl_lst = []
        my_int = 11 ** i
        my_int_str = str(my_int)
        for j in range(len(my_int_str)):
            crrnt_pscl_lst.append(my_int_str[j])
        final_pscl_lst.append(crrnt_pscl_lst)

    return final_pscl_lst
