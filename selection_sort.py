# Example: [2,6,1,3]

def selection_sort(arr):
    start_index = 0
    lowest_index = 0
    sorted = False
    last_index = len(arr)-1

    while not sorted:
        sorted = True
        if start_index == last_index:
            return arr
        for index in range(start_index,last_index+1):
                if arr[index] < arr[lowest_index]:
                    sorted = False
                    lowest_index = index
                    
                    # print(f"Lowest_index{lowest_index}:Value{arr[index]}")
                print(index)
        arr[start_index],arr[lowest_index] = arr[lowest_index],arr[start_index] # Swap
        start_index += 1
    return arr

print(selection_sort([2,6,1,3]))
# print(selection_sort([4,2,7,1,3]))