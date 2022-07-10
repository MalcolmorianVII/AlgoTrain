
def sum_array(arr):
    return arr[0] if len(arr) == 1 else arr[0] + sum_array(arr[1:len(arr)])

print(sum_array([1,2,3,6,7,8,9]))