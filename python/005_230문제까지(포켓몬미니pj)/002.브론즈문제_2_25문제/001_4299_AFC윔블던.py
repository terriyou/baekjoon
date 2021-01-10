hap, cha = map(int,input().split())

if hap-cha<0 or (hap-cha)%2!=0:
    print(-1)
else:
    print((hap+cha)//2,(hap-cha)//2)