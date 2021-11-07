k, n, m = map(int,input().split())
flag = m-(k*n)

if flag < 0:
    print(-1*flag)
else:
    print(0)