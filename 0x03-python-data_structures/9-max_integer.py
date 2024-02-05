#!/usr/bin/python3
def max_integer(my_list=[]):
    list_leng = len(my_list)

    if list_leng == 0:
        return None
    else:
        max_val = my_list[0]
        for i in range(1, list_leng):
            if my_list[i] > max_val:
                max_val = my_list[i]
        return max_val
