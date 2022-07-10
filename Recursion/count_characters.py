
def count_characters(arr):
    #  return count[0] + count_characters(arr[1:])
    if len(arr) == 1:
        return len(arr[0])
    return len(arr[0]) + count_characters(arr[1:])

print(count_characters(["abcdedafc"]))