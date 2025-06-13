#!/usr/bin/python3
def pow(a, b):
    if b == 0:
        return 1
    else:
        temp = a
        for i in range (b-1):
            a *= temp
        return a
