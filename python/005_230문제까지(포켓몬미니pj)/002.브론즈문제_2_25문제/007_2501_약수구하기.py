n,k=map(int,input().split())
hubo = []

for i in range(1,n+1):
    if n % i == 0:
        hubo.append(i)

try:
    print(hubo[k-1])
except:
    print(0)