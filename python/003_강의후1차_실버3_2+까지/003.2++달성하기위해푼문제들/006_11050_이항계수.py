import math 
n, k = map(int, input().split())
rst = math.factorial(n) // (math.factorial(n-k) * math.factorial(k))
print(rst)