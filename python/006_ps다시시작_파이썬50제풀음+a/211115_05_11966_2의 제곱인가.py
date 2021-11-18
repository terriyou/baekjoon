import math

flag = 0

inpt = int(input())
for i in range(31):
    if math.pow(2, i) == inpt:
        flag = 1

print(flag)
