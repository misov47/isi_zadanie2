def dfs(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    visited = [[False] * cols for _ in range(rows)]

    def dfs_recursive(row, col, path):
        if not (0 <= row < rows and 0 <= col < cols) or visited[row][col] or maze[row][col] == '#':
            return None

        visited[row][col] = True
        current_position = (row, col)

        if current_position == end:
            original_path = path + [current_position]
            switched_path = [(y, x) for x, y in original_path]
            return switched_path

        neighbors = [
            (row - 1, col), 
            (row + 1, col), 
            (row, col - 1),  
            (row, col + 1), 
        ]

        for neighbor_row, neighbor_col in neighbors:
            result = dfs_recursive(neighbor_row, neighbor_col, path + [current_position])
            if result:
                return result

        return None

    path = dfs_recursive(start[0], start[1], [])

    return path