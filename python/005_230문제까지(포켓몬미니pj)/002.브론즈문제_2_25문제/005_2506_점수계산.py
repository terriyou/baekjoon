n = int(input())
inpt = list(map(int,input().split()))
cnt = 0
add = 0

for i in inpt:
    if i == 1:
        add += 1
        cnt += add

    if i == 0:
        add_flag = False
        add = 0

print(cnt)