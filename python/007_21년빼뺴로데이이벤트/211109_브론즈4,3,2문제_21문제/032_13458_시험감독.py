n = int(input())
each_cnt = list(map(int, input().split()))
b, c = map(int, input().split())

sup_cnt = 0
sub_sup_cnt = 0

for i in each_cnt:
    rest_human = i - b
    sup_cnt += 1
    if rest_human <= 0:
        pass
    else:
        sub_sup_cnt += int(rest_human / c if rest_human % c == 0 else rest_human / c +1)

print(sup_cnt + sub_sup_cnt)

