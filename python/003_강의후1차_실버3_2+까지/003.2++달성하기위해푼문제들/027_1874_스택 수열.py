from sys import stdin

n = int(stdin.readline())

stack = []
op = []
count = 1
flag = True
for i in range(n):
    num = int(stdin.readline())
    while count <= num:
        stack.append(count)
        op.append('+')
        count += 1
    if stack[-1] == num:
        stack.pop()
        op.append('-')
    else:
        flag = False
if flag == False:
    print('NO')
else:
    print("\n".join(op))