t = int(input())

for _ in range(t):
    n = int(input())
    total_c = 0
    total = 0
    for _ in range(n):
        c,g = map(float,input().split())
        total_c += c
        total += g*c
    total /= total_c
    print(int(total_c),round(total,1))