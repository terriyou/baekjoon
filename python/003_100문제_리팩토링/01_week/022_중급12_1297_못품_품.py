import math
i,y,x = map(int,input().split())

base = math.sqrt(i**2/(y**2+x**2))
print(int(base*y), int(base*x))