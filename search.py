import matplotlib.pyplot as plt
import numpy as np
import time
import matplotlib.animation as animation

from utils import *
from grid import *
from breadthFirstSearch import *
from depthFirstSearch import *
from greedyBestFirstSearch import *
from aStar import *

def run_all_algorithms_and_log_results(source, destination, epolygons, tpolygons, MAX):
    algorithms = {
        'Depth-First Search': depthFirstSearch,
        'Breadth-First Search': breadthFirstSearch,
        'Greedy Best First Search': greedyBestFirstSearch,
        'A* Search': aStar
    }
    
    with open("summary.txt", "a") as file:
        for name, algorithm in algorithms.items():
            res_path, totalCost, nodesExpanded = algorithm(source, destination, epolygons, tpolygons, MAX)
            file.write(f"{name}:\n Path Cost: {totalCost}\n Nodes Expanded: {nodesExpanded}\n\n")

def user_select_algorithm():
    algorithms = {
        '1': ('Depth-First Search', depthFirstSearch),
        '2': ('Breadth-First Search', breadthFirstSearch),
        '3': ('Greedy Best First Search', greedyBestFirstSearch),
        '4': ('A* Search', aStar)
    }

    print("Select an algorithm to run:")
    for key, (name, _) in algorithms.items():
        print(f"{key}: {name}")

    choice = input("Enter your choice (1-4): ")
    if choice in algorithms:
        _, algorithm = algorithms[choice]
        return algorithm  # Return the chosen algorithm function
    else:
        print("Invalid choice.")
        return None


def gen_polygons(worldfilepath):
    polygons = []
    with open(worldfilepath, "r") as f:
        lines = f.readlines()
        lines = [line[:-1] for line in lines]
        for line in lines:
            polygon = []
            pts = line.split(';')
            for pt in pts:
                xy = pt.split(',')
                polygon.append(Point(int(xy[0]), int(xy[1])))
            polygons.append(polygon)
    return polygons

if __name__ == "__main__":
    with open("summary.txt", "w"):
        pass
    
    epolygons = gen_polygons('TestingGrid/world2_enclosures.txt')
    tpolygons = gen_polygons('TestingGrid/world2_turfs.txt')

    source = Point(8,10)
    dest = Point(43,45)

    run_all_algorithms_and_log_results(source, dest, epolygons, tpolygons, MAX)
    chosenAlgorithm = user_select_algorithm()
    if chosenAlgorithm:
        res_path, totalCost, nodesExpanded = chosenAlgorithm(source, dest, epolygons, tpolygons, MAX)


    fig, ax = draw_board()
    draw_grids(ax)
    draw_source(ax, source.x, source.y)  # source point
    draw_dest(ax, dest.x, dest.y)  # destination point
    
    # Draw enclosure polygons
    for polygon in epolygons:
        for p in polygon:
            draw_point(ax, p.x, p.y)
    for polygon in epolygons:
        for i in range(0, len(polygon)):
            draw_line(ax, [polygon[i].x, polygon[(i+1)%len(polygon)].x], [polygon[i].y, polygon[(i+1)%len(polygon)].y])
    
    # Draw turf polygons
    for polygon in tpolygons:
        for p in polygon:
            draw_green_point(ax, p.x, p.y)
    for polygon in tpolygons:
        for i in range(0, len(polygon)):
            draw_green_line(ax, [polygon[i].x, polygon[(i+1)%len(polygon)].x], [polygon[i].y, polygon[(i+1)%len(polygon)].y])

    for i in range(len(res_path)-1):
        draw_result_line(ax, [res_path[i].x, res_path[i+1].x], [res_path[i].y, res_path[i+1].y])
        plt.pause(0.1)
    
    plt.show()
