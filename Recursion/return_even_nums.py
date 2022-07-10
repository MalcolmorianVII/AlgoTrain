
def even_nums(arr,evens=[]):
    # evens = []
    # determine the evenity or oddity of arr[0] + deal with subproblem
    if len(arr) == 0:
        return evens
    if arr[0] % 2 == 0:
        evens.append(arr[0])
    return even_nums(arr[1:],evens)


print(even_nums([1,2,3,4,5,6,7,8,9]))
