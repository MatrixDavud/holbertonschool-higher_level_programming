#!/usr/bin/python3
import sys
from calculator_1 import (add, sub, mul, div)

if __name__ == "__main__":
    try:
        if len(sys.argv) != 4:
            print(f"Usage: {sys.argv[0]} <a> <operator> <b>")
            sys.exit(1)
        a = sys.argv[1]
        b = sys.argv[3]
        operator = sys.argv[2]
        res = None
        if operator == '+':
            res = add(int(a), int(b))
            print(f"{a} {operator} {b} = {res}")
        elif operator == '-':
            res = sub(int(a), int(b))
            print(f"{a} {operator} {b} = {res}")
        elif operator == '*':
            res = mul(int(a), int(b))
            print(f"{a} {operator} {b} = {res}")
        elif operator == '/':
            res = div(int(a), int(b))
            print(f"{a} {operator} {b} = {res}")
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
    except Exception:
        sys.exit(1)
