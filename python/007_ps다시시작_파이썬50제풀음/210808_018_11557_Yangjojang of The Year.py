t = int(input())

for i in range(t):
    n = int(input())
    s = dict(input().split() for _ in range(n))
    s = {str(k):int(v) for k,v in s.items()}
    s_sorted = sorted(s.items(), key = lambda item: item[1], reverse=True)
    print(s_sorted[0][0])