import heapq
from grid import Point

class Stack:
    "A container with a last-in-first-out (LIFO) policy"
    def __init__(self):
        self.list = []

    def push(self,item):
        "Push 'item' onto the stack"
        self.list.insert(0, item)

    def pop(self):
        "Pop the most recently pushed item from the stack"
        return self.list.pop()

    def isEmpty(self):
        "Returns true if the stack is empty"
        return len(self.list) == 0

class Queue:
    "A container with a first-in-first-out (FIFO) policy"
    def __init__(self):
        self.list = []

    def push(self,item):
        "Enqueue the 'item' into the queue"
        self.list.insert(0,item)

    def pop(self):
        """
          Dequeue the earliest enqueued item still in the queue. This
          operation removes the item from the queue.
        """
        return self.list.pop()

    def isEmpty(self):
        "Returns true if the queue is empty"
        return len(self.list) == 0

class PriorityQueue:
    """
      Implements a priority queue data structure. Each inserted item
      has a priority associated with it and the client is usually interested
      in quick retrieval of the lowest-priority item in the queue. This
      data structure allows O(1) access to the lowest-priority item.
    """
    def  __init__(self):
        self.heap = []
        self.count = 0

    def push(self, item, priority):
        entry = (priority, self.count, item)
        heapq.heappush(self.heap, entry)
        self.count += 1

    def pop(self):
        (_, _, item) = heapq.heappop(self.heap)
        return item

    def isEmpty(self):
        return len(self.heap) == 0

    def update(self, item, priority):
        # If item already in priority queue with higher priority, update its priority and rebuild the heap
        # If item already in priority queue with equal or lower priority, do nothing
        # If item not in priority queue, do the same thing as self.push
        flag = False
        for index, (p, c, i) in enumerate(self.heap):
            if i == item:
                flag = True
                if p <= priority:
                    break
                del self.heap[index]
                self.heap.append((priority, c, item))
                heapq.heapify(self.heap)
                break
        if flag == False:
            self.push(item, priority)

def isPointInsidePolygon(point, polygon):
    x, y = point.x, point.y
    inside = False

    # Check if point is on any of the edges
    for i in range(len(polygon)):
        p1 = polygon[i]
        p2 = polygon[(i + 1) % len(polygon)]
        if (p1.y == y and p2.y == y) and (min(p1.x, p2.x) <= x <= max(p1.x, p2.x)):
            # Point is on a horizontal edge
            return True
        if (p1.x == x and p2.x == x) and (min(p1.y, p2.y) <= y <= max(p1.y, p2.y)):
            # Point is on a vertical edge
            return True
        
    # Ray casting algorithm to check if point is inside the polgyon
    n = len(polygon)
    for i in range(n):
        j = (i + 1) % n
        if ((polygon[i].y > y) != (polygon[j].y > y)) and \
            (x < (polygon[j].x - polygon[i].x) * (y - polygon[i].y) / (polygon[j].y - polygon[i].y) + polygon[i].x):
            inside = not inside

    return inside

def isPointInEnclosure(point, enclosures):  
    for enclosure in enclosures:
        if isPointInsidePolygon(point, enclosure):
            return True
    return False

def isPointInTurf(point, turfs):
    for turf in turfs:
        if isPointInsidePolygon(point, turf):
            return True
    return False

def getNeighbors(point, enclosures, MAX):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    neighbors = []

    for dx, dy in directions:
        nx, ny = point.x + dx, point.y + dy

        # Create neighbor point
        neighbor = Point(nx, ny)

        # Check if the neighbor is within the grid bounds
        if 0 <= nx < MAX and 0 <= ny < MAX:
            # Make sure neighbor isn't in enclosure
            if not isPointInEnclosure(point, enclosures):
                neighbors.append(neighbor)

    return neighbors


def reconstructPath(parentNodes, source, destination):
    path = []
    currentPoint = destination
    while currentPoint != source:
        path.append(currentPoint)
        currentPoint = parentNodes[currentPoint]
    path.append(source)
    path.reverse()

    return path
