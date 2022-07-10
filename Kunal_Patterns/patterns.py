
def patterns(N):
    for i in range(N):
        if i % 2 == 1:
            print('*' * i)

def pattern(N):
    if N == 0:
        return
    print('*' * N)
    pattern(N-1)

patterns(15)
print()
print()
pattern(5)