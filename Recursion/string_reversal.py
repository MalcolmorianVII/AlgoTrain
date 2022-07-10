
# def reverse_string(str):
#     # e.g. 
#     # subproblem is bcde
#     return str[0] if len(str) == 1 else reverse_string(str[1:]) + str[0]

def reverse_string(str):
    # problem is abcde
    # subproblem is bcde
    return str[0] if len(str) == 1 else str[-1] + reverse_string(str[-2:])


print(reverse_string("abcde"))