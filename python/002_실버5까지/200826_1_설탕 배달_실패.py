n = int(input())

if n < 3:
    print(-1)
    exit(1)
elif n == 3:
    print(1)
    exit(1)
elif n < 5:
    print(-1)
    exit(1)
elif n%5 ==0:
    rst_bj = n//5
elif n%3 ==0:
    rst_bj = n//3
else:
    rst_bj = n//5
    if rst_bj % 3 == 0:
        rst_bj = rst_bj + (n%5) // 3
    else:
        rst_bj = -1

print(rst_bj)