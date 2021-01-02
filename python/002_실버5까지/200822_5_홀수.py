sum = 0
odd_l = []

for i in range(7):
    tmp = int(input())
    if(tmp % 2 == 1):
        sum = sum + tmp
        odd_l.append(tmp)

odd_l.sort()

if (sum == 0):
    print(-1)
else:
    print(sum)
    print(odd_l[0])