
# To be continued!!!!!

def find_unique_path(R,C):
    if R == 1 or C == 1:
        return 1
    return find_unique_path(R - 1,C) + find_unique_path(R,C-1)

        

print(find_unique_path(2,3))
