
# def max(arr):
#     if len(arr) == 1:
#         return arr[0]
#     if arr[0] > max(arr[1:]):
#         return arr[0]
#     else:
#         return max(arr[1:])

def max(arr):
    print('RECURSION')
    if len(arr) == 1:
        return arr[0]
    max_remainder = max(arr[1:])
    if arr[0] > max_remainder:
       return arr[0]
    else:
        return max_remainder

print(max([5,4,7,2,9,0]))