from utils import *
from grid import Point

def greedyBestFirstSearch(sourcePoint, destinationPoint, enclosures, turfs, MAX):
    frontier = PriorityQueue()
    frontier.push(sourcePoint, 0)
    parentNodes = {sourcePoint: None}
    nodesExpanded = 0

    while not frontier.isEmpty():
        currentPoint = frontier.pop()
        nodesExpanded += 1

        if currentPoint == destinationPoint:
            break

        for nextPoint in getNeighbors(currentPoint, enclosures, MAX):
            if nextPoint not in parentNodes:
                priority = heuristic(nextPoint, destinationPoint)
                frontier.push(nextPoint, priority)
                parentNodes[nextPoint] = currentPoint

    path = reconstructPath(parentNodes, sourcePoint, destinationPoint)
    pathCost = calculatePathCost(path, turfs)

    return path, pathCost, nodesExpanded
