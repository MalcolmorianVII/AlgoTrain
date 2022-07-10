
def find_num_paths(n):
    if n < 0: 
        return 0 
    elif n==1 or n == 0:
        return 1
    else:
        return find_num_paths(n-1) + find_num_paths(n-2) + find_num_paths(n-3)

print(find_num_paths(11))