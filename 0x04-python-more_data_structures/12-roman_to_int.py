#!/usr/bin/python3
def sub(list_num):
    subto = 0
    max_list = max(list_num)

    for i in list_num:
        if max_list > i:
            subto += i

    return (max_list - subto)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_key = list(roman.keys())

    rom_last = 0
    num = 0
    list_num = [0]

    for ch in roman_string:
        for r_num in list_key:
            if r_num == ch:
                if roman.get(ch) <= rom_last:
                    num += sub(list_num)
                    list_num = [roman.get(ch)]
                else:
                    list_num.append(roman.get(ch))

                rom_last = roman.get(ch)
    num += sub(list_num)

    return (num)
