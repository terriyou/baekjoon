inpt = list(map(int, input().split('/')))

if inpt[0] + inpt[2] < inpt[1] or inpt[1] == 0:
    print('hasu')
else:
    print('gosu')