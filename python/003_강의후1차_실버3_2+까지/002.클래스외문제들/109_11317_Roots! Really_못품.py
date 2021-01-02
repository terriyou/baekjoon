from sys import stdin
from math import sqrt
from sys import exit
n = int(stdin.readline())
for i in range(n):
    a,b,c,s,t = map(float,stdin.readline().split())
    in_root = (b**2)-4*a*c
    if in_root < 0:
        print("No")
        exit()
    plus = (-1*b+sqrt(in_root)) / (2*a)
    minus = (-1*b-sqrt(in_root)) / (2*a)

    if minus >=s and plus <=t:
        print("Yes")
    else:
        print("No")
    
