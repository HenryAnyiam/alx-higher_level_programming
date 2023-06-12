#!/usr/bin/python3

"""1-my_list module with class inheriting from list"""


class MyList(list):
    """MyList inherits from class list

    Adds new method print_sorted

    """
    def print_sorted(self):
        """prints a sorted version of the object"""

        new = self.copy()
        new.sort()
        print(new)
