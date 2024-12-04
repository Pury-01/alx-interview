#!/usr/bin/python3


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be unlocked.

    Args:
        boxes: A lost of lists.

    Returns:
        True if all boxes can be unlocked, otherwise False.
    """

    if not boxes or not isinstance(boxes, list):
        return False

    n = len(boxes)
    unlocked = {0}
    keys = set(boxes[0])

    while keys:
        key = keys.pop()
        if key < n and key not in unlocked:
            unlocked.add(key)
            keys.update(boxes[key])

    return len(unlocked) == n
