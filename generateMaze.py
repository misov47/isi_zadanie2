import random

maze = [['#' for _ in range(30)] for _ in range(30)]

# Mark the starting and ending points
maze[1][0] = ' '
maze[28][29] = ' '

# Recursive Backtracking algorithm to generate a random maze
def generate_maze(x, y):
    directions = [(0, 2), (0, -2), (2, 0), (-2, 0)]
    random.shuffle(directions)

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 < nx < 29 and 0 < ny < 29 and maze[nx][ny] == '#':
            maze[x + dx // 2][y + dy // 2] = ' '
            maze[nx][ny] = ' '
            generate_maze(nx, ny)

# Start the maze generation from the entrance
generate_maze(1, 0)

# Print the generated maze
for row in maze:
    print(row)