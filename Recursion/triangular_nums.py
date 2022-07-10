
def triangular_nums(N):
    if N == 1:
        return 1
    return N + triangular_nums(N-1)

print(triangular_nums(10))