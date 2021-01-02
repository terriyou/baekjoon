from sys import stdin

n = int(stdin.readline())

n_list = []

for i in range(n):
    tmp = int(stdin.readline())
    if tmp == 0:
        del n_list[-1]
    else:
        n_list.append(tmp)

print(sum(n_list))