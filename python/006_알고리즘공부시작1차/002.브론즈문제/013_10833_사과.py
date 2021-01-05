n = int(input())
total = 0
for i in range(n):
    st_num, ap_num = map(int,input().split())
    total += ap_num % st_num

print(total)