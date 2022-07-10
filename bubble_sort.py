# def bubble_sort(arr):
#     sorted = []
#     i = 0
#     while True and i < len(arr)- 1:
#         first = arr[i]
#         second = arr[i+1]
#         if first > second:
#             sorted.append(second)
#             arr[i+1] = first
#             i += 1
#             continue
#         break
#     return sorted


def bubble_sort(arr):
    max_index = len(arr) - 1
    sorted  = False

    while not sorted:
        sorted = True
        for i in range(max_index):
            if arr[i] > arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
                sorted = False
        # max_index -= 1
    return arr
print(bubble_sort([65, 55, 45, 35, 25, 15, 10]))
