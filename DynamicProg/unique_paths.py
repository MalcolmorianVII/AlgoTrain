def unique_paths(rows, columns):
    if rows == 1 or columns == 1 :
        return 1
    return unique_paths(rows - 1, columns) + unique_paths(rows, columns - 1)


def unique_paths1(rows, columns,mem):
    if rows == 1 or columns == 1 :
        return 1
    row_cols = f"{rows}{columns}"

    if not mem.get(row_cols):
        mem[row_cols] = unique_paths1(rows - 1, columns,mem) + unique_paths1(rows, columns - 1,mem)
    
    return mem.get(row_cols)

# print(unique_paths(2,2))
print(unique_paths(2,7))
print(unique_paths1(2,7,{}))
# print(unique_paths(2,2,{}))