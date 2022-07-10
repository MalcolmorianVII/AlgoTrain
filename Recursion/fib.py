
# def fib(n,memo):
#     if n == 0 or n == 1:
#         return n
#     if not memo.get(n):
#         result = fib(n-2,memo) + fib(n-1,memo)
#         memo[n] = result
#     return memo.get(n)


def fib(n):
    if n == 0 :
        return 0
    a = 0
    b = 1

    for i in range(1,n):
        temp = a
        a = b
        b = temp + a
    return b
print(fib(10))