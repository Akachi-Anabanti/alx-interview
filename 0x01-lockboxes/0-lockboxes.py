#!/usr/bin/python3
'''A python script that uses the depth first search
algorithm to check if all the nodes of a graph can be
visited'''


def canUnlockAll(boxes):
    """A function that checks if all the boxes of a graph
    can be visited
    The keys in a box; i.e the value in the node represents the
    index[position] of another node
    """
    n = len(boxes)
    visited = set()
    stack = [0]

    while stack:
        current_box = stack.pop()
        if current_box not in visited:
            visited.add(current_box)
            for key in boxes[current_box]:
                if key < n not in visited:
                    stack.append(key)
    return len(visited) == n
