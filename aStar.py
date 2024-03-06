import math
from utils import *
from grid import Point

# A* Search Algorithm 
def aStar(sourcePoint, destinationPoint, enclosures, turfs, MAX):
    # Initialize frontier with source point and a priority of 0
    frontier = PriorityQueue()
    frontier.push(sourcePoint, 0)
    # Dictionary to keep track of parent point for each visited point
    parentNodes = {sourcePoint: None}
    # Dictionary to keep track of cost of the cheapest path found so far
    pathCost = {sourcePoint: 0}
    nodesExpanded = 0

    # Loop until no more points are in the frontier
    while not frontier.isEmpty():
        # Pop the node will the lowest prority
        currentPoint = frontier.pop()
        nodesExpanded += 1

        if currentPoint == destinationPoint:
            break

        # Exploring neighbors of current point
        for nextPoint in getNeighbors(currentPoint, enclosures, MAX):
            # Calculating cost to reach next point
            newCost = pathCost[currentPoint] + actionCost(currentPoint, nextPoint, turfs)
            # Updating frontier and visited nodes
            if nextPoint not in pathCost or newCost < pathCost[nextPoint]:
                pathCost[nextPoint] = newCost
                priority = newCost + heuristic(nextPoint, destinationPoint)
                frontier.push(nextPoint, priority)
                parentNodes[nextPoint] = currentPoint

    path = reconstructPath(parentNodes, sourcePoint, destinationPoint)
    pathCost = pathCost[destinationPoint] if destinationPoint in pathCost else None

    return path, pathCost, nodesExpanded