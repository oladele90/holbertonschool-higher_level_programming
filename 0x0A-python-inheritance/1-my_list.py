#!/usr/bin/python3
"""print sorted module"""


class MyList(list):
    """defines class called Mylist"""

    def __init__(self):
        """initializes variable"""
        
    def print_sorted(self):
        """print sorted module prints sorted list of ints in ascending order"""
        print(sorted(self))