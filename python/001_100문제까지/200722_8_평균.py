a = int(input())
b = input().split(' ')
print(b)
print(type(b))
b = list(map(int, b))

max = max(b)

for i in range(a):
    b[i] = 100 * int(b[i]) / max

print(sum(b)/a)    