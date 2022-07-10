
def first_x(str,index=0):
    if len(str) == 0:
        return index
    if str[0] == 'x':
        return index
    return first_x(str[1:],index+1)

print(first_x("abcdefghijklmnopqrstuvwxyz"))
# print(first_x("acx"))
        
