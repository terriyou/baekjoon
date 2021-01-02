inpt = int(input())

x3 = -1
x5 = -1

for i in range(0, int(inpt/5)+1):
    tmp = inpt
    if inpt % 5 == 0:
        x5 = int(inpt / 5)
        x3 = 0
        break
    tmp -= i*5
    if tmp % 3 == 0:
        x5 = i
        x3 = int(tmp / 3)

if x3 == -1:
    print(-1)
else:
    print(x5 + x3)
