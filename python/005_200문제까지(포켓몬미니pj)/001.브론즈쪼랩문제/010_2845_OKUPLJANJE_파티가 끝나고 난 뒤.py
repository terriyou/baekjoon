l,p = map(int, input().split())
ps = list(map(int,input().split()))
ps_minus =  [str(x - l*p) for x in ps]

print(" ".join(ps_minus))