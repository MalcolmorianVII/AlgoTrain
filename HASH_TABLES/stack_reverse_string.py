
# def stack_reverse_string(str):
#     reversed_str = ''
#     str = list(str)

#     for index in range(len(str)):
#         reversed_str += str.pop()
#     return reversed_str

from collections import deque
def stack_reverse_string(str):
    reversed_str = ''
    stack = deque(str)
    while stack:
        reversed_str += stack.pop()
    return reversed_str
print(stack_reverse_string('abcde'))