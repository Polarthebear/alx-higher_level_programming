#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    list_key = list(a_dictionary.keys())

    for value_del in list_key:
        if value == a_dictionary.get(value_del):
            del a_dictionary[value_del]

    return (a_dictionary)
