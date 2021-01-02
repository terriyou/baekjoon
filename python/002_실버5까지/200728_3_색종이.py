n = int(input())
jong_e_pos =[]
dou_hwa_ji = []
black_s = 0

for i in range(n):
    jong_e_pos.append(list(map(int, input().split(' '))))

for i in range(100):
    new = []
    for j in range(100):
        new.append(0)
    dou_hwa_ji.append(new)

for i in range(n):
    for j in range(jong_e_pos[i][0],jong_e_pos[i][0] + 10):
        for k in range(jong_e_pos[i][1],jong_e_pos[i][1] + 10):
            dou_hwa_ji[j][k] = 1

for i in range(100):
    for j in range(100):
        if dou_hwa_ji[i][j] == 1:
            black_s = black_s+1

print(black_s)