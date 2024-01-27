from collections import deque

test=deque(["test1","test2","test3"])

test.append("test4")
print(test)
print(test.popleft())
print(test)
print(test.pop())