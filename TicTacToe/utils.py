def check(grid, line, column, player):
    if grid[line][column] == 0:
        grid[line][column] = player
        return True
    return False

def check_game(grid):
    res_line = check_lines(grid)
    res_column = check_columns(grid)
    res_diag = check_diag(grid)
    if res_line or res_column or res_diag:
        return True
    return False

def check_lines(grid):
    for line in grid:
        size = len(set(line))
        if size == 1 and set(line) != {0}: # an unique element in lines
            return True
    return False

def check_columns(grid):
    columns = list(zip(*grid))
    for c in columns:
        size = len(set(c))
        if size == 1 and set(c) != {0}:
            return True
    return False

def check_diag(grid):
    length = len(grid)
    d1 = [grid[i][i] for i in range(length)]
    d2 = [grid[length-1-i][i] for i in range(length-1, -1, -1)]
    s1 = len(set(d1))
    s2 = len(set(d2))
    if (s1 == 1 and set(d1) != {0}) or (s2 == 1 and set(d2) != {0}):
        return True
    return False
