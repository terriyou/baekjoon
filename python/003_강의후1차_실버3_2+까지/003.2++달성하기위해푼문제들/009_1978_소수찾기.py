n = int(input())
nums = list(map(int, input().split()))
cnt_total = 0

for i in nums:
    cnt = 0
    if i == 1:
        continue

    for j in range(2,i+1):
        if i % j == 0:
            cnt += 1
    if cnt == 1:
        cnt_total +=1

print(cnt_total)
