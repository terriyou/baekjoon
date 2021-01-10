test_num = int(input())
for i in range(test_num):
    s = int(input())
    n = int(input())
    for _ in range(n):
        q,p = map(int,input().split())
        s += q*p
    print(s)