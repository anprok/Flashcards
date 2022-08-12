from collections import deque

my_stack = deque()
read_list = []
for _ in range(int(input())):
    command = input().split()
    if command[0] == 'BUY':
        command.remove('BUY')
        my_stack.append(" ".join(command))
    elif command[0] == 'READ':
        read_list.append(my_stack.pop())

print("\n".join(read_list))
