from utils import *
from grid import Point

def depthFirstSearch(sourcePoint, destinationPoint, enclosures, turfs, MAX):
    frontier = Stack()
    frontier.push(sourcePoint)
    visited = set()
    parentNodes = {}

    while not frontier.isEmpty():
        currentPoint = frontier.pop()

        # If goal is reached, reconstruct the path and return
        if currentPoint == destinationPoint:
            path = reconstructPath(parentNodes, sourcePoint, destinationPoint)
            pathCost = len(path) - 1
            return path, pathCost, len(visited)
        
        if currentPoint not in visited:
            visited.add(currentPoint)

            for next in getNeighbors(currentPoint, enclosures, MAX):
                if next not in visited:
                    parentNodes[next] = currentPoint
                    frontier.push(next)

    # If function exits the while loop without returning, the destination is unreachable.
    return [], 0, len(visited)