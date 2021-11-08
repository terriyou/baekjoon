a = list(map(int, input().split()))
b = list(map(int, input().split()))

tmp1 = a[0] + b[1]
tmp2 = a[1] + b[0]

if tmp1 > tmp2:
    print(tmp2)
else:
    print(tmp1)