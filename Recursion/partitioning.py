from random import choice

def part(arr):
    pivot = choice(arr)
    if len(arr) == 1:
        return [arr[0]]
    if arr[1] < pivot:
        arr[0],arr[1] = arr[1],pivot
    else:
        arr[1],arr[0] = pivot,arr[1]
    
    return [arr[0]] + part(arr[1:])

print(part([1,3,4,5,9,2]))