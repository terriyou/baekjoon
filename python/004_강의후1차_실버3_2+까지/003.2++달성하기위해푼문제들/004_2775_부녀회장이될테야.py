t = int(input())

for n in range(t):
    rst = 0   
    inpt_k = int(input())
    inpt_n = int(input())

    list_num = [[0]*15 for _ in range(16)]
    
    for i in range(inpt_k + 1):
        for j in range(1, inpt_n+1):
            if i == 0:
                list_num[i][j] = j
            else:
                for k in range(1,j+1):               
                    list_num[i][j] += list_num[i-1][k]

    print(list_num[inpt_k][inpt_n])
