n = int(input())
cnt_1 = 0
cnt_2 = 0
for i in range(n+1):
    cnt_1 += i
for i in range(2,2*n+1):
    cnt_2 += i

print(cnt_1)
print(cnt_2)
print(cnt_1 + cnt_2)