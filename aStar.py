import math

from utils import *
from grid import Point

def aStar(sourcePoint, destinationPoint, enclosures, turfs, MAX):
    frontier = PriorityQueue()
    frontier.push(sourcePoint, 0)
    parentNodes = {sourcePoint: None}
    pathCost = {sourcePoint: 0}
    nodesExpanded = 0

    while not frontier.isEmpty():
        currentPoint = frontier.pop()
        nodesExpanded += 1

        if currentPoint == destinationPoint:
            break

        for nextPoint in getNeighbors(currentPoint, enclosures, MAX):
            newCost = pathCost[currentPoint] + actionCost(currentPoint, nextPoint, turfs)
            if nextPoint not in pathCost or newCost < pathCost[nextPoint]:
                pathCost[nextPoint] = newCost
                priority = newCost + heuristic(nextPoint, destinationPoint)
                frontier.push(nextPoint, priority)
                parentNodes[nextPoint] = currentPoint

    path = reconstructPath(parentNodes, sourcePoint, destinationPoint)
    pathCost = pathCost[destinationPoint] if destinationPoint in pathCost else None

    return path, pathCost, nodesExpanded