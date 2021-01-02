a = input()
pre_sum = 0
sum = 0

for i in range(int(a)):
    b = input()
    sum = 0
    pre_sum = 0
    for j in range(len(b)):
        if j == 0:
           if b[0] == 'O':
               pre_sum = 1
        elif b[j] == 'X':
            pre_sum = 0
        elif b[j-1] == 'O' and b[j] == 'O':
            pre_sum = pre_sum + 1
        elif b[j] == 'O':
            pre_sum = 1
        sum = sum + pre_sum
    print(sum)
