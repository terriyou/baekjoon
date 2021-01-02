n = int(input())

for i in range(n):
    ps = input()
    tmp = ps
    for j in range(len(ps)):
        tmp = tmp.replace("()","")
    if not tmp:
        print("YES")
    else:
        print("NO")