#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    list_n = []
    for i in range(0, list_length):
        try:
            divout = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            divout = 0
        except ZeroDivisionError:
            print("division by 0")
            divout = 0
        except IndexError:
            print("out of range")
            divout = 0
        finally:
            list_n.append(divout)
    return (list_n)
