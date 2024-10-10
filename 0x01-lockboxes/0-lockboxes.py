#!/usr/bin/python3
"""
Determine if all boxes can be opened
Using prototype: def canUnlockAll(boxes)
"""


def canUnlockAll(boxes):
    """
    Check if boxes can be unlocked
    """
    for key in range(1, len(boxes) - 1):
        ctrl = False
        for index in range(len(boxes)):
            ctrl = (key in boxes[index] and key != index)
            if ctrl:
                break
        if ctrl is False:
            return ctrl
    return True
