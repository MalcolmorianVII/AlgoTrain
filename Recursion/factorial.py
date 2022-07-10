# def factorial(num):
#     if num == 1:
#         return 1
#     return num * factorial(num-1)

def factorial(n,i=1,product=1):
    return product if i > n else factorial(n,i+1,product*i)
print(factorial(3))