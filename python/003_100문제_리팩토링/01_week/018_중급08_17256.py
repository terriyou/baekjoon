a, c = (list(map(int,input().split())) for _ in range(2))
b = []

for i in range(3):
    if i == 2-i:
        b.append(int(c[i] / a[i]))
    else:
        b.append(c[i] - a[2-i])

for i in range(3):
    print(b[i],end=' ')