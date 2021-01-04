m = int(input())
n = int(input())
cnt = -1
a = [False,False] + [True]*(n-1)
flag = True
for i in range(2,n+1):
    if a[i]:
        if i >= m and i <= n:
            if flag == True:
                smallest = i
                flag = False
            cnt += i
        for j in range(2*i, n+1, i):
            a[j] = False
if cnt != -1:
    print(cnt+1)
    print(smallest)
else:
    print(cnt)