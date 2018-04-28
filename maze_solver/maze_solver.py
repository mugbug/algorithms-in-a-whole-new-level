maze = [
    [1, 0, 0, 0, 1, -1],
    [1, 0, 1, 0, 1, 0],
    [1, 1, 1, 0, 1, 0],
    [0, 1, 0, 0, 1, 1],
    [0, 1, 1, 1, 0, 1],
    [1, 1, 0, 1, 1, 1],
]

solved_maze = [[0]*6]*6

def is_safe(row, column):
    size = len(maze)
    if row < size and column < size:
        return True
    return False

def keep_going(row, column):
    if is_safe(row, column):
        if maze[row][column] == -1:
            print(solved_maze)
            return True
        if maze[row][column] == 1:
            return True
        if maze[row][column == 0]:
            return False
        
        
        
