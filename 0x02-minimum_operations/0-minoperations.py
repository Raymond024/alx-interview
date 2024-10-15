#!/usr/bin/python3
""" Module for 0-minoperations"""

def minOperations(n):
    """
    Gets fewest # of operations needed to result in exactly n H characters
    """
    # all outputs should be at least 2 char: (min, Copy All => Paste)
    if (n < 2):
        return 0
    op, roo = 0, 2
    while roo <= n:
        # if n evenly divides by root
        if n % roo == 0:
            # total even-divisions by root = total operations
            op += roo
            # set n to the remainder
            n = n / roo
            # reduce root to find remaining smaller vals that evenly-divide n
            roo -= 1
        # increment root until it evenly-divides n
        roo += 1
    return op
