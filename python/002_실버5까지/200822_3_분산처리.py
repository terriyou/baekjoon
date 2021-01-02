n = int(input())

for i in range(n):
    a,b=map(int,input().split(" "))
    b = b % 4 + 4
    bf_rst = (a**b)%10

    if bf_rst == 0:
        print(10)
    else:
        print(bf_rst)