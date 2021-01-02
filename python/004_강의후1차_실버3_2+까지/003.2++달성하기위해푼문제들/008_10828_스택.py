import sys
n = int(sys.stdin.readline())
stack = []
for _ in range(n):
    cmd = sys.stdin.readline().split()
    if cmd[0] == 'push':
        stack.append(int(cmd[1]))
    elif cmd[0] == 'pop':
        if not stack:
            print('-1')
        else:
            print(stack[-1])
            stack.pop(-1)
    elif cmd[0] == 'size':
        print(len(stack))
    elif cmd[0] == 'empty':
        if not stack:
            print('1')
        else:
            print('0')
    elif cmd[0] == 'top':
        if not stack:
            print('-1')
        else:
            print(stack[-1])