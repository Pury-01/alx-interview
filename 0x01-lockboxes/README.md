# Lockboxes Algorithm in Python

## Problem Description
You are given **n** locked boxes, each numbered from **0** to **n-1**.
Each box contains keys to other boxes, and box **0** is unlocked. The task is to determine if all boxes can be opened.

Function Prototype:
```
def canUlockAll(boxes):
# boxes: List of lists, where each inner list contains integers (keys)
# Returns: True if all boxes can be unlocked, else False.
```

### Example:
```
boxes = [[1], [2], [3], [4], []]
print(canUlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))\
```

## Approach: Depth-First search (DFS)
DFS method is chosen to solve this task. Starting from box 0, exploring each box and the keys inside it using stack. If all boxes are visited, return True.
