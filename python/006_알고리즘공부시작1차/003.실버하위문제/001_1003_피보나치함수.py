n = int(input())
zero_cnt = [1,0,1]
one_cnt = [0,1,1]


for i in range(n):
    zero_cnt = [1,0,1]
    one_cnt = [0,1,1]
    inpt = int(input())    
    if inpt < 3:
        print(zero_cnt[inpt], one_cnt[inpt])
        continue
    for j in range(3, inpt+1):
        zero_cnt.append(one_cnt[j-1])
        one_cnt.append(zero_cnt[j-1] + one_cnt[j-1])

    print(zero_cnt[inpt], one_cnt[inpt])