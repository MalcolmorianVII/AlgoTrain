def golomb(n):
    if n == 1:
        return 1
    return 1 + golomb( n - golomb(golomb(n-1)))

def golomb1(n,mem = {}):
    if n == 1:
        return 1
    
    if not mem.get(n):
        mem[n] =  1 + golomb1( n - golomb1(golomb1(n-1,mem),mem),mem)
    return mem[n]

print(golomb(2))
print(golomb1(2,{}))