#!/usr/bin/python3
"""
This module defines MyList class that inherits from list
"""


class MyList(list):
    """Custom list that can print itself sorted"""
    def print_sorted(self):
        """Prints the list, but sorted in ascending order"""
        print(sorted(self))
