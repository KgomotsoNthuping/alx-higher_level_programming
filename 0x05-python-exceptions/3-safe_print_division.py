#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        div = a / b
    except (ZeroDivisionError, TypeError):
        div = None
    finally:
        print("Result: {}".format(div))
    return (div)