from collections import deque

my_stack = deque()
for _ in range(int(input())):
    my_stack.append(input())

for _ in range(len(my_stack)):
    print(my_stack.pop())
