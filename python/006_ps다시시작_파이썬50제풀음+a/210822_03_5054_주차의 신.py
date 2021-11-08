t = int(input())

for _ in range(t):
    n = int(input())
    inpt = list(map(int,input().split()))
    ssum = (max(inpt) - min(inpt)) * 2
    print(ssum) 