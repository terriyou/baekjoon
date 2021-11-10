
ex_list = [1,2,3]
n = int(input())

for i in range(n):
    inpt = list(map(int, input().split()))
    tmp = ex_list[inpt[0]-1]
    ex_list[inpt[0]-1] = ex_list[inpt[1]-1]
    ex_list[inpt[1]-1] = tmp


for i in range(3):
    if ex_list[i] == 1:
        print(i+1)

