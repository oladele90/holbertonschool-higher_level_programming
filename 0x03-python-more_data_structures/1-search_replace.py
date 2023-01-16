#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = my_list.copy()
    i = -1
    try:
        while True:
            i = my_list.index(search, i + 1)
            new[i] = replace
    except ValueError:
        pass
    return new
