
# def add_less_100(arr):
#     sum = 0
#     for num in arr:
#         if sum + num > 100:
#             continue
#         sum += num
#     return sum

def add_less_100(arr):
    if len(arr) == 0:
        return 0
    rest_sum = add_less_100(arr[1:])
    if arr[0] + rest_sum > 100:
        return rest_sum
    else:
        return arr[0] + rest_sum
print(add_less_100([1,3,20,4,5,9]))