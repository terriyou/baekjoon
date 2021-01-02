a = input()

if len(a) == 2:
    print(int(a[0]) + int(a[1]))
elif len(a) == 3:
    if int(a[-1]) == 0:
        print(int(a[0])+ 10)
    else:
        print(int(a[-1])+ 10)
else:
    print(20)