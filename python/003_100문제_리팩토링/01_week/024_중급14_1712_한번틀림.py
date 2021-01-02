import sys
a,b,c = map(int,input().split())
flag = 0
cnt = 0
if b >= c:
    print(-1)
    sys.exit()

cnt = a//(c-b) +1

print(cnt)

"""
잘못 푼 문제:
if b >= c:
    print(-1)
else:
    while flag >= 0:
        a -= (c-b)
        flag = a
        cnt += 1
print(cnt)
"""