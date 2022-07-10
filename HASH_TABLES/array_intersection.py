

# def int_two_arrays(arr1,arr2):
#     arr3 = []

#     for _,item in enumerate(arr1):
#         if item in arr2:
#             arr3.append(item)
#     return arr3

def int_two_arrays(arr1,arr2):
    arr1_dict = {key:True for key in arr1} 
    arr3 = [item for item in arr2 if arr1_dict.get(item)]
    return arr3 if arr3 else None
print(int_two_arrays([1, 2, 3, 4, 5],[0, 2, 4, 6, 8]))
print(int_two_arrays([1, 2, 3, 4, 5],[0, 6, 8,7,9]))
