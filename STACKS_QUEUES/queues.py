# Using lists

# queue = [] #Initializing a queue

# # Enquieng

# queue.append(1)
# queue.append(2)
# queue.append(3)

# print(queue)

# print(queue.pop(0))
# print(queue.pop(0))
# print(queue.pop(0))

#Using collections.deque

# from collections import deque

# queue = deque()

# queue.append(1)
# queue.append(2)
# queue.append(3)

# print("Initial queue")
# print(queue)

# print(queue.pop())

# Using built-in queue module

from queue import Queue

q = Queue(maxsize=5)

q.put(1)
q.put(2)
q.put(3)
q.put(4)
q.put(5)

print("Getting queue items")
print(q.get())
print(q)
