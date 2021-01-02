from sys import stdin

n = int(stdin.readline())
n_str = stdin.readline().split()
flag = True
for i in range(n):
    if n_str[0][0] != n_str[i][0]:
        flag = False
    
if flag == True:
    print(1)
else:
    print(0)