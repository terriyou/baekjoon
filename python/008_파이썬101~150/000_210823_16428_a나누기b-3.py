a,b = map(int,input().split())

if a == 0:
    q = 0
    r = 0
elif a > 0:
    if b > 0:
        q = a // b
        r = a - q * b
    else:
        b *= -1
        q = a // b
        r = a-q*b
        q *= -1
else:
    if b > 0:
        tmp_a = a * -1
        tmp_a = tmp_a + b
        tmp_q = tmp_a // b
        r = tmp_q * b + a
        q = tmp_q * -1
    else:
        tmp_a = a+b
        tmp_a*=-1
        q = tmp_a//(b*-1)
        r = a - b * q
        
print(q)
print(r)