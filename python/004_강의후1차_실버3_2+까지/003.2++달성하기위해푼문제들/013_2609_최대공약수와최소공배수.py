from math import gcd

x, y = map(int, input().split())

def lcm(x,y):
    return x * y // gcd(x, y)

print(gcd(x,y))
print(lcm(x,y))