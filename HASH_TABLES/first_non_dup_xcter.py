# def first_non_dup(str):
#     xcter_count = {}
#     non_dup = [item for _,item in enumerate(str) if str.count(item) == 1]
#     return non_dup[0]
def first_non_dup(str):
    xcter_count = {}
    count = 0

    for _,item in enumerate(str):
        if xcter_count.get(item):
            # count += 1
            xcter_count[item] += 1
            continue
        xcter_count[item] = 1
    for key in xcter_count:
        if xcter_count.get(key) == 1:
            return key
    

print(first_non_dup("minimum"))