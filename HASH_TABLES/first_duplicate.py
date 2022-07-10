# def find_first_duplicate(arr):
    
#     for _,item in enumerate(arr):
#         if arr.count(item) > 1:
#             return item
def find_first_duplicate(arr):
    item_count = {}
    for _,item in enumerate(arr):
        if item_count.get(item):
            return item
        item_count[item] = True

print(find_first_duplicate(["a", "b", "c", "d", "c", "e", "f"]))