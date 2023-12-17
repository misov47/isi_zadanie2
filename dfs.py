import time

def dfs(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    visited = [[False] * cols for _ in range(rows)]
    visited_path = []

    start_time = time.time()

    def dfs_recursive(row, col, path):
        if not (0 <= row < rows and 0 <= col < cols) or visited[row][col] or maze[row][col] == '#':
            return None, None

        visited[row][col] = True
        current_position = (row, col)
        if maze[row][col] == ' ':
            visited_path.append(current_position)

        if current_position == end:
            original_path = path + [current_position]
            switched_path = [(y, x) for x, y in original_path]
            end_time = time.time()
            elapsed_time = end_time - start_time
            return switched_path, elapsed_time

        neighbors = [
            (row - 1, col), 
            (row + 1, col), 
            (row, col - 1),  
            (row, col + 1), 
        ]

        for neighbor_row, neighbor_col in neighbors:
            result, elapsed_time = dfs_recursive(neighbor_row, neighbor_col, path + [current_position])
            if result:
                return result, elapsed_time

        return None, None

    path, search_time = dfs_recursive(start[0], start[1], [])

    return path, search_time, visited_path
