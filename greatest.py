def greatest_num(arr):
    greatest = arr[0]

    for num in arr:
        if num > greatest:
            greatest = num
    return greatest

print(greatest_num([65, 55, 45, 35000, 25, 15, 100]))