from collections import deque

n = int(input())

n_list = deque(range(1,n+1))

while len(n_list) > 1:
    n_list.remove(n_list[0])
    n_list.append(n_list.popleft())

print(n_list[0])