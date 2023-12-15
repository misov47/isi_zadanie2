import time

def heuristic(position, goal):
    return abs(position[0] - goal[0]) + abs(position[1] - goal[1])

def greedy_search(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    visited = [[False] * cols for _ in range(rows)]
    priority_queue = [(heuristic(start, end), start, [])]

    start_time = time.time()

    while priority_queue:
        _, current_position, path = priority_queue.pop(0)

        if current_position == end:
            original_path = path + [current_position]
            switched_path = [(y, x) for x, y in original_path]
            end_time = time.time()
            elapsed_time = end_time - start_time
            return switched_path, elapsed_time

        if not visited[current_position[0]][current_position[1]]:
            visited[current_position[0]][current_position[1]] = True

            neighbors = [
                (current_position[0] - 1, current_position[1]),  
                (current_position[0] + 1, current_position[1]),  
                (current_position[0], current_position[1] - 1),  
                (current_position[0], current_position[1] + 1), 
            ]

            neighbors = [(heuristic(neighbor, end), neighbor) for neighbor in neighbors if
                         0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and maze[neighbor[0]][neighbor[1]] != '#']

            neighbors.sort()  

            for _, neighbor in neighbors:
                priority_queue.insert(0, (heuristic(neighbor, end), neighbor, path + [current_position]))

    return None, None  