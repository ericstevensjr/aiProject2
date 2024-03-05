from utils import *
from grid import Point

def breadthFirstSearch(sourcePoint, destinationPoint, enclosures, turfs, MAX):
    frontier = Queue()
    frontier.push(sourcePoint)
    parentNodes = {sourcePoint: None}
    pathCost = {sourcePoint: 0}
    nodesExpanded = 0

    while not frontier.isEmpty():
        currentPoint = frontier.pop()
        nodesExpanded += 1

        if currentPoint == destinationPoint:
            break

        for next in getNeighbors(currentPoint, enclosures, MAX):
            newCost = pathCost[currentPoint] + 1
            if next not in pathCost or newCost < pathCost[next]:
                pathCost[next] = newCost
                priority = newCost
                frontier.push(next)
                parentNodes[next] = currentPoint

    path = reconstructPath(parentNodes, sourcePoint, destinationPoint)
    totalCost = pathCost[destinationPoint] if destinationPoint in pathCost else None
    
    return path, totalCost, nodesExpanded
    

