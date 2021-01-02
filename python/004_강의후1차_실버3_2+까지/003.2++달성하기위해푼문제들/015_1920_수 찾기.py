import sys
n = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
m_list = list(map(int, sys.stdin.readline().split()))

n_set = set(n_list)

for i in range(m):
    if m_list[i] in n_set:
        print(1)
    else:
        print(0)