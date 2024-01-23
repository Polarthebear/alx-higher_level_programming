#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        divout = a / b
    except (TypeError, ZeroDivisionError):
        divout = None
    finally:
        print("Inside Result: {}".format(divout))
    return (divout)
