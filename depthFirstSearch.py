from utils import *
from grid import Point

def depthFirstSearch(sourcePoint, destinationPoint, enclosures, turfs, MAX):
    stack = [(sourcePoint, [sourcePoint])]  # Stack holds tuples of (current node, path to current node)
    visited = set([sourcePoint])
    nodes_expanded = 0

    while stack:
        current_node, path = stack.pop()
        nodes_expanded += 1

        # If the current node is the destination, return the path and its cost
        if current_node == destinationPoint:
            path_cost = len(path) - 1  # Path cost is 1 per move
            return path, path_cost, nodes_expanded

        for neighbor in getNeighbors(current_node, enclosures, MAX):
            if neighbor not in visited:
                visited.add(neighbor)
                # For each unvisited neighbor, push it onto the stack along with the path taken to reach it
                stack.append((neighbor, path + [neighbor]))

    # If the loop exits without finding the destination, the destination is not reachable
    return [], 0, nodes_expanded