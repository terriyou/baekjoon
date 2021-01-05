n = int(input())
for i in range(1,n+1):
    c,v = map(int,input().split())
    print(f"You get {c//v} piece(s) and your dad gets {c%v} piece(s).")