n, m = map(int,input().split())

inpt_chess = [[0]*m for _ in range(n)]

dif_cnt = [[[0]*(m-7) for _ in range(n-7)], [[0]*(m-7) for _ in range(n-7)]]

cmp_chess = [[[0,1,0,1,0,1,0,1],
              [1,0,1,0,1,0,1,0],
              [0,1,0,1,0,1,0,1],
              [1,0,1,0,1,0,1,0],
              [0,1,0,1,0,1,0,1],
              [1,0,1,0,1,0,1,0],
              [0,1,0,1,0,1,0,1],
              [1,0,1,0,1,0,1,0]],
             [[1,0,1,0,1,0,1,0],
              [0,1,0,1,0,1,0,1],
              [1,0,1,0,1,0,1,0],
              [0,1,0,1,0,1,0,1],
              [1,0,1,0,1,0,1,0],
              [0,1,0,1,0,1,0,1],
              [1,0,1,0,1,0,1,0],
              [0,1,0,1,0,1,0,1]]]

for i in range(n):
    m_one_list = input()
    for j in range(m):
        if m_one_list[j] == 'W':
            inpt_chess[i][j] = 1
        else:
            inpt_chess[i][j] = 0

for a in range(n-7):
    for b in range(m-7):
        for c in range(2):
            for d in range(8):
                for e in range(8):
                    if inpt_chess[d+a][e+b] != cmp_chess[c][d][e]:
                        dif_cnt[c][a][b] += 1

output = min(list(map(min, dif_cnt[0])) + list(map(min, dif_cnt[1])))

print(output)