from collections import deque

def bfs(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    visited = [[False] * cols for _ in range(rows)]
    queue = deque([(start[0], start[1], [])])

    while queue:
        current_row, current_col, path = queue.popleft()
        visited[current_row][current_col] = True

        if (current_row, current_col) == end:
            original_path = path + [(current_row, current_col)]
            switched_path = [(y, x) for x, y in original_path]
            return switched_path

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
    return None