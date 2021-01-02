from sys import stdin
n = int(stdin.readline())
daque = []
for _ in range(n):
    cmd = stdin.readline().split()
    if cmd[0] == 'push_back':
        daque.append(int(cmd[1]))
    elif cmd[0] == 'push_front':
        daque.insert(0,int(cmd[1]))
    elif cmd[0] == 'pop_front':
        if not daque:
            print('-1')
        else:
            print(daque[0])
            del daque[0]
    elif cmd[0] == 'pop_back':
        if not daque:
            print('-1')
        else:
            print(daque[-1])
            daque.pop(-1)
    elif cmd[0] == 'size':
        print(len(daque))
    elif cmd[0] == 'empty':
        if not daque:
            print('1')
        else:
            print('0')
    elif cmd[0] == 'front':
        if not daque:
            print('-1')
        else:
            print(daque[0])
    elif cmd[0] == 'back':
        if not daque:
            print('-1')
        else:
            print(daque[-1])

