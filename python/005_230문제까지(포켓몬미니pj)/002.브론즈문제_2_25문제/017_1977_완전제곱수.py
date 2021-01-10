m = int(input())
n = int(input())
ans = []
i=1

while i*i <= n:
    if i*i >= m and i*i <= n:
        ans.append(i*i)
    i +=1

try:
    i = ans[0]
    print(sum(ans))
    print(ans[0])
except:
    print(-1)
