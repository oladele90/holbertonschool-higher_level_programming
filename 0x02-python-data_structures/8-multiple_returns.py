#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        letter = sentence[0]
        length = len(sentence)
    else:
        letter = None
        length = 0
    new = (length, letter)
    return new
