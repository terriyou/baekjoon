from sys import stdin
from collections import Counter
n = int(stdin.readline())
n_list = []

for _ in range(n):
    n_list.append(int(stdin.readline()))

print(round(sum(n_list)/n))

n_list.sort()
print(n_list[n//2])

c = Counter(n_list).most_common()

if len(n_list) > 1:
    if c[0][1] == c[1][1]:
        print(c[1][0])
    else:
        print(c[0][0])
else:
    print(n_list[0])

print(n_list[-1] - n_list[0])