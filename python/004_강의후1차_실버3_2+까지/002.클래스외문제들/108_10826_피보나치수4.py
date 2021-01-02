from sys import stdin
from sys import exit 
n = int(stdin.readline())

n_list = []

if n == 0:
    print(0)
    exit()
elif n == 1:
    print(1)
    exit()

for i in range(n+1):
    if i == 0:
        n_list.append(0)
    elif i == 1:
        n_list.append(1)
    else:
        n_list.append(n_list[i-1]+n_list[i-2])

print(n_list[n])