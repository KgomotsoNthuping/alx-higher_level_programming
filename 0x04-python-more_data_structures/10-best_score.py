#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    integer = 0
    for key, amt in a_dictionary.items():
        if amt > integer:
            integer = amt
    for key, amt in a_dictionary.items():
        if amt == integer:
            return key
