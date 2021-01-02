a = input().split(' ')
b = a[0][::-1]
c = a[1][::-1]

if b[0] > c[0]:
    print(b)
elif b[0] < c[0]:
    print(c)
else:
    if b[1] > c[1]:
        print(b)
    elif b[1] < c[1]:
        print(c)
    else:
        if b[2] > c[2]:
            print(b)
        elif b[2] < c[2]:
            print(c)
        else:
            print(b)

