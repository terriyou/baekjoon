
iter = int(input())
list_b = []
tmp_cnt = 1
rst_str = []

for i in range(iter):
    list_b.append(list(map(int, input().split(' '))))

for i in range(iter):
    for j in range(iter):
        if list_b[i][0] < list_b[j][0] and list_b[i][1] < list_b[j][1]:
            tmp_cnt = tmp_cnt + 1
    rst_str.append(str(tmp_cnt))
    tmp_cnt = 1
    if not i == (iter - 1):
        rst_str.append(" ")

rst_str = ''.join(rst_str)

print(rst_str)