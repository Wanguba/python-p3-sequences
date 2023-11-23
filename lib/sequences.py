#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        print([])  # Print an empty list when length is 0
    else:
        fib_list = [0]
        while len(fib_list) < length:
            fib_list.append(fib_list[-1] + fib_list[-2] if len(fib_list) > 1 else 1)
        print(fib_list)

