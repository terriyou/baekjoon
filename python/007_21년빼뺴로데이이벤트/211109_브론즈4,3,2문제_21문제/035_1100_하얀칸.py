inpt = []
cnt = 0
for i in range(8):
    inpt.append(list(map(str, list(input()))))
    for j in range(8):
        if (i+j) % 2 == 0 and inpt[i][j] == 'F':
            cnt += 1

print(cnt)