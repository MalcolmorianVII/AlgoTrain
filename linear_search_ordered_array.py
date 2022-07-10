import time
def linear_search_order(arr,search_value):
    count = 0
    for index,element in enumerate(arr):
        if element == search_value:
            return index,count
        elif element > search_value:
            break
        count += 1
    return None,count


def binary_search(arr,search_value):
    if len(arr) == 0:
        return None
    middle_index = int(len(arr)/2)
    # print(f"Middle index:{middle_index}")
    middle_value = arr[middle_index]
    if middle_value == search_value:
        return middle_index
    elif middle_value < search_value:
        left_arr = arr[middle_index+1:]
        binary_search(left_arr,search_value)
    elif middle_value > search_value:
        right_arr = arr[:middle_index]
        binary_search(right_arr,search_value)
    else:
        return None

# def binary_search(arr,search_value):
#     lower_bound = 0
#     upper_bound = len(arr)-1

#     while lower_bound <= upper_bound:
#         middle_index = int((lower_bound + upper_bound )/2)
#         middle_value = arr[middle_index]

#         if search_value == middle_value:
#             return middle_index
#         elif search_value < middle_value:
#             upper_bound = middle_index - 1
#         elif search_value > middle_value:
#             lower_bound = middle_index+ 1
#         else:
#             return None   

start1 = time.time()
linear_search_order([3, 17, 75, 80, 202], 7)
end1 = time.time()

diff1 = round((end1 - start1),5)

print(f"Linear search took {diff1} seconds")


start2 = time.time()
b = binary_search([3, 17, 75, 80, 202], 202 )
print(f"Returned binary search results:{b}")
end2 = time.time()

diff2 = round((end2 - start2),5)

print(f"Binary search took {diff2} seconds")