
a = input().split(' ')
a = list(map(int, a))

a[2] = a[2] - a[0]
a[3] = a[3] - a[1]
min_value = min(a)

print(min_value)