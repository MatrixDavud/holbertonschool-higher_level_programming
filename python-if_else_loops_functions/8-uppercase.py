#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            i = chr(ord(i) - 32)
        print("{}".format(i), end="")
print(str)
