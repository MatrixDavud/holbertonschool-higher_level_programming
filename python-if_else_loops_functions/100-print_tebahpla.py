#!/usr/bin/python3
count = 122
while count > 96:
    if count % 2 == 0:
        print(chr(count), end='')
        count -= 1
    elif count % 2 == 1:
        print(chr(count - 32), end='')
        count -= 1