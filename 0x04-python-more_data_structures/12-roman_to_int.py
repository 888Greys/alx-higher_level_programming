#!/usr/bin/python3
def to_subtract(list_num):
    to_sub = 0
    max_list = max(list_num)

    for num in list_num:
        if max_list > num:
            to_sub += num

    return (max_list - to_sub)


def roman_to_int(romanian_string):
    if not romanian_string:
        return 0

    if not isinstance(romanian_string, str):
        return 0

    rom_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_keys = list(rom_n.keys())

    num = 0
    last_rom = 0
    list_num = [0]

    for ch in romanian_string:
        for r_num in list_keys:
            if r_num == ch:
                if rom_n.get(ch) <= last_rom:
                    num += to_subtract(list_num)
                    list_num = [rom_n.get(ch)]
                else:
                    list_num.append(rom_n.get(ch))

                last_rom = rom_n.get(ch)

    num += to_subtract(list_num)

    return (num)
# This code actually worked i dont even know why
