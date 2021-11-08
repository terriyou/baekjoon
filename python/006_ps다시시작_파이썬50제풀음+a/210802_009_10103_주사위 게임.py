n = int(input())
c = 100
s = 100

for i in range(n):
    tmp_c, tmp_s = map(int, input().split())
    if tmp_c > tmp_s:
        s = s - tmp_c
    elif tmp_c < tmp_s:
        c = c - tmp_s
    else:
        pass

print(c)
print(s)