#!/usr/bin/python3
def uniq_add(my_list=[]):
    list_unq = set(my_list)
    num = 0

    for n in list_unq:
        num += n

    return (num)
