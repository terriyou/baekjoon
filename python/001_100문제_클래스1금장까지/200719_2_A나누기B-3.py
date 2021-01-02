a = input().split(' ')

if (a[1] == '0'):
    print(-1)
else:
    if (int(a[1]) != abs(int(a[1]))):
        minus_rst = int(a[0]) // abs(int(a[1])) * -1
        print(minus_rst)
    else:
        print(int(a[0]) // int(a[1]))
    print(int(a[0]) % int(a[1]))