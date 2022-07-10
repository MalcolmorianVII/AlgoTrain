
def find_shortest_paths(rows,cols):
    cells = rows * cols
    shortest_paths = []
    start = 1
    finish = cells
    max_row = rows - 1
    max_col = cols - 1
    max_total = max_row + max_col
    