maze = [
    [1, 0, 0, 0, 1, 1],
    [1, 0, 1, 0, 1, 0],
    [1, 1, 1, 0, 1, 0],
    [0, 1, 0, 0, 1, 1],
    [0, 1, 1, 1, 0, 1],
    [1, 1, 0, 1, 1, 1],
]

length = 6
solved_maze = [[0 for i in range(length)] for j in range(length)]

def is_safe(row, column):
    # check if its not out of bounds nor a wall
    return row >= 0 and row < length and column >= 0 and column < length and maze[row][column] == 1

def keep_going(row, column):
    if row == (length - 1) and column == (length - 1):
        solved_maze[row][column] = 1
        return True
    if is_safe(row, column):
        solved_maze[row][column] = 1
        # try to keep going on row
        if keep_going(row + 1, column):
            return True
        # try to keep going on column
        if keep_going(row, column + 1):
            return True

        solved_maze[row][column] = 0
        return False
    return False

if __name__ == '__main__':
    # populate solved_maze matrix with solution path
    keep_going(0, 0)
    for position in solved_maze:
        print(position)