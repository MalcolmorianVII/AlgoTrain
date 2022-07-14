# from collections import deque

# stack = deque()

# stack.append('a')
# stack.append('b')
# stack.append('c')

# print('Initial stack')
# print(stack)

# stack.pop()
# stack.pop()
# stack.pop()

# print('Poped stack')
# print(stack)

from queue import LifoQueue

stack = LifoQueue(maxsize=3)

print(stack.qsize())
stack.put('a')
stack.put('b')
stack.put('c')

print(f"Full:{stack.full()}")
print(f"Size:{stack.qsize()}")

# Pop elements

print(stack.get())
print(stack.get())
print(stack.get())

print("Empty?",stack.empty())

