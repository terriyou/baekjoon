import sys
n = int(input())

for i in range(1, n+1):
    sum = 0
    sum = sum + i
    i = str(i)
    for j in i:
        sum = sum + int(j)
        if sum == n:
            print(i)
            sys.exit(0)
        elif int(i) == n:
            print(0)
        else:
            continue