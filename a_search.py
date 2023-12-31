from heapq import heappush, heappop
import time

def heuristic(position, goal):
    return abs(position[0] - goal[0]) + abs(position[1] - goal[1])

def a_star_search(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    visited = [[False] * cols for _ in range(rows)]
    priority_queue = [(0 + heuristic(start, end), 0, start, [])]

    visited_path = []
    start_time = time.time()

    while priority_queue:
        _, cost, current_position, path = heappop(priority_queue)
        visited_path.append(current_position)

        if current_position == end:
            original_path = path + [current_position]
            switched_path = [(y, x) for x, y in original_path]
            end_time = time.time()
            elapsed_time = end_time - start_time
            return switched_path, elapsed_time, visited_path

        if not visited[current_position[0]][current_position[1]]:
            visited[current_position[0]][current_position[1]] = True

            neighbors = [
                (current_position[0] - 1, current_position[1]),  
                (current_position[0] + 1, current_position[1]),  
                (current_position[0], current_position[1] - 1),  
                (current_position[0], current_position[1] + 1),  
            ]

            neighbors = [(cost + 1 + heuristic(neighbor, end), cost + 1, neighbor, path + [current_position]) for neighbor in neighbors if
                         0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and maze[neighbor[0]][neighbor[1]] != '#']

            for neighbor_priority, neighbor_cost, neighbor, neighbor_path in neighbors:
                heappush(priority_queue, (neighbor_priority, neighbor_cost, neighbor, neighbor_path))
    end_time = time.time()
    elapsed_time = end_time - start_time
    return None, elapsed_time, visited_path