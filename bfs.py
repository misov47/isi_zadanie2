from collections import deque
import time

def bfs(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    visited = [[False] * cols for _ in range(rows)]
    queue = deque([(start[0], start[1], [])])

    start_time = time.time()
    visited_path = []

    while queue:
        current_row, current_col, path = queue.popleft()
        visited[current_row][current_col] = True
        if maze[current_row][current_col] == ' ':
            visited_path.append((current_row, current_col))

        if (current_row, current_col) == end:
            original_path = path + [(current_row, current_col)]
            switched_path = [(y, x) for x, y in original_path]
            end_time = time.time()
            elapsed_time = end_time - start_time
            return switched_path, elapsed_time, visited_path

        neighbors = [
            (current_row - 1, current_col), 
            (current_row + 1, current_col), 
            (current_row, current_col - 1), 
            (current_row, current_col + 1),
        ]

        for neighbor_row, neighbor_col in neighbors:
            if 0 <= neighbor_row < rows and 0 <= neighbor_col < cols and not visited[neighbor_row][neighbor_col] and maze[neighbor_row][neighbor_col] != '#':
                queue.append((neighbor_row, neighbor_col, path + [(current_row, current_col)]))
                visited[neighbor_row][neighbor_col] = True
    end_time = time.time()
    elapsed_time = end_time - start_time
    return None, elapsed_time, visited_path