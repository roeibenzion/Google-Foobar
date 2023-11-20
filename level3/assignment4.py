'''
Challenge 3.1
Prepare the Bunnies' Escape
===========================

You're awfully close to destroying the LAMBCHOP doomsday device and freeing Commander Lambda's bunny prisoners, but once they're free of the prison blocks, the bunnies are going to need to escape Lambda's space station via the escape pods as quickly as possible. Unfortunately, the halls of the space station are a maze of corridors and dead ends that will be a deathtrap for the escaping bunnies. Fortunately, Commander Lambda has put you in charge of a remodeling project that will give you the opportunity to make things a little easier for the bunnies. Unfortunately (again), you can't just remove all obstacles between the bunnies and the escape pods - at most you can remove one wall per escape pod path, both to maintain structural integrity of the station and to avoid arousing Commander Lambda's suspicions. 

You have maps of parts of the space station, each starting at a prison exit and ending at the door to an escape pod. The map is represented as a matrix of 0s and 1s, where 0s are passable space and 1s are impassable walls. The door out of the prison is at the top left (0,0) and the door into an escape pod is at the bottom right (w-1,h-1). 

Write a function answer(map) that generates the length of the shortest path from the prison door to the escape pod, where you are allowed to remove one wall as part of your remodeling plans. The path length is the total number of nodes you pass through, counting both the entrance and exit nodes. The starting and ending positions are always passable (0). The map will always be solvable, though you may or may not need to remove a wall. The height and width of the map can be from 2 to 20. Moves can only be made in cardinal directions; no diagonal moves are allowed.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int) maze = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
Output:
    (int) 7

Inputs:
    (int) maze = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
Output:
    (int) 11
    
'''

import copy
from collections import deque
def bfs(grid, i, j):
    s = []
    dist = [[float('inf') for _ in range(len(grid[0]))] for _ in range(len(grid))]
    s.append((i, j, 1))
    d = 1

    grid[i][j] = -1
    while len(s) != 0:
        (i, j, d) = s.pop(0)
        dist[i][j] = d

        if grid[i][j] == 1:
            grid[i][j] = -1
            continue

        grid[i][j] = -1
        if i > 0 and grid[i - 1][j] != -1:
            s.append((i - 1, j, d + 1))

        if i < len(grid) - 1 and grid[i + 1][j] != -1:
            s.append((i + 1, j, d + 1))

        if j > 0 and grid[i][j - 1] != -1:
            s.append((i, j - 1, d + 1))

        if j < len(grid[0]) - 1 and grid[i][j + 1] != -1:
            s.append((i, j + 1, d + 1))

    return dist

def bfs_distance_matrix(matrix, start_i, start_j):
    if not matrix:
        return []

    rows, cols = len(matrix), len(matrix[0])
    distance_matrix = [[float('inf') for _ in range(cols)] for _ in range(rows)]
    queue = deque([(start_i, start_j, 1)])  # (i, j, distance)
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # 4 possible movements (up, down, left, right)

    while queue:
        i, j, distance = queue.popleft()

        # Update the distance for the current cell
        distance_matrix[i][j] = distance

        # Explore the neighbors
        for dx, dy in directions:
            ni, nj = i + dx, j + dy
            if 0 <= ni < rows and 0 <= nj < cols and matrix[ni][nj] == 0 and distance_matrix[ni][nj] == float('inf'):
                # If the neighbor is within bounds, is passable, and not visited yet
                # Mark it as visited and enqueue it
                queue.append((ni, nj, distance + 1))
            elif 0 <= ni < rows and 0 <= nj < cols and matrix[ni][nj] == 1 and distance_matrix[ni][nj] == float('inf'):
                distance_matrix[ni][nj] = distance+1

    return distance_matrix

def solution(map):
    #call by value
    orig1 = copy.deepcopy(map)
    orig2 = copy.deepcopy(orig1)
    d1 = bfs_distance_matrix(orig1, 0, 0)
    d2 = bfs_distance_matrix(orig2, len(map)-1, len(map[0])-1)

    d = d1[len(map)-1][len(map[0])-1]
    for i in range(len(map)):
        for j in range(len(map[0])):
            #check if reachable by 0's from both sources
            if map[i][j] == 1 and d1[i][j] > 0 and d2[i][j] > 0:
                d = min(d, d1[i][j]+d2[i][j] - 1)
    return d
    
