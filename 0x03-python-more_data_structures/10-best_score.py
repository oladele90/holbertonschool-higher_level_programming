#!/usr/bin/python3
def best_score(a_dictionary):
    bs = 0
    if not a_dictionary:
        return None
    key = ""
    for i in a_dictionary:
        if a_dictionary[i] > bs:
            bs = a_dictionary[i]
            key = i
    return key
