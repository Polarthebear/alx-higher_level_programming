#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a_leng = len(tuple_a)
    tuple_b_leng = len(tuple_b)

    if tuple_a_leng > 2:
        tuple_a = (tuple_a[0], tuple_a[1])
    if tuple_b_leng > 2:
        tuple_b = (tuple_b[0], tuple_b[1])
    if tuple_a_leng == 1:
        tuple_a = (tuple_a[0], 0)
    if tuple_b_leng == 1:
        tuple_b = (tuple_b[0], 0)
    if tuple_a_leng == 0:
        tuple_a = (0, 0)
    if tuple_b_leng == 0:
        tuple_b = (0, 0)
    summ = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])

    return summ
