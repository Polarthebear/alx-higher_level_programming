#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dir_new = a_dictionary.copy()
    list_key = list(dir_new.keys())

    for n in list_key:
        dir_new[n] *= 2

    return (dir_new)
