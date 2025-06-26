#!/usr/bin/python3
"""Pascal triangle module."""


def factorial(n):
    """Return the factorial of n with recursive function."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)


def n_choose_k(n, k):
    """Return the value of C(n, k) for binomial coefficients."""
    return int(factorial(n) / ((factorial(k)) * factorial(n-k)))


def pascal_triangle(n):
    """Return list of lists for n size pascal triangle."""
    final_pscl_lst = []
    for i in range(n):
        crrnt_pscl_lst = []
        for j in range(i+1):
            bin_coeff = n_choose_k(i, j)
            crrnt_pscl_lst.append(bin_coeff)
        final_pscl_lst.append(crrnt_pscl_lst)
    return final_pscl_lst
