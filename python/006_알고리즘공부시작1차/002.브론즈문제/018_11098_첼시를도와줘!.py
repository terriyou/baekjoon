n = int(input())
for _ in range(n):
    p = int(input())
    p_list = []
    for i in range(p):
        p_list.append(input().split())
        p_list[i][0] = int(p_list[i][0])
    p_list.sort(key=lambda x :x[0],reverse=True)
    print(p_list[0][1])