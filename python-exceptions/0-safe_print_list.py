#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        _ = my_list[x]
        for i in range(x):
            print(my_list[i], end="")
        print()
        return x
    except IndexError:
        i = 0
        for j in my_list:
            print(j, end="")
            i += 1
        print()
        return i
