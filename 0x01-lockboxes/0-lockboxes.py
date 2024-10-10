#!/usr/bin/python3


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be unlocked.

    Args:
        boxes: A lost of lists.

    Returns:
        True if all boxes can be unlocked, otherwise False.
    """

    n = len(boxes)
    visited = [False] * n   # To track visited boxes
    visited[0] = True       # Box 0 is already unlocked
    stack = [0]             # Start with box 0

    while stack:
        box = stack.pop()
        for key in boxes[box]:
            if key < n and not visited[key]:
                visited[key] = True
                stack.append(key)

    return all(visited)
