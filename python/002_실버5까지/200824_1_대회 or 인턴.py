
n,m,k = map(int,input().split())

if n == 2*m:
    team_cnt = m
    while(k>0):
        k = k - 3
        team_cnt = team_cnt - 1
    print(team_cnt)
elif n < 2*m:
    if (n < 2):
        print(0)
    else:
        team_cnt = int(n / 2)
        #print(team_cnt)
        rest_m = m - team_cnt
        rest_w = n % 2
        rest_k = k - rest_m
        rest_k = rest_k - rest_w
        while(rest_k > 0):
            rest_k = rest_k - 3
            team_cnt = team_cnt - 1
        print(team_cnt)
else:
    team_cnt = m
    rest_w = n - 2*m
    rest_k = k - rest_w
    while(rest_k > 0):
        rest_k = rest_k - 3
        team_cnt = team_cnt - 1
    print(team_cnt)