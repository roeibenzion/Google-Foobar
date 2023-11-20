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
    
