t = int(input())

a_count = 0
b_count = 0
c_count = 0


if t%10 != 0:
    print(-1)
    exit(0)
else:
    cs = t / 10
    bs = cs // 6
    a_s = bs // 5
    if a_s < 0:
        if bs < 0:
            c_count = cs
        else:
            b_count = bs
            c_count = cs - (6 * bs)
    else:
        a_count = a_s
        b_count = bs - (5 * a_s)
        if b_count < 0:
            pass
        else:
            c_count = cs - (6 * bs)

print(str(int(a_count)), str(int(b_count)), str(int(c_count)))
