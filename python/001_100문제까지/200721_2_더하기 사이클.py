import sys
a = input()
b = a
sum = 0
rest = 0
cnt = 1

if(a=='0'):
    print(1)
    sys.exit()

if (len(b)) == 1:
    rest = int(b) % 10
    b = b + str(rest)
else:
    sum = int(b[0]) + int(b[1])
    rest = sum % 10
    b = b[1] + str(rest)

while ( str(a) != str(b)):
    if (len(b)) == 1:
        rest = int(b) % 10
        b = b + str(rest)
    else:
        sum = int(b[0]) + int(b[1])
        rest = sum % 10
        b = b[1] + str(rest)
        b = b.lstrip('0')
    cnt = cnt + 1

print(cnt)