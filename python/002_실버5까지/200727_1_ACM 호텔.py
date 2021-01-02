
iter = int(input())
rst = []

for i in range(iter):
    h,w,n = map(int, input().split(' '))
    xx = n // h
    xx = xx +1   
    yy = n % h
    if yy == 0:
        yy = h
        xx = xx - 1
    if (len(str(xx)) == 1):
        rst.append(str(yy) + '0' + str(xx))
    else:
        rst.append(str(yy) + str(xx))

for i in range(iter):
    print(rst[i])


