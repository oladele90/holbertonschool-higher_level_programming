#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    list_a = list(tuple_a)
    list_b = list(tuple_b)
    for i in range(2):
        list_a.append(0)
        list_b.append(0)
    list_t= [list_a[x] + list_b[x] for x in range(2)]
    new_tuple = tuple(list_t)
    return new_tuple
