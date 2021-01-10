a = 3
b = 6
ans = 0
    
n = int(input())
for i in range(n):
    ans += a
    a = a + b
    b += 3

print(ans)