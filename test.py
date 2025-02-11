#Algoritma A* pada game Mobile legend
import numpy as np
import heapq

def a_star_algorithm(grid, start, goal):
    """
    Implementasi algoritma A* untuk pathfinding dalam game Mobile Legends.
    """
    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
    
    open_list = []
    heapq.heappush(open_list, (0, start))
    came_from = {}
    cost_so_far = {start: 0}
    
    while open_list:
        _, current = heapq.heappop(open_list)
        
        if current == goal:
            break
        
        for neighbor in get_neighbors(grid, current):
            new_cost = cost_so_far[current] + 1  # Asumsikan bobot grid seragam
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic(goal, neighbor)
                heapq.heappush(open_list, (priority, neighbor))
                came_from[neighbor] = current
    
    return reconstruct_path(came_from, start, goal)

def get_neighbors(grid, node):
    """
    Mengembalikan daftar tetangga dari suatu node dalam grid.
    """
    x, y = node
    neighbors = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
    return [n for n in neighbors if 0 <= n[0] < len(grid) and 0 <= n[1] < len(grid[0])]

def reconstruct_path(came_from, start, goal):
    """
    Merekonstruksi jalur dari start ke goal.
    """
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from.get(current, start)
    path.append(start)
    path.reverse()
    return path

def main():
    grid = np.zeros((5, 5))  # Grid 5x5 kosong
    start = (0, 0)
    goal = (4, 4)
    path = a_star_algorithm(grid, start, goal)
    print("Path ditemukan:", path)

if __name__ == "__main__":
    main()
