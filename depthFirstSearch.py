from utils import *
from grid import Point

# Depth-First Search Algorithm
def depthFirstSearch(sourcePoint, destinationPoint, enclosures, turfs, MAX):
    # Had to create my own stack instead of using the function already made.
    #     for some reason, the provided stack was not working for me.
    stack = [(sourcePoint, [sourcePoint])] 
    visited = set([sourcePoint])
    nodesExpanded = 0

    while stack:
        currentNode, path = stack.pop()
        nodesExpanded += 1

        if currentNode == destinationPoint:
            return path, len(path) - 1, nodesExpanded

        neighbors = getNeighbors(currentNode, enclosures, MAX)
        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append((neighbor, path + [neighbor]))

    return [], 0, nodesExpanded