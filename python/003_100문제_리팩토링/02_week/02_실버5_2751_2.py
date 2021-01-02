import sys

lst = []
n = int(sys.stdin.readline())

for _ in range(n):
    lst.append(int(sys.stdin.readline()))

for i in sorted(lst):
    sys.stdout.write(str(i)+'\n')
