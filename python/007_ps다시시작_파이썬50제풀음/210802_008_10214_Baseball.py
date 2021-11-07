n = int(input())

yonsei = 0
koryou = 0

for i in range(n):
    for j in range(9):
        tmp_y, tmp_k = map(int,input().split())
        yonsei = yonsei + tmp_y
        koryou = koryou + tmp_k
    if yonsei == koryou:
        print("Draw")
    elif yonsei > koryou:
        print("Yonsei")
    else:
        print("Korea")
    yonsei = 0
    koryou = 0