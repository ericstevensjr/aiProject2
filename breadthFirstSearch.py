from utils import *
from grid import Point

def breadthFirstSearch(sourcePoint, destinationPoint, enclosures, turfs, MAX):
    frontier = Queue()
    frontier.push(sourcePoint)
    visited = set()
    parentNodes = {sourcePoint: None}
    pathCost = {sourcePoint: 0}
    nodesExpanded = 0

    while not frontier.isEmpty():
        currentPoint = frontier.pop()
        nodesExpanded += 1

        if currentPoint == destinationPoint:
            break

        for nextPoint in getNeighbors(currentPoint, enclosures, MAX):
           if nextPoint not in visited:
               visited.add(nextPoint)
               parentNodes[nextPoint] = currentPoint
               pathCost[nextPoint] = pathCost[currentPoint] + 1
               frontier.push(nextPoint)
    
    path = reconstructPath(parentNodes, sourcePoint, destinationPoint)
    totalCost = pathCost[destinationPoint] if destinationPoint in pathCost else None
    
    return path, totalCost, nodesExpanded
    

