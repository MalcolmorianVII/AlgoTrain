# def insertion_sort(arr):
#     start = 1
#     gap = start
#     shift = 0
#     sorted = False

#     while not sorted:
#         sorted = True
#         temp = arr[start]
#         # Begin shifting phase
#         left_val = arr[:start][::-1]
#         for index in range(len(left_val)):
#             if left_val[index] > temp:
#                 sorted = False
#                 shift +=1
#                 shift_index = start+ shift
#                 arr[shift_index] = left_val[index]
#                 gap -= 1
#         arr[gap] = temp
#         start += 1
#     return arr

# print(insertion_sort([2,1,3]))
            
def insertion_sort(arr):
    start = 1
    left = arr[:start]
    gap = start
    for i in range(len(arr)):
        # gap = start
        for j in range(len(left)):
            if start < len(arr) and left[j] > arr[start]:
                # Goes to the right of the start
                # Swap now
                gap = start - 1
                arr[gap],arr[start] = arr[start],left[j]
        start += 1
    return arr

print(insertion_sort([4,2,7,1,3]))



            