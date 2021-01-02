n = input()
n_len = len(n)
n_int = int(n)
tmp_str = ""
flag = 0

for i in range(n_len*9,1,-1):
    check = 0
    tmp = n_int-i
    if tmp < 0:
        continue
    tmp_str = str(tmp)
    for j in range(len(tmp_str)):
        check = check + int(tmp_str[j]) 
    if check + tmp == n_int:
        print(tmp)
        flag = 1
        break
    else:
        continue

if flag == 0:
    print(0)