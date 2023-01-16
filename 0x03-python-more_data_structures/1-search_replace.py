#!/usr/bin/python3
def search_replace(my_list, search, replace):
    i = -1
    try:
        while True:
            i = my_list.index(search, i + 1)
            my_list[i] = replace
    except ValueError:
        pass
