n = int(input())
cnt = 1
cnt_add = 6
cnt_rst = 1
while n > cnt:
    cnt_rst = cnt_rst + 1
    cnt = cnt + cnt_add
    cnt_add = cnt_add + 6
print(cnt_rst)