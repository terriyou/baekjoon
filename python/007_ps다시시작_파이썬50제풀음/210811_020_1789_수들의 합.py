
from math import sqrt

s = int(input())
x = int(sqrt(2*s))

print(x)

if x*(x+1) <= 2*s:
    print(x)
else:
    print(x-1)

