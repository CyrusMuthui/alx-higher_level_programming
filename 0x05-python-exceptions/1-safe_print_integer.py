#!/usr/bin/python3

def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return (True)
    except Exception as ch:
        return (False)
