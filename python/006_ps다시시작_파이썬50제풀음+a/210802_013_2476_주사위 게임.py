n = int(input())

ns = []
abc = [0,0,0]

for i in range(n):
    abc[0],abc[1],abc[2] = map(int,input().split())
    if abc[0] == abc[1] and abc[1] == abc[2]:
        ns.append(10000+abc[0]*1000)
    elif abc[0] == abc[1] or abc[1] == abc[2]:
        ns.append(1000+abc[1]*100)
    elif abc[0] == abc[2]:
        ns.append(1000+abc[0]*100)
    else:
        ns.append(max(abc)*100)

print(max(ns))



